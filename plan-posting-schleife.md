# Plan: Datengetriebene Posting-Schleife (Facebook & LINE)

> **Franz · KI-Lotse · Pattaya** · Stand: 18.07.2026 · Status: **Plan** (Konzept folgt)
> Quelle: ChatGPT-Gespräch, übersetzt und an den Ist-Stand angepasst.

---

## 1. Ziel

Ein sich selbst verbessernder Marketing-Kreislauf:

```
[1. Posts generieren (Claude)] ──▶ [2. Posten (FB-Gruppen / LINE)]
            ▲                                   │
            │                                   ▼
[4. Claude optimiert Varianten] ◀── [3. Reaktionen & Leads messen]
```

Nicht raten, was ankommt — messen, welche Post-Variante Leads und Erstgespräche bringt, und nur die Gewinner-Formate weiterentwickeln.

**Zeitbudget:** max. ~1 Stunde pro Woche + 20 Min Auswertung alle 2 Wochen.

---

## 2. Ist-Stand (das gibt es schon — nichts doppelt bauen)

| Baustein aus dem ChatGPT-Plan | Ist-Stand |
|---|---|
| Content-Erstellung mit KI | ✅ 5 Post-Varianten DE/EN fertig in [posts/](posts/) |
| Kanal-Liste + Gruppenregeln | ✅ [kanaele.md](kanaele.md) inkl. Erfolgs-Tracker |
| Posting-Ablauf Woche 1 + Rotation | ✅ [posts/testplan-woche-1.md](posts/testplan-woche-1.md) |
| Give-away (Mini-App Formulare: 90-Tage, TM7, Wohnsitz, Lebensbestätigung) | ✅ Giveaway V1+V2 live auf ki-lotse.tech (MyDocs/MySetup) |
| E-Mail/Lead-Erfassung auf der Website | ✅ Kontaktformular → Lead-Auto-Sync → Leads-Tab in MyTM |
| Terminbuchung | ✅ Calendly + Linktree ([booking/](booking/)) |
| Erstgespräch (30 Min gratis) | ✅ [erstgespraech/](erstgespraech/) Leitfaden |
| 3-Stufen-Angebot (Erste Schritte / Planung per App / Umsetzung) | ✅ [angebot/](angebot/), App = MyPro |

**Was fehlt → dieser Plan:** die Mess- und Feedback-Schleife (Schritte 3+4) und ein fester Zyklus.

---

## 3. Wichtige Korrektur gegenüber dem ChatGPT-Vorschlag

ChatGPT empfiehlt **Meta Business Suite + Insights** zum Messen. Das funktioniert **nur mit einer eigenen Business-Page** — nicht für Posts, die vom Privatprofil in fremden Gruppen stehen. Unsere Strategie ist aber genau das: Gruppen-Posts + LINE.

**Konsequenz für Phase 1:** manuell messen (dauert 10 Min alle 2 Wochen) mit den Daten, die wir ohnehin haben:

| Messwert | Quelle |
|---|---|
| Likes / Kommentare / Shares pro Post | Facebook, manuell ablesen |
| Website-Besuche → Giveaway-Downloads | ki-lotse.tech (Lead-Zahlen) |
| Leads (E-Mail-Adressen) | MyTM Leads-Tab (Auto-Sync läuft) |
| LINE-Anfragen | LINE, manuell zählen |
| Erstgespräch-Buchungen | Calendly |

Eine Business-Page ist **Phase 2** (optional, siehe unten) — erst wenn die Schleife läuft und sich Reichweite über die Gruppen hinaus lohnt.

---

## 4. Der Zyklus (2-Wochen-Takt)

### Woche A — Posten
1. **Montag (~15 Min):** 2 Post-Varianten wählen (Rotation aus [posts/testplan-woche-1.md](posts/testplan-woche-1.md)) oder mit Claude 1–2 neue Varianten generieren.
2. **Di–Do (~15 Min):** je 1 DE- und 1 EN-Gruppe aus [kanaele.md](kanaele.md) — Gruppenregeln-Schnellcheck beachten. Nie derselbe Text in mehreren Gruppen am selben Tag.
3. **Laufend:** auf Kommentare reagieren, Interessenten auf LINE holen.
4. **Jeden Post sofort in den Tracker** eintragen (Datum, Gruppe, Variante).

### Woche B — Messen & Optimieren
5. **Messen (~10 Min):** pro Post Likes/Kommentare ablesen; Leads aus MyTM und Calendly-Buchungen der 2 Wochen zuordnen. In den Erfolgs-Tracker in [kanaele.md](kanaele.md) eintragen.
6. **Optimieren (~10 Min):** Zahlen an Claude geben (Prompt unten). Claude analysiert, welche Variante/Gruppe/Sprache funktioniert, und erzeugt 2 neue Varianten im Gewinner-Stil.
7. Schwache Varianten aussortieren, neue in [posts/](posts/) ablegen → zurück zu Schritt 1.

### Optimierungs-Prompt (Vorlage)

```
Hier die Ergebnisse meiner Facebook-Posts der letzten 2 Wochen (KI-Lotse Pattaya):

- Variante X in Gruppe Y (Sprache): __ Likes, __ Kommentare, __ LINE-Anfragen, __ Leads, __ Erstgespräche
- Variante … (je Post eine Zeile)

Analysiere: Welche Variante bringt Reaktionen, welche bringt echte Leads/Gespräche?
(Likes ≠ Leads — Leads zählen mehr.) Erstelle 2 neue Post-Varianten (DE + EN),
die den Stil des Lead-Gewinners übernehmen, im bestehenden Format aus posts/.
```

> Wichtig: Optimiert wird auf **Leads und Erstgespräche**, nicht auf Likes. Ein Post mit 80 Likes und 2 Leads verliert gegen einen mit 10 Likes und 8 Leads.

---

## 5. Zeit-Filter (Schutz der eigenen Zeit)

Aus dem ChatGPT-Gespräch übernommen, da Face-to-Face + allein:

- **Keine Telefonnummer in Posts** — nur Linktree/LINE-ID, Termine nur über Calendly.
- **Calendly-Pflichtfragen** im Erstgespräch-Event prüfen/ergänzen:
  1. Was ist dein Business in Pattaya/Thailand?
  2. Welchen Prozess willst du mit KI verbessern?
- Wer die Fragen nicht ernsthaft beantwortet → kein Termin.

---

## 6. Phase 2 (optional, später)

Erst wenn der Zyklus 4–6 Wochen läuft und Daten liefert:

- **Facebook Business-Page** „Franz — KI-Lotse Pattaya“: eigene Posts planbar (Meta Business Suite), Insights automatisch, Gruppen-Posts bleiben zusätzlich.
- **Automatisierung der Messung:** Lead-Zahlen sind schon in MyTM — denkbar ist ein kleiner Report (Posts ↔ Leads pro Zeitraum) statt Handarbeit.
- **Thai-Kanäle** (Phase 2 aus kanaele.md).

Kein Make.com/Zapier nötig — Claude + bestehende Infrastruktur reichen.

---

## 7. Offene Punkte fürs Konzept

- [ ] Tracker-Format: reicht die Tabelle in kanaele.md oder eigene Datei/DB (z. B. MyTM)?
- [ ] Zuordnung Lead → Post: woran erkennen wir, aus welchem Post ein Lead kam? (z. B. eigene Linktree-/URL-Parameter pro Variante — ohne persönliche Daten in der URL)
- [ ] Calendly-Pflichtfragen final formulieren
- [ ] Startzeitpunkt Zyklus 1 (erster FB-Post ist ohnehin für nächste Woche geplant)
- [ ] Kriterium für Phase 2 (ab wie vielen Leads/Woche lohnt die Business-Page?)
