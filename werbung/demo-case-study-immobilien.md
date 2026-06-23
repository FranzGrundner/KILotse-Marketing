# Demo Case Study — Immobilien-Anfragen (anonymisiert)

> Showcase für Posts und Loom-Video. Kein echter Kundenname — Demo-Daten.

## Ausgangslage (Vorher)

**Kunde-Typ:** Expat-Immobilienmakler, Pattaya/Jomtien  
**Problem:** 15–25 Anfragen pro Woche über Facebook Messenger, LINE und WhatsApp. Jede Anfrage manuell in Google Sheets übertragen, Antworten einzeln tippen.

**Zeitaufwand:** ca. **6–8 Stunden/Woche** nur für Erfassung und Erstantworten.

**Tools vorher:** Messenger, LINE, WhatsApp, Google Sheets (manuell)

---

## Lösung (Nachher)

**Automatisierter Flow:**

```
Anfrage (FB/LINE/WhatsApp)
    → KI extrahiert: Name, Budget, Zimmer, Bezirk, Kontakt
    → Eintrag in Google Sheets (neue Zeile, Priorität)
    → Entwurf-Antwort auf Deutsch oder Englisch
    → LINE-Nachricht an Makler: „Neue Anfrage — Entwurf bereit“
    → Makler: prüfen, ggf. 1 Satz anpassen, senden
```

**Zeitaufwand nachher:** ca. **1–2 Stunden/Woche**

**Leistungsstufe im Generator:** 3 (Komplettentwicklung) oder 2 (wenn Kunde mit Prompts weiterarbeiten will)

---

## Use Cases (für MyPro)

| # | Use Case | Modul |
|---|---|---|
| 1 | Anfrage aus Kanal auslesen | Input-Parser |
| 2 | Felder in Sheet schreiben | Sheets-Integration |
| 3 | Antwortentwurf generieren | KI-Prompt (DE/EN) |
| 4 | Benachrichtigung an Makler | LINE |

---

## Vorher / Nachher (für Werbung)

| | Vorher | Nachher |
|---|---|---|
| Erfassung | Manuell, fehleranfällig | Automatisch strukturiert |
| Antwortzeit | Stunden bis nächster Tag | Minuten (Entwurf sofort) |
| Sprachen | Durcheinander | DE/EN je nach Anfrage |
| Überblick | 3 Apps durchklicken | Eine Sheet-Übersicht + LINE |

---

## So im Generator vorführen

1. Neues Demo-Projekt: `demo-immobilien-pattaya`
2. Leistungsstufe 3, Ausgabesprache DE
3. Use Cases aus Tabelle oben eintragen
4. Export / Präsentationsmodus für Screenshot oder Loom
5. **Keine echten Kundendaten** im Screenshot — nur Demo-Namen („Max M.“, „Budget 25k THB“)

---

## Hook-Zeilen für Posts

**DE:** „Von 8 Stunden Copy-Paste auf 2 Stunden pro Woche — bei Immobilien-Anfragen in Pattaya.“

**EN:** „From 8 hours of copy-paste to 2 hours a week — for property inquiries in Pattaya.“
