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
import os
import shutil
import subprocess
import sys
import tempfile

from PIL import Image, ImageDraw

BASIS = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(BASIS)))      # ../video.py

import edge_tts                                               # noqa: E402
from video import (AKZENT, ASSETS_DIR, BG, LOGOS_DIR, WEISS,   # noqa: E402
                   auftritt, bild_einsetzen, mischen, schrift, text_bei)

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

# Der Clip aus prompts.md. Reihenfolge = Reihenfolge im fertigen Post.
SHOTS = [
    {"datei": "01-buero",
     "de": "Alle sind draußen. Du nicht.",
     "en": "Everyone's outside. You're not."},
    {"datei": "02-arm",
     "de": "Das muss nicht so sein.",
     "en": "It doesn't have to be."},
    {"datei": "03-hinaus",
     "de": "Ich zeige dir den Weg.",
     "en": "Let me show you the way."},
]

ABSPANN = {
    "de": ("Ich zeige dir den Weg.", "Franz Grundner · KI-Lotse · Pattaya"),
    "en": ("Let me show you the way.", "Franz Grundner · KI-Lotse · Pattaya"),
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
    zeilen = umbrechen(d, satz, f, BREITE - 160)
    # Von unten setzen, mit Sicherheitsabstand: Facebook legt im Feed eigene
    # Bedienelemente ueber den unteren Rand.
    y = HOEHE - 210 - len(zeilen) * 78
    for zeile in zeilen:
        d.text((80, y), zeile, font=f, fill=(255, 255, 255, 255))
        y += 78
    ebene.save(ziel)


def abspannbild(sprache, ziel):
    """Markenflaeche als Standbild — der Abspann braucht keine Bewegung."""
    blatt = Image.new("RGB", (BREITE, HOEHE), AKZENT)
    d = ImageDraw.Draw(blatt)
    bild_einsetzen(blatt, os.path.join(ASSETS_DIR, "logo-icon-weiss.png"),
                   (390, 470), 210, 1.0)
    bild_einsetzen(blatt, os.path.join(ASSETS_DIR, "avatar-franz-rund-512.png"),
                   (700, 470), 250, 1.0)
    satz, name = ABSPANN[sprache]
    text_bei(d, (BREITE // 2, 730), satz, schrift(46, leicht=True), WEISS,
             anker="mm")
    text_bei(d, (BREITE // 2, 850), "ki-lotse.tech", schrift(72, fett=True),
             WEISS, anker="mm")
    text_bei(d, (BREITE // 2, 960), name, schrift(34, leicht=True),
             mischen(AKZENT, WEISS, 0.85), anker="mm")
    blatt.save(ziel)


# ── Bildspur ────────────────────────────────────────────────────────────────
def segment(quelle, text_png, laenge, ziel):
    """Ein Rohclip: auf 4:5 bringen, Textebene darueber, Laenge festzurren.

    `increase` + `crop` statt `decrease` + Balken: schwarze Balken kosten im
    Feed die halbe Aufmerksamkeit. Was Higgsfield in 16:9 liefert, wird auf die
    Bildmitte beschnitten — die Prompts sind darauf ausgelegt.
    """
    kette = (
        f"[0:v]scale={BREITE}:{HOEHE}:force_original_aspect_ratio=increase,"
        f"crop={BREITE}:{HOEHE},setsar=1,fps={FPS},trim=0:{laenge:.2f},"
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


# ── Tonspur ─────────────────────────────────────────────────────────────────
async def _sprich(text, ziel):
    await edge_tts.Communicate(text, STIMME, rate=TEMPO).save(ziel)


def stimmen(sprache, neu=False):
    ordner = os.path.join(SPRECHER, sprache)
    os.makedirs(ordner, exist_ok=True)
    dateien = []
    for shot in SHOTS:
        ziel = os.path.join(ordner, f"{shot['datei']}.mp3")
        if neu or not os.path.isfile(ziel):
            asyncio.run(_sprich(shot[sprache], ziel))
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


def tonspur(starts, gesamt, arbeit, sprache, mit_stimme):
    eingaben, teile, marken = [], [], []
    if mit_stimme:
        for i, pfad in enumerate(stimmen(sprache)):
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
def dummys():
    """Rohclips vortaeuschen, damit die Kette ohne Abo pruefbar ist (§0.5).

    Bewusst in verschiedenen Seitenverhaeltnissen: 16:9, 9:16 und 1:1. Genau
    daran zeigt sich, ob Skalierung und Beschnitt taugen — ein Test mit lauter
    4:5-Dateien wuerde nichts beweisen.
    """
    os.makedirs(ROH, exist_ok=True)
    masse = [("1920x1080", 5.0), ("1080x1920", 4.5), ("1080x1080", 5.5)]
    for shot, (groesse, laenge) in zip(SHOTS, masse):
        ziel = os.path.join(ROH, f"{shot['datei']}.mp4")
        ffmpeg("-f", "lavfi", "-i",
               f"testsrc2=size={groesse}:rate={FPS}:duration={laenge}",
               "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "23", ziel)
        print(f"   {os.path.basename(ziel)}  ({groesse}, {laenge} s)")


# ── Zusammenbau ─────────────────────────────────────────────────────────────
def bauen(sprache, mit_stimme=True):
    fehlend = [s["datei"] for s in SHOTS
               if not os.path.isfile(os.path.join(ROH, f"{s['datei']}.mp4"))]
    if fehlend:
        print(f"Fehlende Rohclips in {ROH}: {', '.join(fehlend)}\n"
              f"Higgsfield-Clips dort ablegen oder --dummy für einen Probelauf.",
              file=sys.stderr)
        return None

    os.makedirs(FERTIG, exist_ok=True)
    arbeit = tempfile.mkdtemp(prefix="montage-")
    try:
        teile, starts, uhr = [], [], 0.0
        for i, shot in enumerate(SHOTS):
            quelle = os.path.join(ROH, f"{shot['datei']}.mp4")
            laenge = min(dauer(quelle), MAX_SHOT_S)
            png = os.path.join(arbeit, f"text{i}.png")
            textebene(shot[sprache], png)
            ziel = os.path.join(arbeit, f"seg{i}.mp4")
            segment(quelle, png, laenge, ziel)
            teile.append(ziel)
            starts.append(uhr + 0.3)
            uhr += laenge
            print(f"   {shot['datei']}  {laenge:.1f} s")

        bild = os.path.join(arbeit, "abspann.png")
        abspannbild(sprache, bild)
        ziel = os.path.join(arbeit, "seg_abspann.mp4")
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
            for shot, start, pfad in zip(SHOTS, starts, stimmen(sprache)):
                ende = start + dauer(pfad)
                grenze = starts[SHOTS.index(shot) + 1] if shot is not SHOTS[-1] else gesamt
                if ende > grenze + 0.2:
                    print(f"   Hinweis: „{shot[sprache]}“ ist {ende - grenze:.1f} s "
                          f"länger als sein Bild.")

        ton = tonspur(starts, gesamt, arbeit, sprache, mit_stimme)
        endziel = os.path.join(FERTIG, f"01-eyecatcher-{sprache}-4x5.mp4")
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
    p.add_argument("--sprache", default="de", choices=["de", "en"])
    p.add_argument("--beide", action="store_true")
    p.add_argument("--ohne-stimme", action="store_true")
    p.add_argument("--dummy", action="store_true",
                   help="Platzhalter-Rohclips erzeugen (Probelauf ohne Abo)")
    args = p.parse_args(argv)

    if args.dummy:
        dummys()

    for sprache in (["de", "en"] if args.beide else [args.sprache]):
        print(f"{sprache}:")
        if bauen(sprache, mit_stimme=not args.ohne_stimme) is None:
            return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
