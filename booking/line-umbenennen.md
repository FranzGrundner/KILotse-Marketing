# Bestehenden LINE-Account umbenennen — Schritt für Schritt

> ✅ **ERLEDIGT / AUFGELÖST (24.07.2026):** Das LINE-Konto hatte bereits die ID
> `lorddipar` — sie ist **gesperrt und nicht mehr änderbar**. Entscheidung:
> ID **nicht** im Kundentext zeigen (off-brand), Kontakt läuft über **QR-Code**
> + **LINE-Button im Linktree**. Anzeigename ist `Franz · KI-Lotse`.
> Die Schritte unten sind nur noch Referenz. Für einen sauberen `@`-Handle
> gäbe es später den Weg **LINE Official Account** (Anleitung: [line-official-account.md](line-official-account.md)).

> **NACHTRAG 28.07.2026 — der funktionierende Link:** Der Kontaktweg ist der
> **Token-Link aus der App** (LINE → Profil → QR-Symbol):
> `https://line.me/ti/p/duSUGFi0h5`
> Der haengt an KEINER ID und bleibt gueltig. Auf der Startseite stand bis
> heute `~franz.kilotse` — diese ID existiert nicht und der Kontaktweg war
> tot. Nicht `~lorddipar` verwenden, sondern immer den Token-Link.
> Im Einsatz: Homepage-Kontaktkachel + QR (`shots/line-qr.jpg`) und der QR in
> allen elf Paket-Prospekten (`Bausteine/prospekt/pdf.py`, Konstante LINE_URL).

---

> **Franz · KI-Lotse · Pattaya** · Geschätzte Zeit: **10 Minuten**
> Ziel: Dein vorhandener LINE-Account bekommt den KI-Lotse-Auftritt.
> Vorschläge kommen aus [branding.md](../branding.md) (Variante 1 empfohlen).

---

## Zuerst das Wichtigste (bitte lesen)

An deinem LINE-Profil gibt es **zwei verschiedene Dinge**:

| | Änderbar? |
|---|---|
| **Anzeigename** (der Name, den andere sehen) | **Jederzeit**, so oft du willst |
| **LINE-ID** (`franz.kilotse`, für den Freund-Link) | **Nur ein einziges Mal** — danach **nie wieder** |

Das heißt:
- Den **Anzeigenamen** kannst du ohne Sorge auf `Franz · KI-Lotse` ändern.
- Die **LINE-ID** ist die Falle: Hast du schon einmal eine ID gesetzt, kannst du
  sie **nicht** umbenennen. Nur wenn dein Account **noch keine ID** hat, kannst du
  jetzt `franz.kilotse` festlegen — und dann ist sie für immer.

**Bevor du etwas tust:** Prüf zuerst in Schritt 2, ob schon eine ID gesetzt ist.

---

## Schritt 1 — Anzeigenamen ändern (unbedenklich)

1. LINE öffnen → unten auf **Home** (Häuschen).
2. Oben links auf dein **Profil / deinen Namen** tippen.
3. Auf **Bearbeiten** (Stift) neben dem Namen tippen.
4. Neuen Namen eingeben:

   ```
   Franz · KI-Lotse
   ```
   Den Mittelpunkt „·“ bekommst du per Kopieren aus dieser Zeile, oder nimm
   einfach `Franz - KI-Lotse` mit Bindestrich.
5. **Speichern**. Fertig — Freunde sehen ab sofort den neuen Namen.

---

## Schritt 2 — LINE-ID prüfen und (falls möglich) setzen

1. LINE → **Einstellungen** (Zahnrad, oben rechts auf Home).
2. **Profil** antippen.
3. Zeile **ID** ansehen:
   - **Steht dort schon etwas** (z. B. eine alte ID)? → Dann ist sie **vergeben
     und nicht mehr änderbar.** Überspring das Setzen. Du nutzt dann den
     **QR-Code** (Schritt 3) statt eines schönen Links — das reicht völlig.
   - **Ist das Feld leer / „ID nicht festgelegt"?** → Du darfst **einmalig** eine
     ID setzen. Tippe rein und gib ein:
     ```
     franz.kilotse
     ```
     Ist die vergeben, nimm die Ausweich-Variante aus branding.md:
     `franz.pattaya`. **Danach speichern = endgültig.**
4. Schalter **„ID-Suche erlauben"** einschalten, damit Kunden dich über die ID
   finden.

> **Merke:** Wenn `franz.kilotse` schon deine ID ist — super, nichts zu tun.
> Wenn eine andere alte ID drinsteht — lass sie stehen, arbeite mit dem QR-Code.

---

## Schritt 3 — QR-Code / Freund-Link sichern

Das ist der Weg, den Kunden zum Anschreiben nutzen — funktioniert **unabhängig**
von der ID.

1. LINE → **Home** → oben das **QR-Symbol** neben der Suchleiste.
2. Reiter **Mein QR-Code**.
3. **Teilen** → **Link kopieren** (für Linktree/Homepage) **und** ein
   **Screenshot** des QR-Codes (zum Herzeigen offline).
4. Falls du eine ID setzen konntest, lautet dein Freund-Link:
   ```
   https://line.me/ti/p/~lorddipar
   ```

---

## Schritt 4 — Statusnachricht (optional, empfohlen)

Einstellungen → Profil → **Statusnachricht**:

```
Pattaya · KI & Automatisierung nebenbei · Gratis 30-Min-Gespräch — einfach schreiben
```

---

## Schritt 5 — Profilbild (optional)

Einstellungen → Profil → Bild antippen → Logo oder ein freundliches Foto von dir.
Logo liegt in `C:\Claude\Franz\Marketing\logo\`.

---

## Danach an mich melden

Sobald feststeht, **welche ID** am Ende gilt (`franz.kilotse`, `franz.pattaya`
oder die alte), sag mir Bescheid — dann trage ich sie in den Café-Prospekt
(PDF + Homepage) ein und schließe Todo #343 ab.
