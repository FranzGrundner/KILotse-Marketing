"""clip.py — der Poolservice-Clip (Betriebsart-Clip #1) komplett lokal bauen.

Gebaut wie das Werbevideo #160 (`../video.py`): Bild mit PIL gezeichnet, Ton aus
edge-tts, zusammengesetzt mit ffmpeg. Der Unterschied: hier stehen **echte
Screenshots** des laufenden Beispielbetriebs im Bild statt gezeichneter Symbolik
— bei einem Clip, der einem konkreten Poolservice geschickt wird, ist der Beweis
die Ware. Gezeichnet wird nur der Rahmen darum.

Warum Hochformat: der Clip geht auf LINE/WhatsApp und in den FB-Feed, beides
Handy. 4:5 fuellt die Spalte, 16:9 verschwindet darin.

Marken-Tokens, Schrift und Zeichenhelfer kommen aus `video.py` — eine Quelle
fuer den Look, damit der zweite Clip nicht anders aussieht als der erste.

Aufruf:
    python -X utf8 clip.py                 Sprecherspur (falls noetig) + Video
    python -X utf8 clip.py --szene 2       nur Szene 2 als Kontaktbogen pruefen
    python -X utf8 clip.py --ohne-musik
"""
import argparse
import asyncio
import os
import shutil
import subprocess
import sys
import tempfile

from PIL import Image, ImageDraw

BASIS = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(BASIS))           # ../video.py

import edge_tts                                       # noqa: E402
from video import (AKZENT, AKZENT_BG, AKZENT_HELL, ASSETS_DIR, BG, FLAECHE,   # noqa: E402
                   GEDAEMPFT, LOGOS_DIR, RAND, TEXT, WEISS, auftritt, dauer,
                   mischen, schrift, text_bei, weich)

SHOTS = os.path.join(BASIS, "shots")
SPRECHER = os.path.join(BASIS, "sprecher")
ZIEL = os.path.join(BASIS, "poolservice-clip-de.mp4")

STIMME = "de-DE-FlorianMultilingualNeural"           # Franz' Wahl (27.07.2026)
# #160 lief mit -8%; hier -4%: der Clip soll unter 22 s bleiben (§6 des
# Higgsfield-Plans), und die Saetze sind kuerzer als dort.
TEMPO = "-4%"

BREITE, HOEHE = 1080, 1350                            # 4:5, Feed und Messenger
FPS = 30
SUPER = 2                                             # zeichnen in 2x, dann verkleinern

VORLAUF = 0.4
PAUSE = 0.4
NACHLAUF = 1.2

# ── Sprechtext ──────────────────────────────────────────────────────────────
# Reihenfolge = Szenenreihenfolge. Die Domain steht fuers Ohr geschrieben
# ("punkt tech"): als "ki-lotse.tech" verschliff die Stimme das Satzende (#160).
SAETZE = [
    ("01-streit",
     "Der Kunde sagt, ihr wart nicht da. Deine Leute sagen: doch."),
    ("02-nachweis",
     "Datum, Servicekraft, Foto — steht alles am Einsatz."),
    ("03-rhythmus",
     "Jeder Vertrag hat seinen Rhythmus, die Einsätze entstehen von selbst."),
    ("04-rechnung",
     "Am Monatsende wird daraus die Rechnung."),
    ("05-cta",
     "Schau es dir an — ki-lotse punkt tech."),
]


# ── Zeichenhelfer, die es in video.py noch nicht gibt ───────────────────────
def umbrechen(d, inhalt, font, maxbreite):
    """Text auf mehrere Zeilen brechen — PIL bricht von selbst nicht um."""
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


def block(d, xy, inhalt, font, farbe, maxbreite, zeilenhoehe, anker="la",
          deckung=1.0):
    x, y = xy
    for i, zeile in enumerate(umbrechen(d, inhalt, font, maxbreite)):
        text_bei(d, (x, y + i * zeilenhoehe), zeile, font, farbe, anker=anker,
                 deckung=deckung)
    return y + len(umbrechen(d, inhalt, font, maxbreite)) * zeilenhoehe


_CACHE = {}


def ausschnitt_bild(name, rel, zielbreite):
    """Beschnittener, skalierter Screenshot — einmal je (Bild, Ausschnitt, Breite).

    `rel` ist (links, oben, rechts, unten) in Anteilen 0…1. Beschneiden ist
    erlaubt, Zusammensetzen nicht: was im Bild steht, steht so auch in der Demo.
    """
    schluessel = (name, rel, zielbreite)
    if schluessel not in _CACHE:
        quelle = Image.open(os.path.join(SHOTS, f"{name}.png")).convert("RGB")
        b, h = quelle.size
        teil = quelle.crop((int(rel[0] * b), int(rel[1] * h),
                            int(rel[2] * b), int(rel[3] * h)))
        faktor = zielbreite / teil.width
        _CACHE[schluessel] = teil.resize(
            (zielbreite, max(1, int(teil.height * faktor))), Image.LANCZOS)
    return _CACHE[schluessel]


def karte(blatt, d, name, rel, xy, zielbreite, deckung=1.0, radius=16,
          rand=RAND, hebung=0):
    """Screenshot-Ausschnitt als Karte mit Rahmen und runden Ecken."""
    if deckung <= 0.01:
        return 0
    bild = ausschnitt_bild(name, rel, zielbreite)
    x, y = int(xy[0]), int(xy[1] + hebung * (1 - deckung))
    maske = Image.new("L", bild.size, 0)
    ImageDraw.Draw(maske).rounded_rectangle((0, 0, bild.width - 1, bild.height - 1),
                                            radius=radius, fill=255)
    if deckung < 1.0:
        maske = maske.point(lambda a: int(a * deckung))
    blatt.paste(bild, (x, y), maske)
    d.rounded_rectangle((x, y, x + bild.width - 1, y + bild.height - 1),
                        radius=radius, outline=mischen(BG, rand, deckung), width=3)
    return bild.height


def sprechblase(d, kasten, farbe_fuell, farbe_rand, spitze_links=True, deckung=1.0):
    x0, y0, x1, y1 = kasten
    d.rounded_rectangle(kasten, radius=int((y1 - y0) * 0.22),
                        fill=mischen(BG, farbe_fuell, deckung),
                        outline=mischen(BG, farbe_rand, deckung), width=3)
    # Spitze unten, damit die Kachel als Zitat und nicht als Knopf gelesen wird.
    sx = x0 + (y1 - y0) * 0.35 if spitze_links else x1 - (y1 - y0) * 0.35
    r = (y1 - y0) * 0.16
    d.polygon([(sx - r, y1 - 2), (sx + r, y1 - 2), (sx + (r if not spitze_links else -r),
               y1 + r * 1.4)], fill=mischen(BG, farbe_fuell, deckung))


def marke(d, s, deckung=1.0):
    """Dezente Fusszeile — der Clip wird weitergeleitet, die Quelle muss mit."""
    text_bei(d, (s(BREITE) // 2, s(1268)), "KI-Lotse · Pattaya",
             schrift(s(28), leicht=True), GEDAEMPFT, anker="mm", deckung=deckung * 0.9)
    text_bei(d, (s(BREITE) // 2, s(1310)), "poolservice.demo.ki-lotse.tech",
             schrift(s(30), fett=True), AKZENT, anker="mm", deckung=deckung * 0.9)


def kopf(d, s, titel, unter, t, maxbreite=920):
    """Titel (umbrechend) und Unterzeile. Gibt die Grundlinie darunter zurueck —
    die Bildkarten haengen sich daran, statt auf geratene Werte."""
    f_titel = schrift(s(60), fett=True)
    zeilen = umbrechen(d, titel, f_titel, s(maxbreite))
    for i, zeile in enumerate(zeilen):
        text_bei(d, (s(72), s(112) + i * s(74)), zeile, f_titel, TEXT,
                 deckung=auftritt(t, 0.05))
    y = s(112) + len(zeilen) * s(74) + s(14)
    if unter:
        f_unter = schrift(s(36), leicht=True)
        for i, zeile in enumerate(umbrechen(d, unter, f_unter, s(maxbreite))):
            text_bei(d, (s(72), y + i * s(48)), zeile, f_unter, GEDAEMPFT,
                     deckung=auftritt(t, 0.3))
            y_ende = y + (i + 1) * s(48)
        return y_ende + s(28)
    return y + s(20)


def haken(d, mitte, groesse, farbe, breite, deckung=1.0):
    """Haekchen zeichnen — Segoe UI hat kein U+2713, das gaebe ein Tofu-Kaestchen."""
    if deckung <= 0.01:
        return
    x, y = mitte
    d.line([(x - groesse, y), (x - groesse * 0.25, y + groesse * 0.7),
            (x + groesse, y - groesse * 0.75)],
           fill=mischen(BG, farbe, deckung), width=breite, joint="curve")


# ── Szenen ──────────────────────────────────────────────────────────────────
def szene_streit(blatt, d, t, laenge, s):
    """Der Streitfall — zwei Aussagen, kein Beweis. Ohne Screenshots."""
    text_bei(d, (s(72), s(150)), "Wart ihr da?", schrift(s(76), fett=True), TEXT,
             deckung=auftritt(t, 0.05))

    a1 = auftritt(t, 0.5)
    if a1 > 0.01:
        sprechblase(d, (s(72), s(330), s(830), s(520)), FLAECHE, RAND,
                    spitze_links=True, deckung=a1)
        block(d, (s(120), s(378)), "„Ihr wart letzte Woche nicht da.“",
              schrift(s(42)), TEXT, s(660), s(52), deckung=a1)
        text_bei(d, (s(120), s(560)), "der Kunde", schrift(s(30), leicht=True),
                 GEDAEMPFT, deckung=a1 * 0.9)

    a2 = auftritt(t, 1.5)
    if a2 > 0.01:
        sprechblase(d, (s(250), s(670), s(1008), s(860)), AKZENT_BG, AKZENT_HELL,
                    spitze_links=False, deckung=a2)
        block(d, (s(298), s(718)), "„Doch. Waren wir.“",
              schrift(s(42)), TEXT, s(660), s(52), deckung=a2)
        text_bei(d, (s(960), s(900)), "deine Leute", schrift(s(30), leicht=True),
                 GEDAEMPFT, anker="ra", deckung=a2 * 0.9)

    a3 = auftritt(t, max(1.0, laenge - 1.5), 0.6)
    if a3 > 0.01:
        text_bei(d, (s(72), s(1010)), "Beweisen kann es keiner.",
                 schrift(s(52), fett=True), AKZENT, deckung=a3)
        text_bei(d, (s(72), s(1085)), "Am Monatsende schreibst du die Rechnung kleiner.",
                 schrift(s(34), leicht=True), GEDAEMPFT, deckung=auftritt(t, laenge - 1.0, 0.5))
    marke(d, s, auftritt(t, 0.8))


def szene_nachweis(blatt, d, t, laenge, s):
    """Der Beweis steht am Einsatz — zwei echte Ausschnitte derselben Seite.

    Bewusst eng beschnitten: eine ganze Bildschirmseite waere im Hochformat
    unlesbar. Zwei Ausschnitte nebeneinanderzumontieren waere eine erfundene
    Ansicht — sie stehen deshalb als getrennte Karten untereinander.

    Die zweite Karte ist seit `wartung` v1.1.0 (Demo-Seed bringt Foto und
    Unterschrift mit) der Kern des Clips: der Prospekt verkauft genau diesen
    Satz, und hier steht er als echter Screenshot dahinter. Vorher waren dort
    nur leere Upload-Felder und die Karte zeigte die Checkliste.
    """
    y = kopf(d, s, "Am Einsatz steht, was war.",
             "Kein Erinnern, kein Streiten.", t)

    # Ausschnitt 1: Datum, Servicekraft, Notiz und die abgehakte Checkliste.
    a1 = auftritt(t, 0.5)
    h = karte(blatt, d, "nachweis", (0.015, 0.179, 0.42, 0.443), (s(72), y),
              s(690), deckung=a1, hebung=s(30))

    # Ausschnitt 2: das Foto und die quittierte Unterschrift.
    a2 = auftritt(t, 1.5)
    karte(blatt, d, "nachweis", (0.015, 0.452, 0.634, 0.786),
          (s(72), y + h + s(36)), s(830), deckung=a2, hebung=s(30),
          rand=AKZENT_HELL)

    a3 = auftritt(t, laenge - 1.4, 0.5)
    if a3 > 0.01:
        haken(d, (s(96), s(1178)), s(20), AKZENT, s(7), a3)
        text_bei(d, (s(134), s(1156)), "Foto und Unterschrift hängen dran.",
                 schrift(s(40), fett=True), AKZENT, deckung=a3)
    marke(d, s, auftritt(t, 0.4))


def szene_rhythmus(blatt, d, t, laenge, s):
    """Vertrag hat Rhythmus, Einsaetze entstehen daraus."""
    # Die Aussage steht hier oben und nicht unten wie in den anderen Szenen:
    # die vergroesserte Rhythmus-Spalte braucht die untere Bildhaelfte ganz.
    y = kopf(d, s, "Verträge laufen im Rhythmus.",
             "Die Einsätze entstehen daraus von selbst.", t)

    a1 = auftritt(t, 0.5)
    h = karte(blatt, d, "vertraege", (0.015, 0.33, 0.70, 1.0), (s(40), y),
              s(1000), deckung=a1, hebung=s(30))

    # Lupe auf die Rhythmus-Spalte: in der ganzen Tabelle ist genau die Angabe,
    # auf die es ankommt, am Handy zu klein.
    # Spaltengrenze exakt treffen: bei 0.44 stand ein angeschnittenes
    # "lservice" im Bild und sah nach Fehler aus.
    a2 = auftritt(t, 1.5)
    karte(blatt, d, "vertraege", (0.527, 0.33, 0.70, 1.0),
          (s(320), y + h + s(30)), s(440), deckung=a2, hebung=s(30),
          rand=AKZENT_HELL)
    marke(d, s, auftritt(t, 0.4))


def szene_rechnung(blatt, d, t, laenge, s):
    """Aus erledigten Leistungen wird der Beleg."""
    y = kopf(d, s, "Am Monatsende wird daraus die Rechnung.",
             "Erledigte Leistungen werden zur Positionsliste.", t)

    # Ausschnitt ab der Spalte Datum: Nummer und Empfaenger sind fuer die
    # Aussage entbehrlich, und ohne sie ist die Schrift fast doppelt so gross.
    a1 = auftritt(t, 0.5)
    karte(blatt, d, "rechnungen", (0.455, 0.16, 0.99, 0.80), (s(40), y + s(30)),
          s(1000), deckung=a1, hebung=s(30))

    a3 = auftritt(t, laenge - 1.3, 0.5)
    if a3 > 0.01:
        haken(d, (s(96), s(1158)), s(20), AKZENT, s(7), a3)
        text_bei(d, (s(134), s(1136)), "Offen, bezahlt, überfällig.",
                 schrift(s(40), fett=True), AKZENT, deckung=a3)
    marke(d, s, auftritt(t, 0.4))


def szene_abspann(blatt, d, t, laenge, s):
    """Markenflaeche mit der Adresse, die im Clip gezeigt wurde."""
    a_bg = auftritt(t, 0.0, 0.5)
    d.rectangle((0, 0, s(BREITE), s(HOEHE)), fill=mischen(BG, AKZENT, a_bg))

    def hell(deckung):
        return mischen(mischen(BG, AKZENT, a_bg), WEISS, deckung)

    from video import bild_einsetzen
    bild_einsetzen(blatt, os.path.join(ASSETS_DIR, "logo-icon-weiss.png"),
                   (s(390), s(430)), s(210), auftritt(t, 0.35))
    bild_einsetzen(blatt, os.path.join(ASSETS_DIR, "avatar-franz-rund-512.png"),
                   (s(700), s(430)), s(250), auftritt(t, 0.55))

    text_bei(d, (s(BREITE) // 2, s(680)), "Pool · Garten · Reinigung",
             schrift(s(44), leicht=True), hell(auftritt(t, 0.8) * 0.9), anker="mm")
    text_bei(d, (s(BREITE) // 2, s(790)), "Schau es dir an:",
             schrift(s(40), leicht=True), hell(auftritt(t, 1.0) * 0.9), anker="mm")
    # Eine Zeile: umgebrochen stand der Punkt am Zeilenanfang und die Adresse
    # las sich wie zwei verschiedene.
    text_bei(d, (s(BREITE) // 2, s(900)), "poolservice.demo.ki-lotse.tech",
             schrift(s(48), fett=True), hell(auftritt(t, 1.1)), anker="mm")
    text_bei(d, (s(BREITE) // 2, s(1120)), "Franz Grundner · KI-Lotse · Pattaya",
             schrift(s(36), leicht=True), hell(auftritt(t, 1.4) * 0.85), anker="mm")


SZENEN = [szene_streit, szene_nachweis, szene_rhythmus, szene_rechnung,
          szene_abspann]


# ── Ton ─────────────────────────────────────────────────────────────────────
async def _sprich(text, stimme, ziel):
    await edge_tts.Communicate(text, stimme, rate=TEMPO).save(ziel)


def sprecherspur(stimme, neu=False):
    """Fehlende Saetze synthetisieren (edge-tts, braucht Internet)."""
    ordner = os.path.join(SPRECHER, stimme)
    os.makedirs(ordner, exist_ok=True)
    for name, text in SAETZE:
        ziel = os.path.join(ordner, f"{name}.mp3")
        if neu or not os.path.isfile(ziel):
            asyncio.run(_sprich(text, stimme, ziel))
            print(f"   {name}.mp3")
    return ordner


def takt(ordner):
    """Startzeiten und Szenenfenster aus den echten Audiolaengen (ffprobe)."""
    laengen = [dauer(os.path.join(ordner, f"{n}.mp3")) for n, _ in SAETZE]
    starts, fenster, uhr = [], [], VORLAUF
    for i, l in enumerate(laengen):
        starts.append(uhr)
        beginn = 0.0 if i == 0 else fenster[-1][1]
        uhr += l + PAUSE
        fenster.append((beginn, uhr))
    gesamt = uhr - PAUSE + NACHLAUF
    fenster[-1] = (fenster[-1][0], gesamt)
    return starts, fenster, gesamt


def tonspur(ordner, starts, gesamt, arbeit, mit_musik=True):
    eingaben, filter_teile, marken = [], [], []
    for i, (name, _) in enumerate(SAETZE):
        eingaben += ["-i", os.path.join(ordner, f"{name}.mp3")]
        ms = int(starts[i] * 1000)
        filter_teile.append(f"[{i}:a]adelay={ms}|{ms}[s{i}]")
        marken.append(f"[s{i}]")

    musik = os.path.join(LOGOS_DIR, "music_playful.wav")
    if mit_musik and os.path.isfile(musik):
        eingaben += ["-stream_loop", "-1", "-i", musik]
        filter_teile.append(
            f"[{len(SAETZE)}:a]volume=0.08,atrim=0:{gesamt:.2f},"
            f"afade=t=out:st={gesamt - 1.5:.2f}:d=1.5[m]")
        marken.append("[m]")

    # Lautheit auf Rundfunkmass ziehen: die Rohmischung lag bei -21 LUFS. Facebook
    # hebt so etwas selbst an, LINE und WhatsApp nicht — dort kam der Clip leise an.
    filter_teile.append("".join(marken) +
                        f"amix=inputs={len(marken)}:normalize=0:duration=longest"
                        f"[gemischt]")
    filter_teile.append("[gemischt]loudnorm=I=-16:TP=-1.5:LRA=11[aus]")
    ziel = os.path.join(arbeit, "ton.m4a")
    subprocess.run(["ffmpeg", "-y", "-v", "error", *eingaben,
                    "-filter_complex", ";".join(filter_teile),
                    "-map", "[aus]", "-t", f"{gesamt:.2f}",
                    "-c:a", "aac", "-b:a", "192k", ziel], check=True)
    return ziel


# ── Zusammenbau ─────────────────────────────────────────────────────────────
def zeichne(zeit, fenster, s):
    blatt = Image.new("RGB", (s(BREITE), s(HOEHE)), BG)
    d = ImageDraw.Draw(blatt)
    for szene, (beginn, ende) in zip(SZENEN, fenster):
        if beginn <= zeit < ende:
            szene(blatt, d, zeit - beginn, ende - beginn, s)
            break
    else:
        beginn, ende = fenster[-1]
        SZENEN[-1](blatt, d, ende - beginn, ende - beginn, s)
    return blatt


def main(argv=None):
    p = argparse.ArgumentParser(description="Poolservice-Clip bauen")
    p.add_argument("--stimme", default=STIMME)
    p.add_argument("--szene", type=int, choices=range(1, len(SZENEN) + 1))
    p.add_argument("--ohne-musik", action="store_true")
    p.add_argument("--neue-stimme", action="store_true",
                   help="Sprachdateien neu synthetisieren (nach Textaenderung)")
    p.add_argument("--ziel", default=ZIEL)
    args = p.parse_args(argv)

    ordner = sprecherspur(args.stimme, neu=args.neue_stimme)
    starts, fenster, gesamt = takt(ordner)
    s = lambda v: int(v * SUPER)                      # noqa: E731

    if args.szene:
        beginn, ende = fenster[args.szene - 1]
        laenge = ende - beginn
        bogen = Image.new("RGB", (s(BREITE) * 3, s(HOEHE)), BG)
        for i, anteil in enumerate((0.35, 0.7, 0.98)):
            bogen.paste(zeichne(beginn + laenge * anteil, fenster, s),
                        (i * s(BREITE), 0))
        ziel = os.path.join(BASIS, f"szene{args.szene}-kontaktbogen.png")
        bogen.resize((BREITE * 3 // 2, HOEHE // 2), Image.LANCZOS).save(ziel)
        print(f"OK  {ziel}  ({laenge:.1f} s)")
        return 0

    bilder = int(gesamt * FPS)
    arbeit = tempfile.mkdtemp(prefix="poolservice-clip-")
    try:
        print(f"{bilder} Bilder ({gesamt:.1f} s) …")
        for n in range(bilder):
            zeichne(n / FPS, fenster, s).resize((BREITE, HOEHE), Image.LANCZOS).save(
                os.path.join(arbeit, f"{n:05d}.png"))
            if n % 120 == 0:
                print(f"   {n}/{bilder}")
        ton = tonspur(ordner, starts, gesamt, arbeit, mit_musik=not args.ohne_musik)
        subprocess.run(
            ["ffmpeg", "-y", "-v", "error",
             "-framerate", str(FPS), "-i", os.path.join(arbeit, "%05d.png"),
             "-i", ton, "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "19",
             "-c:a", "copy", "-shortest", args.ziel], check=True)
    finally:
        shutil.rmtree(arbeit, ignore_errors=True)

    print(f"OK  {args.ziel}  ({gesamt:.1f} s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
