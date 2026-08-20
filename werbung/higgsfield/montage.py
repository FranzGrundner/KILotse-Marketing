"""montage.py — aus Higgsfield-Rohclips einen fertigen Facebook-Post bauen.

Die Roh-MP4s aus Higgsfield sind **b-roll**: Bild ohne Aussage. Was den Post
ausmacht — Kernsatz, Marke, Abspann, Ton — entsteht hier lokal, so wie beim
Werbevideo #160 und beim Poolservice-Clip. Damit gilt der Trick aus §5 des
Plans: DE und EN teilen sich dieselbe Bildspur, nur Text und Stimme wechseln.
Aus 3 generierten Clips werden 2 fertige Posts.

Die Bildspur wird nicht Frame fuer Frame in Python gebaut (das waere bei
fremdem Videomaterial sinnlos langsam), sondern in ffmpeg zusammengesetzt.
Gezeichnet wird nur, was oben drauf liegt: die Textebene und der Abspann — mit
PIL und denselben Marken-Tokens wie die uebrigen Videos.

Aufruf:
    python -X utf8 montage.py --dummy      Platzhalter erzeugen, Kette pruefen
    python -X utf8 montage.py              DE bauen (aus roh/)
    python -X utf8 montage.py --sprache en
    python -X utf8 montage.py --beide --ohne-stimme
"""
import argparse
import asyncio
import json
import math
import os
import shutil
import subprocess
import sys
import tempfile

from PIL import Image, ImageDraw, ImageFilter

BASIS = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(BASIS)))      # ../video.py

import edge_tts                                               # noqa: E402
from video import (AKZENT, ASSETS_DIR, BG, LOGOS_DIR, WEISS,   # noqa: E402
                   auftritt, bild_einsetzen, mischen, schrift, text_bei,
                   weich)

ROH = os.path.join(BASIS, "roh")
FERTIG = os.path.join(BASIS, "fertig")
SPRECHER = os.path.join(BASIS, "sprecher")

BREITE, HOEHE = 1080, 1350            # 4:5 — fuellt die Feed-Spalte
FPS = 30
ABSPANN_S = 3.0
BLENDE = 0.4                          # Ein- und Ausblenden der Textebene
MAX_SHOT_S = 6.0                      # laenger wird ein b-roll-Clip nicht gebraucht
VERLAUF = 200                         # Deckkraft der Abdunklung unter dem Text
                                      # (0…255). Hochdrehen, wenn ein Shot in
                                      # ausgebranntem Strandlicht endet.
LAUTHEIT = -16.0                      # LUFS; Facebook normalisiert selbst,
                                      # LINE und WhatsApp nicht.

# Franz' Stimme ist multilingual — dieselbe Stimme traegt DE und EN, was fuer
# eine Marke mehr wert ist als eine perfekte Muttersprachler-Aussprache.
STIMME = "de-DE-FlorianMultilingualNeural"
TEMPO = "-4%"

# Die Clips aus prompts.md. Reihenfolge der Shots = Reihenfolge im fertigen Post.
# `ordner` ist der Unterordner in roh/ und sprecher/<sprache>/ — der Eyecatcher
# liegt aus historischen Gruenden flach darin und bleibt deshalb auf "".
CLIPS = {
    "01-eyecatcher": {
        "ordner": "",
        "shots": [
            # Ohne den Handumbruch fiel „not." als Waise in die zweite Zeile —
            # und an der Verneinung haengt der ganze Satz. Die deutsche Fassung
            # passt in eine Zeile und bleibt deshalb ohne „\n".
            {"datei": "01-buero",
             "de": "Alle sind draußen. Du nicht.",
             "en": "Everyone's outside.\nYou're not."},
            {"datei": "02-arm",
             "de": "Das muss nicht so sein.",
             "en": "It doesn't have to be."},
            {"datei": "03-hinaus",
             "de": "Ich zeige dir den Weg.",
             "en": "Let me show you the way."},
        ],
    },
    "02-cafe": {
        "ordner": "02-cafe",
        # Kling liefert 7 s; drei davon plus Abspann waeren 21 s und damit
        # ueber der 8–20-s-Regel aus §6 des Plans. 5 s je Shot ergibt 18 s.
        "max_shot": 5.0,
        "shots": [
            {"datei": "01-grau",
             "de": "Nicht das Café ist müde.",
             "en": "It's not the café that's tired."},
            # Umbruch zwischen die beiden Saetze statt dorthin, wo die Zeile
            # zufaellig voll ist: sonst standen „mehr." bzw. „paperwork."
            # allein in der zweiten Zeile.
            {"datei": "02-bunt",
             "de": "Gleicher Raum.\nKeine Zettel mehr.",
             "en": "Same room.\nNo more paperwork."},
            {"datei": "03-hinaus",
             "de": "Und der Abend gehört dir.",
             "en": "And the evening is yours."},
        ],
    },
    "03-pool": {
        "ordner": "03-pool",
        "max_shot": 5.0,
        "shots": [
            # Ein einziger Satz, also keine Satzgrenze zum Umbrechen: getrennt
            # wird vor der Verneinung, damit „nicht da.«" zusammenbleibt.
            # Vorher stand „da.«" allein — ein verwaistes Schlusszeichen.
            {"datei": "01-vorwurf",
             "de": "»Ihr wart letzte Woche\nnicht da.«",
             "en": "“You weren't here last week.”"},
            {"datei": "02-beweis",
             "de": "Doch. Foto, Datum, Name.",
             "en": "Yes we were.\nPhoto, date, name."},
            {"datei": "03-weg",
             "de": "Diskussion beendet.",
             "en": "Argument over."},
        ],
    },
    "04-lotse": {
        "ordner": "04-lotse",
        "max_shot": 5.0,
        "shots": [
            # Umbrueche von Hand: sonst faellt die Verneinung („nicht.") bzw.
            # das Satzende („are.") als Waise in die zweite Zeile — und im
            # ersten Satz haengt genau daran die Aussage.
            {"datei": "01-frachter",
             "de": "Der Lotse steuert\ndein Schiff nicht.",
             "en": "A pilot doesn't\nsteer your ship."},
            {"datei": "02-haende",
             "de": "Er kennt die Untiefen.",
             "en": "He knows where\nthe rocks are."},
            {"datei": "03-abdrehen",
             "de": "Du bleibst am Steuer.\nIch kenne den Weg.",
             "en": "You stay at the wheel.\nI know the way."},
        ],
    },
    "05-uhren": {
        "ordner": "05-uhren",
        "max_shot": 5.0,
        "shots": [
            # Shot 1 und 2 kommen aus DERSELBEN Bilddatei, nur mit zwei
            # Videoprompts — deshalb steht die Uhr in beiden nachweislich
            # gleich. Siehe prompts.md, „Die Regel, an der dieser Clip haengt".
            #
            # Die Uhrzeit richtet sich nach dem BILD, nicht umgekehrt: das
            # Modell hat die Zeiger auf 3 Uhr gestellt (Minutenzeiger 12,
            # Stundenzeiger 3, in beiden Shots identisch). Der urspruengliche
            # Text sagte 23:40 — ein Zuschauer, der die Uhr liest, haette den
            # Widerspruch gesehen. 3 Uhr frueh ist ausserdem das haertere Bild.
            {"datei": "01-nochmal",
             "de": "3 Uhr früh.\nUnd du sitzt noch da.",
             "en": "3 a.m.\nYou're still at the desk."},
            {"datei": "02-gehen",
             "de": "Gleiche Uhrzeit.\nDu gehst.",
             "en": "Same time.\nYou're leaving."},
            {"datei": "03-draussen",
             "de": "Dafür bist du hergekommen.",
             "en": "This is what you came for."},
        ],
    },
    # ACHTUNG: Dieser Clip gehoert NICHT zu KI-Lotse, sondern zur gemeinsamen
    # Firma mit Andi — die hat noch keinen Namen und kein Erscheinungsbild.
    # Grund, Logo, Avatar und Domain sind hier Platzhalter zu Demozwecken; wird
    # der Clip verwendet, wird der Abspann komplett neu gemacht (Andi).
    # Nicht in die KI-Lotse-Rotation stellen. Siehe prompts.md, Kasten oben am
    # Abschnitt „Die gute Fee".
    "06-fee": {
        "ordner": "06-fee",
        # Seedance liefert 8 s; drei davon plus Abspann waeren 27 s. 5 s je
        # Shot ergibt 18 s wie bei den uebrigen Clips.
        "max_shot": 5.0,
        # Der erste Clip mit eigenem Abspann: er verkauft ein Erzeugnis, nicht
        # die Kategorie. Der Satz ist die Aussage des ganzen Clips in Worten —
        # der Zauberstab wechselt die Hand, das Werkzeug bleibt unseres.
        #
        # `held` schaltet den bewegten Abspann ein: der Name blitzt auf, als
        # haette ihn der Stab geschrieben. Bleibt die Ausnahme fuer Clips, die
        # ein Erzeugnis benennen — die uebrigen fuenf behalten das Standbild.
        "held": {"de": "MyPro", "en": "MyPro"},
        # KEIN „KI-Lotse" und KEINE Domain: der Clip gehoert der gemeinsamen
        # Firma, und die hat noch keinen Namen. Ein Absender, der den falschen
        # Namen nennt, ist schlimmer als gar keiner — lieber eine Leerstelle,
        # die Andi spaeter fuellt.
        "domain": None,
        "abspann": {
            "de": ("KI-Automatisierung durch dich, "
                   "mit modernster Technik von uns",
                   "Franz Grundner · Pattaya"),
            "en": ("AI automation by you, built on our technology",
                   "Franz Grundner · Pattaya"),
        },
        # Karte und Stimme sagen hier dasselbe: die Saetze sind kurz genug zum
        # Lesen und vollstaendig genug zum Sprechen. `sprech_*` wird deshalb
        # nicht gebraucht — es bleibt fuer Clips, wo beides auseinanderfaellt.
        #
        # Die Sprachdateien kommen NICHT von edge-tts, sondern aus Higgsfield
        # (Eleven v3) und liegen fertig in `sprecher/<sprache>/06-fee/`.
        # `stimmen()` erzeugt nur, was fehlt — die Dateien bleiben also stehen.
        # Grund: edge-tts hat „veraltete" zu englischem Kauderwelsch verschliffen.
        #
        # Kein „KI-Lotse" und keine Domain im Sprechtext (siehe `domain`).
        "shots": [
            {"datei": "01-grab",
             "de": "Software von gestern?",
             "en": "Software from yesterday?"},
            {"datei": "02-fee",
             "de": "Nicht mehr auf dem Stand\nvon heute?",
             "en": "Not where it should be\ntoday?"},
            # Zwei Saetze, also wird zwischen ihnen umbrochen — der zweite ist
            # die Aussage des ganzen Clips und darf nicht zerrissen werden.
            #
            # „Schwingen musst du ihn" ist ohne Betonung ein angefangener Satz;
            # mit Kontrastbetonung auf DU ist er vollstaendig (Franz, 14.08.).
            # Die Betonung gehoert deshalb ins Ohr und nicht ins Auge: Auf der
            # Karte bleibt „du" klein, im Sprechtext steht „DU".
            #
            # Die Alternative „…musst du ihn selbst" wurde verworfen, und der
            # Grund gilt ueber diesen Satz hinaus: **„du" ist eine Aufforderung,
            # „selbst" eine Einschraenkung** (Franz). Der Clip verkauft
            # Ermaechtigung — „selbst" haette daraus „du bist auf dich gestellt"
            # gemacht, an genau der Stelle, an der die Aussage steht.
            {"datei": "03-verwandlung",
             "de": "MyPro ist dein Zauberstab.\nSchwingen musst du ihn.",
             "en": "MyPro is your magic wand.\nYou do the waving.",
             "sprech_de": "MyPro ist dein Zauberstab. Schwingen musst DU ihn!"},
        ],
    },
    # Einziger Clip mit nur EINEM Shot: die Verwandlung passiert innerhalb der
    # Aufnahme, nicht zwischen drei Einstellungen. Deshalb auch nur eine
    # Textkarte — sie steht am Schluss und ist die ganze Aussage.
    "12-wiese": {
        "ordner": "12-wiese",
        # Der Rohclip ist 5,04 s; ohne max_shot wuerde MAX_SHOT_S kuerzen und
        # ausgerechnet das Ende wegschneiden — dort steht die fertige Stadt,
        # wegen der es den Shot gibt.
        "max_shot": 5.0,
        # Wie beim Fee-Clip: gehoert der gemeinsamen Firma, nicht KI-Lotse.
        # Anders als dort steht der Name jetzt drin — Franz benutzt GYDE seit
        # dem 20.08. aktiv. Bleibt das Erscheinungsbild Andis Sache, ist das
        # hier eine Zeile Aenderung.
        "domain": None,
        "abspann": {
            "de": ("KI-Automatisierung durch dich, "
                   "mit modernster Technik von uns",
                   "GYDE"),
            "en": ("AI automation by you, built on our technology",
                   "GYDE"),
        },
        # Die Stimme sagt woertlich, was auf der Karte steht — ein Satz, der
        # kurz genug zum Lesen und vollstaendig genug zum Sprechen ist, braucht
        # kein `sprech_*`.
        #
        # Hier kommt edge-tts zum Zug, nicht Eleven v3 wie beim Fee-Clip: Der
        # Satz hat kein Fremdwort und keine Abkuerzung, an denen sich edge-tts
        # damals verschluckt hat („veraltete" wurde zu englischem Kauderwelsch).
        # Wenn die Stimme zu synthetisch klingt, ist der Ersatz ein Eintrag in
        # `sprecher/<sprache>/12-wiese/01-wachstum.mp3` — vorhandene Dateien
        # laesst `stimmen()` stehen.
        #
        # „Bau dir" statt „Bau selbst": „du" ist eine Aufforderung, „selbst"
        # eine Einschraenkung — dieselbe Regel wie beim Zauberstab oben.
        "shots": [
            {"datei": "01-wachstum",
             "de": "Bau dir was du willst.",
             "en": "Build whatever you want."},
        ],
    },
}

# Im Schlussbild steht, WAS verkauft wird — nicht noch einmal der Claim: der
# steht als Textkarte im Bild davor, und ohne die Kategorie weiss ein
# Zuschauer, der den Clip weitergeleitet bekommt, nicht, worum es ueberhaupt
# geht. Formulierung wortgleich zur Homepage (<title> von ki-lotse.tech).
ABSPANN = {
    "de": ("KI & Automatisierung für kleine Betriebe",
           "Franz Grundner · KI-Lotse · Pattaya"),
    # "KI-Lotse" bleibt im Deutschen der Name; auf Englisch sagt die Abkuerzung
    # niemandem etwas (KI = deutsch fuer AI), darum hier die englische Fassung.
    "en": ("AI & automation for small businesses",
           "Franz Grundner · AI guide · Pattaya"),
}


# ── Werkzeug ────────────────────────────────────────────────────────────────
def ffmpeg(*args):
    subprocess.run(["ffmpeg", "-y", "-v", "error", *args], check=True)


def dauer(pfad):
    aus = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "json", pfad], capture_output=True, text=True, check=True)
    return float(json.loads(aus.stdout)["format"]["duration"])


def lautheit(pfad):
    """Integrierte Lautheit einer Datei in LUFS (gemessen, nicht geschaetzt).

    Notwendig, weil `loudnorm` als Filter in der Kette einstufig arbeitet und
    bei Schnipseln von zwei, drei Sekunden — genau die Laenge dieser Saetze —
    daneben liegt: die deutsche und die englische Fassung kamen so 2,4 dB
    auseinander heraus, obwohl beide auf dasselbe Ziel normiert waren.
    """
    aus = subprocess.run(
        ["ffmpeg", "-v", "info", "-i", pfad, "-af",
         "loudnorm=print_format=json", "-f", "null", "-"],
        capture_output=True, text=True, check=True).stderr
    return float(json.loads(aus[aus.rindex("{"):aus.rindex("}") + 1])["input_i"])


def umbrechen(d, inhalt, font, maxbreite):
    zeilen, zeile = [], ""
    for wort in inhalt.split():
        versuch = f"{zeile} {wort}".strip()
        if d.textlength(versuch, font=font) <= maxbreite or not zeile:
            zeile = versuch
        else:
            zeilen.append(zeile)
            zeile = wort
    if zeile:
        zeilen.append(zeile)
    return zeilen


# ── Die Ebenen, die lokal entstehen ─────────────────────────────────────────
def textebene(satz, ziel):
    """Transparentes PNG: Kernsatz ueber einem Verlauf.

    Der Verlauf ist Pflicht, nicht Zierde — b-roll wechselt von dunkel (Buero)
    zu ausgebrannt hell (Strand), und weisser Text auf hellem Sand ist weg.
    """
    ebene = Image.new("RGBA", (BREITE, HOEHE), (0, 0, 0, 0))

    verlauf = Image.new("L", (1, HOEHE), 0)
    for y in range(HOEHE):
        anteil = max(0.0, (y - HOEHE * 0.52) / (HOEHE * 0.48))
        verlauf.putpixel((0, y), int(VERLAUF * anteil ** 1.4))
    ebene.paste(Image.new("RGBA", (BREITE, HOEHE), (10, 14, 20, 255)),
                (0, 0), verlauf.resize((BREITE, HOEHE)))

    d = ImageDraw.Draw(ebene)
    f = schrift(64, fett=True)
    # Ein "\n" im Satz erzwingt einen Umbruch. Noetig, weil der automatische
    # Umbruch gierig ist und keine Satzgrenzen kennt: „Du bleibst am Steuer. Ich
    # / kenne den Weg." trennt mitten im zweiten Satz. Bei zwei kurzen Saetzen
    # auf einer Karte gehoert der Umbruch zwischen die Saetze, nicht dahin, wo
    # die Zeile zufaellig voll ist.
    zeilen = []
    for absatz in satz.split("\n"):
        zeilen += umbrechen(d, absatz, f, BREITE - 160)
    # Von unten setzen, mit Sicherheitsabstand: Facebook legt im Feed eigene
    # Bedienelemente ueber den unteren Rand.
    y = HOEHE - 210 - len(zeilen) * 78
    for zeile in zeilen:
        d.text((80, y), zeile, font=f, fill=(255, 255, 255, 255))
        y += 78
    ebene.save(ziel)


def abspannbild(sprache, ziel, clip=None):
    """Markenflaeche als Standbild — der Abspann braucht keine Bewegung.

    Ein Clip darf die beiden Zeilen ueberschreiben (`abspann` im CLIPS-Eintrag),
    wenn er ein bestimmtes Erzeugnis verkauft statt der Kategorie.

    **`domain: None` schaltet die ganze KI-Lotse-Marke ab**, nicht nur die
    Adresszeile: Teal, Kompass-Logo und Franz' Avatar sind der Auftritt EINER
    Firma, und ein Clip der gemeinsamen Firma darf ihn nicht tragen. Uebrig
    bleibt eine neutrale dunkle Flaeche mit dem Namen aus `abspann` — bewusst
    nicht in Franz' Stil, damit Andi sich daran reiben kann (dieselbe
    Ueberlegung wie bei der Platzhalterseite zur Kampagne).

    Bis zum 20.08.2026 stand „ki-lotse.tech" hier fest verdrahtet; `domain`
    wurde nur im bewegten Abspann ausgewertet. Der Fee-Clip fiel nicht auf,
    weil er ueber `held` den bewegten Weg nimmt.
    """
    eigen = (clip or {}).get("domain", "ki-lotse.tech")
    blatt = Image.new("RGB", (BREITE, HOEHE), AKZENT if eigen else (14, 16, 20))
    d = ImageDraw.Draw(blatt)
    if eigen:
        bild_einsetzen(blatt, os.path.join(ASSETS_DIR, "logo-icon-weiss.png"),
                       (390, 470), 210, 1.0)
        bild_einsetzen(blatt,
                       os.path.join(ASSETS_DIR, "avatar-franz-rund-512.png"),
                       (700, 470), 250, 1.0)
    kategorie, name = (clip or {}).get("abspann", ABSPANN)[sprache]
    f_kat = schrift(44)
    for i, zeile in enumerate(umbrechen(d, kategorie, f_kat, BREITE - 120)):
        text_bei(d, (BREITE // 2, 720 + i * 58), zeile, f_kat, WEISS, anker="mm")
    if eigen:
        text_bei(d, (BREITE // 2, 870), eigen, schrift(72, fett=True),
                 WEISS, anker="mm")
        text_bei(d, (BREITE // 2, 975), name, schrift(34, leicht=True),
                 mischen(AKZENT, WEISS, 0.85), anker="mm")
    else:
        # Ohne Domainzeile rueckt der Name auf deren Platz und wird zur
        # Hauptsache — bei einem Namen ohne Erscheinungsbild ist er alles,
        # was die Flaeche zu zeigen hat. Weite Sperrung, damit die vier
        # Buchstaben als Wortmarke stehen und nicht als Wort gelesen werden.
        text_bei(d, (BREITE // 2, 880), " ".join(name), schrift(96, fett=True),
                 WEISS, anker="mm")
    blatt.save(ziel)


# Auftritt des bewegten Abspanns, in Sekunden ab Segmentbeginn. Die Reihenfolge
# ist die Leserichtung: erst wer, dann was, dann wohin.
TAKT = {"marke": 0.10, "held": 0.55, "satz": 1.15, "domain": 1.75, "name": 2.15}
HELD_GROESSE = 108
HELD_Y = 730                          # Mitte des Erzeugnisnamens
MARKE_Y = 450                         # Mitte von Logo und Avatar
FUNKEN = 16


def abspannbilder(sprache, clip, ordner):
    """Der Abspann als Bildfolge — die Worte tauchen nacheinander auf.

    Nur fuer Clips mit `held` im CLIPS-Eintrag; alle uebrigen behalten das
    Standbild aus `abspannbild()`. Eine Marke, die bei jedem Post anders
    auftritt, ist keine Marke mehr — die Bewegung ist die Ausnahme fuer den
    einen Clip, der ein Erzeugnis beim Namen nennt.

    **Hier kommt kein Modell ran.** Videomodelle schreiben bei Text Kauderwelsch
    (die Baustein-Regel ganz oben in `prompts.md`), und beim KI-Lotse-Intro hat
    dieselbe Einsicht schon einmal zum lokalen Rendern gefuehrt. Schrift ist
    Handwerk, kein Generat.

    Rueckgabe: Liste der Frame-Pfade in Reihenfolge.
    """
    held = clip["held"][sprache]
    satz, name = clip.get("abspann", ABSPANN)[sprache]
    f_satz, f_dom, f_name = schrift(40), schrift(68, fett=True), schrift(32,
                                                                        leicht=True)
    # Umbruch einmal vorweg messen, nicht in jedem der neunzig Frames.
    mess = ImageDraw.Draw(Image.new("RGB", (10, 10)))
    zeilen = umbrechen(mess, satz, f_satz, BREITE - 140)

    pfade = []
    for k in range(int(ABSPANN_S * FPS)):
        t = k / FPS
        blatt = Image.new("RGB", (BREITE, HOEHE), AKZENT)

        a_marke = auftritt(t, TAKT["marke"], 0.50)
        if a_marke > 0.01:
            bild_einsetzen(blatt, os.path.join(ASSETS_DIR, "logo-icon-weiss.png"),
                           (390, MARKE_Y), 210, a_marke)
            bild_einsetzen(blatt,
                           os.path.join(ASSETS_DIR, "avatar-franz-rund-512.png"),
                           (700, MARKE_Y), 250, a_marke)

        # Der Held blitzt auf, als haette ihn der Zauberstab geschrieben: ein
        # weisser Schein, der mit dem Wort kommt und sofort wieder abfaellt,
        # dazu ein letztes Aufziehen von 88 auf 100 Prozent.
        a_held = auftritt(t, TAKT["held"], 0.40)
        if a_held > 0.01:
            skala = 0.88 + 0.12 * a_held
            f_held = schrift(int(HELD_GROESSE * skala), fett=True)
            schein = max(0.0, 1.0 - (t - TAKT["held"]) / 0.75) * a_held
            if schein > 0.02:
                maske = Image.new("L", (BREITE, HOEHE), 0)
                ImageDraw.Draw(maske).text((BREITE // 2, HELD_Y), held,
                                           font=f_held, fill=255, anchor="mm")
                maske = maske.filter(ImageFilter.GaussianBlur(22))
                blatt.paste(Image.new("RGB", (BREITE, HOEHE), WEISS), (0, 0),
                            maske.point(lambda p: int(p * schein)))
            d = ImageDraw.Draw(blatt)
            funken(d, t, schein)
            d.text((BREITE // 2, HELD_Y), held, font=f_held,
                   fill=mischen(AKZENT, WEISS, a_held), anchor="mm")

        d = ImageDraw.Draw(blatt)
        a_satz = auftritt(t, TAKT["satz"], 0.45)
        if a_satz > 0.01:
            for i, zeile in enumerate(zeilen):
                d.text((BREITE // 2, 860 + i * 52), zeile, font=f_satz,
                       fill=mischen(AKZENT, WEISS, a_satz), anchor="mm")
        # `domain: None` laesst die Zeile weg und rueckt den Namen hoch. Fuer
        # Clips, die NICHT zu KI-Lotse gehoeren: eine Domain, die den falschen
        # Absender nennt, ist schlimmer als gar keine.
        domain = clip.get("domain", "ki-lotse.tech")
        a_dom = auftritt(t, TAKT["domain"], 0.40)
        if domain and a_dom > 0.01:
            d.text((BREITE // 2, 1030), domain, font=f_dom,
                   fill=mischen(AKZENT, WEISS, a_dom), anchor="mm")
        a_name = auftritt(t, TAKT["name"], 0.40)
        if a_name > 0.01:
            d.text((BREITE // 2, 1115 if domain else 1020), name, font=f_name,
                   fill=mischen(AKZENT, WEISS, 0.85 * a_name), anchor="mm")

        pfad = os.path.join(ordner, f"ab{k:04d}.png")
        blatt.save(pfad)
        pfade.append(pfad)
    return pfade


def funken(d, t, schein):
    """Der Funkenkranz um den Held — fliegt auseinander und verlischt.

    Die Bahnen stehen fest gerechnet statt gewuerfelt: ein zweiter Lauf muss
    denselben Abspann liefern, sonst laesst sich nichts vergleichen.
    """
    if schein <= 0.02:
        return
    alter = max(0.0, t - TAKT["held"])
    for k in range(FUNKEN):
        w = k * (2 * math.pi / FUNKEN) + 0.35
        weite = (170 + 55 * ((k * 7) % 5)) * weich(alter / 0.9)
        x = BREITE // 2 + math.cos(w) * weite * 1.7      # breit wie das Wort
        y = HELD_Y + math.sin(w) * weite * 0.6
        r = 2 + 3 * schein
        d.ellipse([x - r, y - r, x + r, y + r],
                  fill=mischen(AKZENT, WEISS, min(1.0, schein * 1.4)))


# ── Bildspur ────────────────────────────────────────────────────────────────
def segment(quelle, text_png, start, laenge, ziel):
    """Ein Rohclip: auf 4:5 bringen, Textebene darueber, Laenge festzurren.

    `increase` + `crop` statt `decrease` + Balken: schwarze Balken kosten im
    Feed die halbe Aufmerksamkeit. Was Higgsfield in 16:9 liefert, wird auf die
    Bildmitte beschnitten — die Prompts sind darauf ausgelegt.

    Gekuerzt wird **vorne**, nicht hinten: bei einer Kamerafahrt liegt die
    Pointe am Ende (die Einstellung, auf die zugefahren wird). Wer hinten
    abschneidet, wirft genau das Bild weg, wegen dem der Shot existiert.
    """
    kette = (
        f"[0:v]scale={BREITE}:{HOEHE}:force_original_aspect_ratio=increase,"
        f"crop={BREITE}:{HOEHE},setsar=1,fps={FPS},"
        f"trim={start:.2f}:{start + laenge:.2f},"
        f"setpts=PTS-STARTPTS[v];"
        f"[1:v]format=rgba,fade=t=in:st=0:d={BLENDE}:alpha=1,"
        f"fade=t=out:st={max(0.1, laenge - BLENDE):.2f}:d={BLENDE}:alpha=1[ov];"
        f"[v][ov]overlay=0:0:format=auto[aus]"
    )
    ffmpeg("-i", quelle, "-loop", "1", "-t", f"{laenge:.2f}", "-i", text_png,
           "-filter_complex", kette, "-map", "[aus]",
           "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "19",
           "-r", str(FPS), "-an", ziel)


def abspannsegment(bild, ziel):
    kette = (f"[0:v]fps={FPS},setsar=1,fade=t=in:st=0:d=0.5[aus]")
    ffmpeg("-loop", "1", "-t", f"{ABSPANN_S}", "-i", bild,
           "-filter_complex", kette, "-map", "[aus]",
           "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "19",
           "-r", str(FPS), ziel)


def abspannsegment_bewegt(muster, ziel):
    """Dasselbe aus einer Bildfolge. Laenge und Anfangsblende bleiben gleich,
    damit der Schnitt vom letzten Shot her unveraendert sitzt."""
    kette = "[0:v]setsar=1,fade=t=in:st=0:d=0.5[aus]"
    ffmpeg("-framerate", str(FPS), "-i", muster,
           "-filter_complex", kette, "-map", "[aus]",
           "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "19",
           "-r", str(FPS), ziel)


# ── Tonspur ─────────────────────────────────────────────────────────────────
async def _sprich(text, ziel):
    await edge_tts.Communicate(text, STIMME, rate=TEMPO).save(ziel)


def stimmen(sprache, clip, neu=False):
    ordner = os.path.join(SPRECHER, sprache, clip["ordner"])
    os.makedirs(ordner, exist_ok=True)
    dateien = []
    for shot in clip["shots"]:
        ziel = os.path.join(ordner, f"{shot['datei']}.mp3")
        if neu or not os.path.isfile(ziel):
            # Die Karte muss in fuenf Sekunden lesbar sein, die Stimme darf in
            # derselben Zeit mehr sagen. Wo `sprech_<sprache>` fehlt, spricht
            # sie wie bisher den eingebrannten Text — die aelteren Clips
            # merken von diesem Feld nichts.
            asyncio.run(_sprich(shot.get(f"sprech_{sprache}", shot[sprache]),
                                ziel))
        dateien.append(ziel)
    return dateien


# Zielpegel der einzelnen Spuren, bevor gemischt wird. Sie am Ursprung zu
# setzen ist der ganze Trick: eine Mischung aus roher Sprache und einem mit
# `volume=0.10` heruntergedrehten Musikbett landet bei rund -26 LUFS, und die
# fehlenden 10 dB kann kein Normalisierer mehr holen, ohne die Spitzen zu
# zerdruecken. So bleibt am Schluss nur noch eine kleine Korrektur.
SPRACHE_LUFS = -17.0
MUSIK_LUFS_UNTER_SPRACHE = -15.0      # Bett, das traegt statt mitzuspielen
MUSIK_LUFS_ALLEIN = -18.0


def tonspur(starts, gesamt, arbeit, sprache, clip, mit_stimme):
    eingaben, teile, marken = [], [], []
    if mit_stimme:
        for i, pfad in enumerate(stimmen(sprache, clip)):
            eingaben += ["-i", pfad]
            ms = int(starts[i] * 1000)
            hebung = SPRACHE_LUFS - lautheit(pfad)
            teile.append(f"[{i}:a]volume={hebung:.2f}dB,adelay={ms}|{ms}[s{i}]")
            marken.append(f"[s{i}]")

    musik = os.path.join(LOGOS_DIR, "music_playful.wav")
    if os.path.isfile(musik):
        n = len(marken)
        eingaben += ["-stream_loop", "-1", "-i", musik]
        ziel = (SPRACHE_LUFS + MUSIK_LUFS_UNTER_SPRACHE if mit_stimme
                else MUSIK_LUFS_ALLEIN)
        hebung = ziel - lautheit(musik)
        teile.append(f"[{n}:a]atrim=0:{gesamt:.2f},volume={hebung:.2f}dB,"
                     f"afade=t=out:st={gesamt - 1.5:.2f}:d=1.5[m]")
        marken.append("[m]")
    if not marken:
        return None

    teile.append("".join(marken) + f"amix=inputs={len(marken)}:normalize=0:"
                 f"duration=longest[aus]")
    roh = os.path.join(arbeit, "ton-roh.wav")
    ffmpeg(*eingaben, "-filter_complex", ";".join(teile), "-map", "[aus]",
           "-t", f"{gesamt:.2f}", "-c:a", "pcm_s16le", roh)
    return lautheit_angleichen(roh, os.path.join(arbeit, "ton.m4a"))


def lautheit_angleichen(quelle, ziel):
    """Messen, glatt anheben, Spitzen kappen.

    Bewusst nicht `loudnorm` in zwei Durchgaengen: der Filter haelt die
    True-Peak-Grenze fuer wichtiger als das Lautheitsziel und bleibt dann
    stillschweigend darunter (gemessen: -17,8 statt -16 LUFS). Ein gemessener
    Gain plus Limiter sagt dasselbe geradeheraus — und `level=false` beim
    Limiter ist Pflicht, sonst normalisiert er von sich aus nach oben und
    erzeugt genau die Spitzen, die er kappen soll.
    """
    mess = subprocess.run(
        ["ffmpeg", "-v", "info", "-i", quelle, "-af",
         f"loudnorm=I={LAUTHEIT}:TP=-1.5:LRA=11:print_format=json",
         "-f", "null", "-"], capture_output=True, text=True, check=True)
    text = mess.stderr
    werte = json.loads(text[text.rindex("{"):text.rindex("}") + 1])
    gain = LAUTHEIT - float(werte["input_i"])
    ffmpeg("-i", quelle, "-af",
           f"volume={gain:.2f}dB,alimiter=limit=0.8:level=false:"
           f"attack=5:release=60",
           "-c:a", "aac", "-b:a", "192k", ziel)
    return ziel


# ── Platzhalter ─────────────────────────────────────────────────────────────
def dummys(clip):
    """Rohclips vortaeuschen, damit die Kette ohne Abo pruefbar ist (§0.5).

    Bewusst in verschiedenen Seitenverhaeltnissen: 16:9, 9:16 und 1:1. Genau
    daran zeigt sich, ob Skalierung und Beschnitt taugen — ein Test mit lauter
    4:5-Dateien wuerde nichts beweisen.
    """
    roh = os.path.join(ROH, clip["ordner"])
    os.makedirs(roh, exist_ok=True)
    masse = [("1920x1080", 5.0), ("1080x1920", 4.5), ("1080x1080", 5.5)]
    for shot, (groesse, laenge) in zip(clip["shots"], masse):
        ziel = os.path.join(roh, f"{shot['datei']}.mp4")
        ffmpeg("-f", "lavfi", "-i",
               f"testsrc2=size={groesse}:rate={FPS}:duration={laenge}",
               "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "23", ziel)
        print(f"   {os.path.basename(ziel)}  ({groesse}, {laenge} s)")


# ── Zusammenbau ─────────────────────────────────────────────────────────────
def bauen(sprache, clip_id, clip, mit_stimme=True):
    roh = os.path.join(ROH, clip["ordner"])
    shots = clip["shots"]
    fehlend = [s["datei"] for s in shots
               if not os.path.isfile(os.path.join(roh, f"{s['datei']}.mp4"))]
    if fehlend:
        print(f"Fehlende Rohclips in {roh}: {', '.join(fehlend)}\n"
              f"Higgsfield-Clips dort ablegen oder --dummy für einen Probelauf.",
              file=sys.stderr)
        return None

    os.makedirs(FERTIG, exist_ok=True)
    arbeit = tempfile.mkdtemp(prefix="montage-")
    try:
        teile, starts, uhr = [], [], 0.0
        for i, shot in enumerate(shots):
            quelle = os.path.join(roh, f"{shot['datei']}.mp4")
            roh_laenge = dauer(quelle)
            laenge = min(roh_laenge, clip.get("max_shot", MAX_SHOT_S))
            png = os.path.join(arbeit, f"text{i}.png")
            textebene(shot[sprache], png)
            ziel = os.path.join(arbeit, f"seg{i}.mp4")
            segment(quelle, png, roh_laenge - laenge, laenge, ziel)
            teile.append(ziel)
            starts.append(uhr + 0.3)
            uhr += laenge
            print(f"   {shot['datei']}  {laenge:.1f} s")

        ziel = os.path.join(arbeit, "seg_abspann.mp4")
        if "held" in clip:
            abspannbilder(sprache, clip, arbeit)
            abspannsegment_bewegt(os.path.join(arbeit, "ab%04d.png"), ziel)
        else:
            bild = os.path.join(arbeit, "abspann.png")
            abspannbild(sprache, bild, clip)
            abspannsegment(bild, ziel)
        teile.append(ziel)
        gesamt = uhr + ABSPANN_S

        liste = os.path.join(arbeit, "liste.txt")
        with open(liste, "w", encoding="utf-8") as f:
            for t in teile:
                f.write(f"file '{t.replace(chr(92), '/')}'\n")
        stumm = os.path.join(arbeit, "stumm.mp4")
        ffmpeg("-f", "concat", "-safe", "0", "-i", liste, "-c", "copy", stumm)

        # Sprache, die laenger ist als ihr Bild, laeuft in den naechsten Shot —
        # lieber melden als still verschieben.
        if mit_stimme:
            for i, (shot, start, pfad) in enumerate(
                    zip(shots, starts, stimmen(sprache, clip))):
                ende = start + dauer(pfad)
                grenze = starts[i + 1] if i + 1 < len(shots) else gesamt
                if ende > grenze + 0.2:
                    einzeilig = " ".join(shot[sprache].split())
                    print(f"   Hinweis: „{einzeilig}“ ist {ende - grenze:.1f} s "
                          f"länger als sein Bild.")

        ton = tonspur(starts, gesamt, arbeit, sprache, clip, mit_stimme)
        endziel = os.path.join(FERTIG, f"{clip_id}-{sprache}-4x5.mp4")
        if ton:
            ffmpeg("-i", stumm, "-i", ton, "-c:v", "copy", "-c:a", "copy",
                   "-shortest", endziel)
        else:
            shutil.copyfile(stumm, endziel)
    finally:
        shutil.rmtree(arbeit, ignore_errors=True)

    print(f"OK  {endziel}  ({gesamt:.1f} s)")
    return endziel


def main(argv=None):
    p = argparse.ArgumentParser(description="Higgsfield-Rohclips zum Post montieren")
    p.add_argument("--clip", default="01-eyecatcher", choices=sorted(CLIPS),
                   help="welcher Clip aus prompts.md")
    p.add_argument("--sprache", default="de", choices=["de", "en"])
    p.add_argument("--beide", action="store_true")
    p.add_argument("--ohne-stimme", action="store_true")
    p.add_argument("--dummy", action="store_true",
                   help="Platzhalter-Rohclips erzeugen (Probelauf ohne Abo)")
    args = p.parse_args(argv)

    clip = CLIPS[args.clip]
    if args.dummy:
        dummys(clip)

    for sprache in (["de", "en"] if args.beide else [args.sprache]):
        print(f"{sprache}:")
        if bauen(sprache, args.clip, clip,
                 mit_stimme=not args.ohne_stimme) is None:
            return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
