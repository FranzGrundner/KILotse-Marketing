"""video.py — das Werbevideo (#160) komplett lokal bauen.

Franz geht nicht vor die Kamera. Bild und Ton entstehen darum am Rechner:
die Sprecherspur kommt aus `sprecher.py` (edge-tts), die Bildspur wird hier
Bild fuer Bild mit PIL gezeichnet und mit ffmpeg zusammengesetzt.

Warum selbst zeichnen statt ein Videomodell: auf dieser Maschine laeuft
Stable Diffusion nur auf der CPU (~65 s pro Bild) — 30 Sekunden Video waeren
rund 13 Stunden, und die Bilder wuerden von Frame zu Frame flackern. Gezeichnet
sind es zwei Minuten, und jedes Pixel sitzt da, wo es soll. Dieselbe Lehre wie
beim Intro-Video, wo Firefly ungefragt hineingezoomt hat.

Der Takt kommt aus den echten Laengen der Sprach-Dateien (ffprobe), nicht aus
geschaetzten Sekunden — sonst laeuft Bild gegen Ton.

Aufruf:
    python -X utf8 video.py                    ganzes Video
    python -X utf8 video.py --stimme de-AT-JonasNeural
    python -X utf8 video.py --szene 3          nur Szene 3 als Standbild pruefen
    python -X utf8 video.py --ohne-musik
"""
import argparse
import json
import math
import os
import shutil
import subprocess
import sys
import tempfile

from PIL import Image, ImageDraw, ImageFont

BASIS_DIR = os.path.dirname(os.path.abspath(__file__))
SPRECHER_DIR = os.path.join(BASIS_DIR, "sprecher")
LOGOS_DIR = r"C:\Claude\Franz\Logos"
ASSETS_DIR = r"C:\Claude\Franz\_design\assets"

STIMME = "de-DE-FlorianMultilingualNeural"      # Franz' Wahl (27.07.2026)
ZIEL = os.path.join(BASIS_DIR, "ki-lotse-werbung.mp4")

BREITE, HOEHE = 1920, 1080
FPS = 30
SUPER = 2                     # Ueberabtastung: zeichnen in 2x, dann verkleinern
                              # — PIL kann keine Kantenglaettung, Verkleinern schon.

# ── Marken-Tokens (Franz\_design\tokens.css, helles Thema) ──────────────────
BG = (0xF6, 0xF7, 0xF9)
FLAECHE = (0xFF, 0xFF, 0xFF)
TEXT = (0x1F, 0x24, 0x30)
GEDAEMPFT = (0x5B, 0x64, 0x72)
RAND = (0xDF, 0xE3, 0xE8)
AKZENT = (0x0F, 0x6E, 0x56)
AKZENT_HELL = (0x1D, 0x9E, 0x75)
AKZENT_BG = (0xE7, 0xF6, 0xF0)
WEISS = (0xFF, 0xFF, 0xFF)

# ── Takt ────────────────────────────────────────────────────────────────────
VORLAUF = 0.5                 # Stille vor dem ersten Satz
PAUSE = 0.7                   # zwischen den Saetzen
NACHLAUF = 1.2                # Standbild am Ende, damit der CTA stehen bleibt

SEGMENTE = ["01-problem", "02-loesung", "03-nutzen", "04-abschluss"]


# ── Werkzeug ────────────────────────────────────────────────────────────────
def dauer(pfad):
    """Laenge einer Audiodatei in Sekunden (ffprobe)."""
    aus = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration",
         "-of", "json", pfad], capture_output=True, text=True, check=True)
    return float(json.loads(aus.stdout)["format"]["duration"])


def schrift(groesse, fett=False, leicht=False):
    name = "segoeuib.ttf" if fett else ("segoeuisl.ttf" if leicht else "segoeui.ttf")
    try:
        return ImageFont.truetype(name, groesse)
    except OSError:
        return ImageFont.load_default()


def weich(t):
    """Smoothstep 0…1 — Bewegung ohne harten Anfang und harten Halt."""
    t = max(0.0, min(1.0, t))
    return t * t * (3 - 2 * t)


def auftritt(t, start, laenge=0.45):
    """Einblend-Anteil eines Elements, das bei `start` beginnt."""
    return weich((t - start) / laenge) if laenge > 0 else float(t >= start)


def mischen(a, b, anteil):
    return tuple(int(x + (y - x) * anteil) for x, y in zip(a, b))


def text_bei(d, xy, inhalt, font, farbe, anker="la", deckung=1.0):
    """Text mit Deckung — PIL kennt kein Alpha im Draw, also zur Flaeche mischen."""
    if deckung <= 0.01:
        return
    if deckung < 1.0:
        farbe = mischen(BG, farbe, deckung)
    d.text(xy, inhalt, font=font, fill=farbe, anchor=anker)


def kachel(d, kasten, fuell=FLAECHE, rand=RAND, radius=18, breite=2):
    d.rounded_rectangle(kasten, radius=radius, fill=fuell, outline=rand, width=breite)


def pfeil(d, von, bis, farbe, breite=5, kopf=18):
    d.line([von, bis], fill=farbe, width=breite)
    winkel = math.atan2(bis[1] - von[1], bis[0] - von[0])
    for seite in (+1, -1):
        w = winkel + math.pi + seite * 0.42
        d.line([bis, (bis[0] + math.cos(w) * kopf, bis[1] + math.sin(w) * kopf)],
               fill=farbe, width=breite)


def bild_einsetzen(blatt, pfad, mitte, hoehe, deckung=1.0):
    """Fertiges Asset (Logo, Avatar) mittig platzieren."""
    if deckung <= 0.01 or not os.path.isfile(pfad):
        return
    quelle = Image.open(pfad)
    faktor = hoehe / quelle.height
    quelle = quelle.resize((int(quelle.width * faktor), hoehe), Image.LANCZOS)
    x, y = int(mitte[0] - quelle.width / 2), int(mitte[1] - quelle.height / 2)
    if quelle.mode == "RGBA":
        alpha = quelle.getchannel("A")
        if deckung < 1.0:
            alpha = alpha.point(lambda a: int(a * deckung))
        blatt.paste(quelle.convert("RGB"), (x, y), alpha)
    else:
        if deckung < 1.0:
            hinter = blatt.crop((x, y, x + quelle.width, y + quelle.height))
            quelle = Image.blend(hinter, quelle.convert("RGB"), deckung)
        blatt.paste(quelle.convert("RGB"), (x, y))


# ── Szenen ──────────────────────────────────────────────────────────────────
# Jede Szene bekommt die verstrichene Zeit SEIT ihrem Beginn und ihre Laenge.

KANAELE = ["Facebook", "LINE", "WhatsApp", "E-Mail"]


def szene_problem(blatt, d, t, laenge, s):
    """Anfragen aus vier Kanaelen, alles per Hand in eine Tabelle."""
    text_bei(d, (s(160), s(150)), "Anfragen von überall", schrift(s(78), fett=True),
             TEXT, deckung=auftritt(t, 0.1))
    text_bei(d, (s(160), s(258)), "und alles per Hand in die Tabelle",
             schrift(s(44), leicht=True), GEDAEMPFT, deckung=auftritt(t, 0.35))

    # Kanal-Kacheln links, versetzt eingeblendet
    tabelle_mitte = (s(1420), s(660))
    for i, name in enumerate(KANAELE):
        a = auftritt(t, 0.7 + i * 0.28)
        if a <= 0.01:
            continue
        y = s(430 + i * 118)
        x = s(200) + int(s(40) * (1 - a))         # leicht von links hereinrutschen
        kasten = (x, y, x + s(400), y + s(88))
        kachel(d, kasten, fuell=mischen(BG, FLAECHE, a), rand=mischen(BG, RAND, a))
        text_bei(d, (x + s(36), y + s(44)), name, schrift(s(40)), TEXT,
                 anker="lm", deckung=a)
        # Pfeil zur Tabelle. Jeder Pfeil endet auf eigener Hoehe am linken
        # Tabellenrand — liefen sie in EINEN Punkt, waere daraus ein Knoten.
        p = auftritt(t, 1.0 + i * 0.28, 0.4)
        if p > 0.02:
            start = (x + s(410), y + s(44))
            ziel_x = tabelle_mitte[0] - s(300)
            ziel_y = tabelle_mitte[1] - s(150) + i * s(100)
            pfeil(d, start,
                  (start[0] + (ziel_x - start[0]) * p,
                   start[1] + (ziel_y - start[1]) * p),
                  mischen(BG, AKZENT_HELL, p), breite=s(4), kopf=s(16))

    # Tabelle als Raster, mit angedeuteten Eintraegen — ein leeres Gitter
    # erzaehlt nichts, es soll nach Handarbeit aussehen.
    a_tab = auftritt(t, 1.4)
    if a_tab > 0.01:
        bx, by = tabelle_mitte[0] - s(280), tabelle_mitte[1] - s(220)
        kachel(d, (bx, by, bx + s(560), by + s(440)),
               fuell=mischen(BG, FLAECHE, a_tab), rand=mischen(BG, RAND, a_tab))
        for r in range(1, 7):
            d.line([(bx, by + r * s(63)), (bx + s(560), by + r * s(63))],
                   fill=mischen(BG, RAND, a_tab), width=s(2))
        for c in range(1, 4):
            d.line([(bx + c * s(140), by), (bx + c * s(140), by + s(440))],
                   fill=mischen(BG, RAND, a_tab), width=s(2))
        for r, c, w in ((0, 0, 96), (0, 1, 74), (1, 0, 84), (1, 2, 60),
                        (2, 0, 100), (3, 1, 88), (3, 3, 52), (4, 0, 78)):
            zeile = auftritt(t, 1.7 + r * 0.12, 0.3)
            if zeile > 0.02:
                zx = bx + c * s(140) + s(20)
                zy = by + r * s(63) + s(28)
                d.rounded_rectangle((zx, zy, zx + s(w), zy + s(12)), radius=s(6),
                                    fill=mischen(FLAECHE, (0xC9, 0xD1, 0xD9), zeile))

    # Der Preis dafuer — Position aus der gemessenen Textbreite, nicht geraten.
    a_zeit = auftritt(t, laenge - 1.9, 0.6)
    if a_zeit > 0.01:
        f_gross, f_klein = schrift(s(96), fett=True), schrift(s(46), leicht=True)
        # Grundlinie unter der letzten Kanal-Kachel (die endet bei y=872).
        zx, zy = s(200), s(1000)
        text_bei(d, (zx, zy), "8 Stunden", f_gross, AKZENT, anker="ls",
                 deckung=a_zeit)
        text_bei(d, (zx + d.textlength("8 Stunden", font=f_gross) + s(28), zy),
                 "jede Woche", f_klein, GEDAEMPFT, anker="ls", deckung=a_zeit)


SCHRITTE = ["Anfrage", "KI liest", "Daten", "Antwortentwurf"]


def szene_loesung(blatt, d, t, laenge, s):
    """Der Ablauf als Kette — ein Punkt laeuft hindurch."""
    text_bei(d, (s(160), s(150)), "Anfrage rein, Daten raus",
             schrift(s(78), fett=True), TEXT, deckung=auftritt(t, 0.1))

    y = s(520)
    # Die Linie laeuft UNTER den Kacheln, nicht durch sie: auf Kachelhoehe
    # rannte der Laufpunkt mitten durch die Beschriftung.
    y_linie = y + s(150)
    breite_k, luecke = s(380), s(66)
    spanne = len(SCHRITTE) * breite_k + (len(SCHRITTE) - 1) * luecke
    x0 = (s(BREITE) - spanne) // 2

    a_linie = auftritt(t, 0.5, 0.8)
    if a_linie > 0.01:
        d.line([(x0, y_linie), (x0 + int(spanne * a_linie), y_linie)],
               fill=AKZENT_BG, width=s(10))

    fortschritt = weich((t - 0.8) / max(0.1, laenge - 1.6))
    for i, name in enumerate(SCHRITTE):
        x = x0 + i * (breite_k + luecke)
        a = auftritt(t, 0.8 + i * 0.5)
        if a <= 0.01:
            continue
        # Erreicht der Laufpunkt die Kachel, faerbt sie sich ein.
        erreicht = weich((fortschritt * len(SCHRITTE) - i) / 0.6)
        fuell = mischen(FLAECHE, AKZENT_BG, erreicht)
        rand = mischen(RAND, AKZENT_HELL, erreicht)
        kachel(d, (x, y - s(80), x + breite_k, y + s(80)),
               fuell=mischen(BG, fuell, a), rand=mischen(BG, rand, a),
               radius=s(20), breite=s(3))
        text_bei(d, (x + breite_k // 2, y), name, schrift(s(42), fett=erreicht > 0.5),
                 mischen(GEDAEMPFT, AKZENT, erreicht), anker="mm", deckung=a)

    # Laufpunkt auf der Linie unter den Kacheln
    if 0.8 < t < laenge - 0.4:
        px = x0 + fortschritt * spanne
        d.ellipse((px - s(16), y_linie - s(16), px + s(16), y_linie + s(16)),
                  fill=AKZENT)

    text_bei(d, (s(BREITE) // 2, s(860)), "Der Antwortentwurf steht, bevor du tippst.",
             schrift(s(44), leicht=True), GEDAEMPFT, anker="mm",
             deckung=auftritt(t, laenge - 1.6, 0.6))


def szene_nutzen(blatt, d, t, laenge, s):
    """Vorher/nachher als zwei Balken."""
    text_bei(d, (s(160), s(150)), "Statt acht Stunden — vielleicht zwei",
             schrift(s(72), fett=True), TEXT, deckung=auftritt(t, 0.1))

    x0 = s(260)
    voll = s(1400)
    for i, (label, stunden, farbe, start) in enumerate([
            ("vorher", 8, (0xC9, 0xD1, 0xD9), 0.5),
            ("nachher", 2, AKZENT, 1.4)]):
        y = s(420 + i * 230)
        a = auftritt(t, start, 0.7)
        if a <= 0.01:
            continue
        laenge_b = int(voll * (stunden / 8) * a)
        d.rounded_rectangle((x0, y, x0 + voll, y + s(112)), radius=s(16),
                            fill=mischen(BG, (0xEC, 0xEF, 0xF2), 1.0))
        if laenge_b > s(40):
            d.rounded_rectangle((x0, y, x0 + laenge_b, y + s(112)), radius=s(16),
                                fill=farbe)
        text_bei(d, (x0, y - s(30)), label, schrift(s(38), leicht=True),
                 GEDAEMPFT, anker="lb", deckung=a)
        # Zahl zaehlt mit dem Balken hoch
        zahl = stunden * weich((t - start) / 0.7)
        text_bei(d, (x0 + laenge_b + s(34), y + s(56)),
                 f"{zahl:.0f} Std.", schrift(s(52), fett=True),
                 AKZENT if i else GEDAEMPFT, anker="lm", deckung=a)

    text_bei(d, (s(260), s(920)), "Du klickst nur noch auf Senden.",
             schrift(s(50)), TEXT, deckung=auftritt(t, laenge - 1.8, 0.6))


def szene_abschluss(blatt, d, t, laenge, s):
    """Markenflaeche, Avatar, Adresse."""
    # Volle Akzentflaeche, hereinblendend
    a_bg = auftritt(t, 0.0, 0.5)
    if a_bg > 0.01:
        d.rectangle((0, 0, s(BREITE), s(HOEHE)), fill=mischen(BG, AKZENT, a_bg))

    def hell(deckung):
        return mischen(mischen(BG, AKZENT, a_bg), WEISS, deckung)

    a_logo = auftritt(t, 0.35)
    bild_einsetzen(blatt, os.path.join(ASSETS_DIR, "logo-icon-weiss.png"),
                   (s(560), s(430)), s(240), a_logo)

    a_avatar = auftritt(t, 0.6)
    bild_einsetzen(blatt, os.path.join(ASSETS_DIR, "avatar-franz-rund-512.png"),
                   (s(1290), s(430)), s(300), a_avatar)

    a_text = auftritt(t, 0.9)
    text_bei(d, (s(BREITE) // 2, s(700)), "Drei gratis Gespräche diese Woche",
             schrift(s(64), fett=True), hell(a_text), anker="mm", deckung=1.0)
    a_url = auftritt(t, 1.2)
    text_bei(d, (s(BREITE) // 2, s(810)), "ki-lotse.tech",
             schrift(s(76), fett=True), hell(a_url), anker="mm", deckung=1.0)
    a_name = auftritt(t, 1.4)
    text_bei(d, (s(BREITE) // 2, s(910)), "Franz Grundner · KI-Lotse · Pattaya",
             schrift(s(40), leicht=True), hell(a_name * 0.85), anker="mm", deckung=1.0)


SZENEN = [szene_problem, szene_loesung, szene_nutzen, szene_abschluss]


# ── Zusammenbau ─────────────────────────────────────────────────────────────
def takt(stimme):
    """(Startzeiten der Saetze, Szenenfenster, Gesamtlaenge) aus den echten
    Audiolaengen — geschaetzte Sekunden wuerden Bild gegen Ton laufen lassen."""
    ordner = os.path.join(SPRECHER_DIR, stimme)
    laengen = [dauer(os.path.join(ordner, f"{n}.mp3")) for n in SEGMENTE]
    starts, fenster, uhr = [], [], VORLAUF
    for i, l in enumerate(laengen):
        starts.append(uhr)
        beginn = 0.0 if i == 0 else fenster[-1][1]
        uhr += l + PAUSE
        fenster.append((beginn, uhr))
    gesamt = uhr - PAUSE + NACHLAUF
    fenster[-1] = (fenster[-1][0], gesamt)
    return starts, fenster, gesamt


def zeichne(zeit, fenster, s):
    blatt = Image.new("RGB", (s(BREITE), s(HOEHE)), BG)
    d = ImageDraw.Draw(blatt)
    for szene, (beginn, ende) in zip(SZENEN, fenster):
        if beginn <= zeit < ende:
            szene(blatt, d, zeit - beginn, ende - beginn, s)
            break
    else:                                    # nach der letzten Szene: Standbild
        beginn, ende = fenster[-1]
        SZENEN[-1](blatt, d, ende - beginn, ende - beginn, s)
    return blatt


def tonspur(stimme, starts, gesamt, arbeit, mit_musik=True):
    """Sprache an ihre Startzeiten legen, Musik leise darunter."""
    ordner = os.path.join(SPRECHER_DIR, stimme)
    eingaben, filter_teile, marken = [], [], []
    for i, name in enumerate(SEGMENTE):
        eingaben += ["-i", os.path.join(ordner, f"{name}.mp3")]
        filter_teile.append(f"[{i}:a]adelay={int(starts[i] * 1000)}|"
                            f"{int(starts[i] * 1000)}[s{i}]")
        marken.append(f"[s{i}]")

    musik = os.path.join(LOGOS_DIR, "music_playful.wav")
    if mit_musik and os.path.isfile(musik):
        eingaben += ["-stream_loop", "-1", "-i", musik]
        # Musik deutlich zurueck: sie traegt, sie spielt nicht die Hauptrolle.
        filter_teile.append(f"[{len(SEGMENTE)}:a]volume=0.10,"
                            f"atrim=0:{gesamt:.2f},afade=t=out:st={gesamt - 1.5:.2f}:d=1.5[m]")
        marken.append("[m]")

    filter_teile.append("".join(marken) + f"amix=inputs={len(marken)}:"
                        f"normalize=0:duration=longest[aus]")
    ziel = os.path.join(arbeit, "ton.m4a")
    subprocess.run(["ffmpeg", "-y", "-v", "error", *eingaben,
                    "-filter_complex", ";".join(filter_teile),
                    "-map", "[aus]", "-t", f"{gesamt:.2f}",
                    "-c:a", "aac", "-b:a", "192k", ziel], check=True)
    return ziel


def main(argv=None):
    p = argparse.ArgumentParser(description="Werbevideo bauen (#160)")
    p.add_argument("--stimme", default=STIMME)
    p.add_argument("--szene", type=int, choices=range(1, len(SZENEN) + 1),
                   help="nur diese Szene als Standbild-Kontaktbogen pruefen")
    p.add_argument("--ohne-musik", action="store_true")
    p.add_argument("--ziel", default=ZIEL)
    args = p.parse_args(argv)

    ordner = os.path.join(SPRECHER_DIR, args.stimme)
    if not os.path.isdir(ordner):
        print(f"Keine Sprachdateien für {args.stimme} — erst sprecher.py laufen "
              f"lassen.", file=sys.stderr)
        return 2

    starts, fenster, gesamt = takt(args.stimme)
    s = lambda v: int(v * SUPER)              # noqa: E731 — Skalierung fuer 2x

    if args.szene:
        beginn, ende = fenster[args.szene - 1]
        laenge = ende - beginn
        blatt = Image.new("RGB", (s(BREITE) * 3, s(HOEHE)), BG)
        for i, anteil in enumerate((0.3, 0.6, 0.95)):
            teil = zeichne(beginn + laenge * anteil, fenster, s)
            blatt.paste(teil, (i * s(BREITE), 0))
        ziel = os.path.join(BASIS_DIR, f"szene{args.szene}-kontaktbogen.png")
        blatt.resize((BREITE * 3 // 2, HOEHE // 2), Image.LANCZOS).save(ziel)
        print(f"OK  {ziel}")
        return 0

    bilder = int(gesamt * FPS)
    arbeit = tempfile.mkdtemp(prefix="kilotse-video-")
    try:
        print(f"{bilder} Bilder ({gesamt:.1f} s) …")
        for n in range(bilder):
            blatt = zeichne(n / FPS, fenster, s)
            blatt.resize((BREITE, HOEHE), Image.LANCZOS).save(
                os.path.join(arbeit, f"{n:05d}.png"))
            if n % 120 == 0:
                print(f"   {n}/{bilder}")
        ton = tonspur(args.stimme, starts, gesamt, arbeit,
                      mit_musik=not args.ohne_musik)
        subprocess.run(
            ["ffmpeg", "-y", "-v", "error",
             "-framerate", str(FPS), "-i", os.path.join(arbeit, "%05d.png"),
             "-i", ton,
             "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18",
             "-c:a", "copy", "-shortest", args.ziel], check=True)
    finally:
        shutil.rmtree(arbeit, ignore_errors=True)

    print(f"OK  {args.ziel}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
