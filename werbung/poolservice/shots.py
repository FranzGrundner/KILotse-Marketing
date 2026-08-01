"""shots.py — die Bilder fuer den Poolservice-Clip aus der Live-Demo holen.

Die Regel aus dem Higgsfield-Plan (§2/§7): Produktbilder sind **echte
Screenshots**, nie KI und nie nachgezeichnete Oberflaechen. Aufgenommen wird
darum der laufende Beispielbetrieb `poolservice.demo.ki-lotse.tech` — dieselbe
Adresse, die im Clip als CTA steht. Was der Interessent im Clip sieht, findet
er dort auch wieder.

Je Sprache ein eigener Satz: ein englischer Clip mit deutschen Bildschirmen
waere schlechter als gar keiner. Die Demo schaltet ueber `/sprache/<code>`,
und weil das eine Sitzung setzt, laufen alle Aufnahmen einer Sprache durch
denselben Browser-Kontext.

Doppelte Aufloesung (device_scale_factor=2), weil die Bilder im Video
hochskaliert und auf dem Handy gelesen werden.

Aufruf:
    python -X utf8 shots.py                 alle Sprachen
    python -X utf8 shots.py --sprache en
"""
import argparse
import os

from playwright.sync_api import sync_playwright

BASIS = os.path.dirname(os.path.abspath(__file__))
ZIEL = os.path.join(BASIS, "shots")
HOST = "https://poolservice.demo.ki-lotse.tech"

SPRACHEN = ["de", "en"]

# (Name, Pfad, Viewport, Ausschnitt)
# "main" = Element-Aufnahme des Inhaltsbereichs (kompakte Seiten),
# (b, h)  = Ausschnitt ab oben (lange Listen, die sonst als Bandwurm kaemen).
AUFNAHMEN = [
    ("nachweis",   "/wartung/einsaetze/13",  (900, 950),  "main"),
    ("einsaetze",  "/wartung/einsaetze",     (1000, 1000), (1000, 700)),
    ("vertraege",  "/wartung/vertraege",     (1000, 800), "main"),
    ("abrechnung", "/wartung/abrechnung",    (1000, 1000), "main"),
    ("rechnungen", "/rechnungen/uebersicht",  (900, 900), "main"),
]


def satz(browser, sprache):
    ordner = os.path.join(ZIEL, sprache)
    os.makedirs(ordner, exist_ok=True)
    # Ein Kontext je Sprache: /sprache/<code> setzt eine Sitzung, die bei
    # jeder neuen Seite mitkommen muss.
    ctx = browser.new_context(viewport={"width": 1000, "height": 900},
                              device_scale_factor=2)
    seite = ctx.new_page()
    seite.goto(f"{HOST}/sprache/{sprache}", wait_until="networkidle")
    for name, pfad, (b, h), ausschnitt in AUFNAHMEN:
        seite.set_viewport_size({"width": b, "height": h})
        seite.goto(HOST + pfad, wait_until="networkidle")
        datei = os.path.join(ordner, f"{name}.png")
        if ausschnitt == "main":
            seite.locator("main").screenshot(path=datei)
        else:
            cb, ch = ausschnitt
            seite.screenshot(path=datei,
                             clip={"x": 0, "y": 0, "width": cb, "height": ch})
        print(f"   {sprache}/{name}.png")
    ctx.close()


def main(argv=None):
    p = argparse.ArgumentParser(description="Screenshots aus der Live-Demo holen")
    p.add_argument("--sprache", choices=SPRACHEN)
    args = p.parse_args(argv)

    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        for sprache in ([args.sprache] if args.sprache else SPRACHEN):
            satz(browser, sprache)
        browser.close()
    print(f"OK  {ZIEL}")


if __name__ == "__main__":
    raise SystemExit(main())
