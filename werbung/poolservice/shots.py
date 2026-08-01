"""shots.py — die Bilder fuer den Poolservice-Clip aus der Live-Demo holen.

Die Regel aus dem Higgsfield-Plan (§2/§7): Produktbilder sind **echte
Screenshots**, nie KI und nie nachgezeichnete Oberflaechen. Aufgenommen wird
darum der laufende Beispielbetrieb `poolservice.demo.ki-lotse.tech` — dieselbe
Adresse, die im Clip als CTA steht. Was der Interessent im Clip sieht, findet
er dort auch wieder.

Doppelte Aufloesung (device_scale_factor=2), weil die Bilder im Video
hochskaliert und auf dem Handy gelesen werden.

Aufruf:
    python -X utf8 shots.py
"""
import os

from playwright.sync_api import sync_playwright

BASIS = os.path.dirname(os.path.abspath(__file__))
ZIEL = os.path.join(BASIS, "shots")
HOST = "https://poolservice.demo.ki-lotse.tech"

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


def main():
    os.makedirs(ZIEL, exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for name, pfad, (b, h), ausschnitt in AUFNAHMEN:
            seite = browser.new_page(viewport={"width": b, "height": h},
                                     device_scale_factor=2)
            seite.goto(HOST + pfad, wait_until="networkidle")
            datei = os.path.join(ZIEL, f"{name}.png")
            if ausschnitt == "main":
                seite.locator("main").screenshot(path=datei)
            else:
                cb, ch = ausschnitt
                seite.screenshot(path=datei,
                                 clip={"x": 0, "y": 0, "width": cb, "height": ch})
            seite.close()
            print(f"   {name}.png")
        browser.close()
    print(f"OK  {ZIEL}")


if __name__ == "__main__":
    raise SystemExit(main())
