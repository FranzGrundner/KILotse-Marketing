# Poolservice-Clip — Skript

> Stand: 01.08.2026 · Für die **Direktansprache** (LINE/WhatsApp/Erstgespräch),
> nicht zum Streuen in Gruppen. Grundlage: `plan-higgsfield-monat.md` §0/§9,
> Prospekttext `Bausteine/prospekt/poolservice-garten/prospekt.md`.

## Rahmen

| | |
|---|---|
| Format | 1080 × 1350 (4:5), 30 fps — füllt die Feed-Spalte, passt im Messenger |
| Länge | ~22 s |
| Ton | Sprecherspur (edge-tts, `de-DE-FlorianMultilingualNeural`), Musik leise darunter |
| Ohne Ton | vollständig verständlich — jeder Satz steht auch im Bild |
| Bilder | **echte Screenshots** vom laufenden Beispielbetrieb `poolservice.demo.ki-lotse.tech`, nur beschnitten |

## Die fünf Szenen

| # | Bild | Text im Bild | Sprache |
|---|---|---|---|
| 1 | zwei Zitatkacheln, kein Screenshot | »Ihr wart letzte Woche nicht da.« / »Doch. Waren wir.« → *Beweisen kann es keiner.* | „Der Kunde sagt, ihr wart nicht da. Deine Leute sagen: doch." |
| 2 | `nachweis.png`, zwei Ausschnitte derselben Einsatz-Seite | **Am Einsatz steht, was war.** / Datum · Servicekraft · **das Foto und die Unterschrift** | „Datum, Servicekraft, Foto — steht alles am Einsatz." |
| 3 | `vertraege.png` (Spalte Rhythmus) | **Verträge laufen im Rhythmus.** / Die Einsätze entstehen daraus von selbst. | „Jeder Vertrag hat seinen Rhythmus — die Einsätze entstehen von selbst." |
| 4 | `rechnungen.png` (Belegliste) | **Am Monatsende wird daraus die Rechnung.** / Offen, bezahlt, überfällig — auf einen Blick. | „Am Monatsende wird daraus die Rechnung." |
| 5 | Markenfläche, Logo + Avatar | poolservice.demo.ki-lotse.tech | „Ansehen kannst du es sofort — ki-lotse punkt tech." |

## Regeln, die hier eingehalten sind

- **Domain fürs Ohr, nicht fürs Auge** gesprochen („ki-lotse punkt tech") — Lehre aus #160.
  Im Bild steht die vollständige Demo-Adresse.
- **Nichts, was altert** (§8.4): keine Preise, keine Paketzusammensetzung, kein „seit X Wochen".
  Der Clip stimmt auch in drei Monaten noch.
- **Keine erfundene Oberfläche.** Gezeigt wird nur, was die Demo wirklich zeigt.
  Seit `wartung` v1.1.0 (01.08.2026) hängen am erledigten Poolservice-Einsatz ein
  Beispielfoto **und** eine Unterschrift — vorher standen dort leere Upload-Felder,
  und der stärkste Prospektsatz („Hier ist das Foto") war deshalb aus dem Clip
  herausgehalten. Jetzt ist er Szene 2 und steht mit einem echten Screenshot dahinter.
  Die Bilder im Seed sind selbst erzeugt (kein Stockfoto, keine Person, keine echte
  Unterschrift) — Herkunft in `Bausteine\wartung\docs\demo-bilder.md`.
- **Kein Kundenname.** Strodos wird nicht genannt; das Referenzargument gehört ins
  Gespräch, nicht in eine Datei, die weitergeleitet wird.

## Bauen

```
python -X utf8 shots.py     # Screenshots aus der Live-Demo (nur bei Änderungen nötig)
python -X utf8 clip.py      # Sprecherspur + Video
```

Prüfansicht einer einzelnen Szene: `python -X utf8 clip.py --szene 2`
