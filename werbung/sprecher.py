"""sprecher.py — Sprecherspur fuers Loom-Video (#160) synthetisch erzeugen.

Franz will nicht vor die Kamera; die Stimme kommt darum aus Text-to-Speech.
Genutzt wird `edge-tts` (Microsoft-Neural-Stimmen): kostenlos, ohne Konto,
braucht aber Internet — der Text geht zum Synthetisieren an Microsoft. Fuer
einen Werbetext ist das unkritisch, fuer Vertrauliches waere es der falsche Weg.

Die Textquelle ist `loom-skript.md` (30-Sekunden-Fassung, Spalte "Sprache").
Die Saetze stehen hier bewusst noch einmal als Liste: das Skript ist eine
Tabelle fuer Menschen, kein Datenformat — es zu parsen waere zerbrechlicher,
als die vier Saetze zu pflegen.

Aufruf:
    python -X utf8 sprecher.py                 alle Kandidatenstimmen
    python -X utf8 sprecher.py --stimme de-AT-JonasNeural
    python -X utf8 sprecher.py --stimmen       verfuegbare deutsche Stimmen
"""
import argparse
import asyncio
import os
import sys

import edge_tts

BASIS_DIR = os.path.dirname(os.path.abspath(__file__))
AUSGABE = os.path.join(BASIS_DIR, "sprecher")

# Kandidaten. de-AT zuerst: Franz ist Oesterreicher, seine Zielgruppe sind
# deutschsprachige Expats — eine oesterreichische Stimme sitzt naeher als eine
# bundesdeutsche.
KANDIDATEN = [
    "de-AT-JonasNeural",
    "de-DE-ConradNeural",
    "de-DE-FlorianMultilingualNeural",
]

# Sprechtext aus loom-skript.md. EINE Abweichung gegenueber dem Skript: der
# Schluss zeigte auf Linktree/Calendly — das stammt aus der Zeit vor der
# Homepage. Heute ist ki-lotse.tech live und der richtige Anlaufpunkt.
SAETZE = [
    ("01-problem",
     "Kennst du das? Anfragen von überall — und alles per Hand in Excel."),
    ("02-loesung",
     "So sieht die Lösung aus: Anfrage rein, Daten raus, Antwortentwurf fertig."),
    ("03-nutzen",
     "Statt acht Stunden — vielleicht zwei. Du klickst nur noch auf Senden."),
    ("04-abschluss",
     "Diese Woche noch drei gratis Gespräche. Alles Weitere auf ki-lotse.tech."),
]

# Etwas langsamer als Standard: der Text ist dicht, und die Zielgruppe hoert
# ihn nebenbei auf Facebook.
TEMPO = "-8%"


async def sprich(text, stimme, ziel, tempo=TEMPO):
    ansage = edge_tts.Communicate(text, stimme, rate=tempo)
    await ansage.save(ziel)


async def ganze_spur(stimme):
    """Alle Saetze einer Stimme, einzeln und als durchgehende Spur."""
    ordner = os.path.join(AUSGABE, stimme)
    os.makedirs(ordner, exist_ok=True)
    teile = []
    for name, text in SAETZE:
        ziel = os.path.join(ordner, f"{name}.mp3")
        await sprich(text, stimme, ziel)
        teile.append(ziel)
        print(f"   {os.path.basename(ziel)}")
    # Ganzer Text am Stueck — so klingt es im Video wirklich.
    ganz = os.path.join(ordner, "00-ganzer-text.mp3")
    await sprich(" ".join(t for _, t in SAETZE), stimme, ganz)
    print(f"   {os.path.basename(ganz)}")
    return ganz


async def stimmen_zeigen():
    for v in await edge_tts.list_voices():
        if v["Locale"].startswith("de-"):
            print(f"{v['ShortName']:34} {v['Gender']:6} {v['Locale']}")


def main(argv=None):
    p = argparse.ArgumentParser(description="Sprecherspur fuers Loom-Video (#160)")
    p.add_argument("--stimme", help="nur diese Stimme")
    p.add_argument("--stimmen", action="store_true", help="deutsche Stimmen auflisten")
    args = p.parse_args(argv)

    if args.stimmen:
        asyncio.run(stimmen_zeigen())
        return 0

    stimmen = [args.stimme] if args.stimme else KANDIDATEN
    os.makedirs(AUSGABE, exist_ok=True)
    for stimme in stimmen:
        print(f"{stimme}:")
        try:
            asyncio.run(ganze_spur(stimme))
        except Exception as e:                      # Netz weg, Stimme unbekannt
            print(f"   FEHLER: {e}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
