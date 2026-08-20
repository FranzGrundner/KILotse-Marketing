# Higgsfield — gesicherter Bestand

**Gezogen am 19.08.2026** aus `higgsfield.ai/assets` (Konto Franz Grundner,
Plus Plan). Anlass ist Todo **#457**: Higgsfield sagt zu den Erzeugnissen
ausdrücklich *„your generations aren't guaranteed to be saved past the end of
your subscription"* — die Galerie ist nach einem Abo-Ende also **nicht**
garantiert erreichbar, und Restcredits verfallen sofort zum Periodenende.

## Was hier liegt

| Ordner | Dateien | Größe |
|---|---|---|
| `bilder/` | 49 | 145,5 MB |
| `videos/` | 31 | 243,3 MB |
| `audio/` | 38 | 1,7 MB |
| **gesamt** | **118** | **391 MB** |

Die 118 sind der **vollständige** Bestand: Higgsfield zählt in der Seitenleiste
„All Assets 118", und die Summe stimmt (49 + 31 + 38). Die dort genannten
*69 Audios* sind mehr, weil die Tonspuren der Videos mitgezählt werden; als
eigene Dateien liegen 38 vor.

Zeitraum der Erzeugung: **03.08. bis 14.08.2026**, in vier Blöcken (14.08. ·
03.08. · 02.08. · 01.08.).

## Wie gesichert wurde

Über den Sammel-Download der Galerie: Datumsblock auswählen → `Download` →
Higgsfield packt ein ZIP. Die Archive lagen danach im Downloads-Ordner und sind
hier nach Typ einsortiert; vorhandene Dateien wurden **nie** überschrieben.

**Eine Falle dabei, die zählt:** Die Galerie lädt beim Scrollen nach, und ein
Klick auf den Datumskopf wählt nur die **bereits geladenen** Kacheln. Beim
ersten Durchgang fehlten deshalb fünf Dateien. Verlässlicher sind die
Typ-Filter links (*Image · Video · Audio*) — dort steht die Sollzahl daneben und
lässt sich gegen den Ordner hier zählen.

## Die Prompts liegen daneben

**Nachgezogen am 20.08.2026.** Je Ordner eine `PROMPTS.md` mit dem Prompt und
den Erzeugungsdaten (Modell, Groesse, Zeitpunkt, bei Ton die Stimme) zu **jeder**
der 118 Dateien. Die Zuordnung laeuft ueber die **UUID im Dateinamen** — sie ist
zugleich die Asset-Kennung der Galerie, `hf_JJJJMMTT_hhmmss_<uuid>` also direkt
adressierbar unter `higgsfield.ai/asset/all/<uuid>`.

| Ordner | Eintraege |
|---|---|
| `bilder/PROMPTS.md` | 49 |
| `videos/PROMPTS.md` | 31 |
| `audio/PROMPTS.md` | 38 |

Ein Stueck faellt aus dem Raster und ist eigens vermerkt: das Video `92d05cd3`
traegt gar keinen Prompt, es entstand ueber die Funktion *Change Voice* aus
einem anderen Video. Wer dort einen Prompt sucht, sucht vergeblich — es gab
nie einen.

Damit ist die Luecke geschlossen, die hier vorher stand: dass an den Dateien
nicht mehr ablesbar sei, wie sie entstanden sind.

## Stand des Abos (19.08.2026)

Plus Plan, **verlängert sich am 01.09.2026** — dann zum regulären Preis von
49 USD statt der 29 USD des ersten Monats (Todo **#590**: die Ausgabenzeile in
MyTM ist ab dann zu ändern). Guthaben: **730 von 1000 Credits**, Auto-Refill
aus. Bei rund 55 Credits je Clip sind das noch etwa 13 Clips (Todo **#642**).
