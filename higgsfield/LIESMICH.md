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

## Nachgezogen am 24.08.2026

Seit der Sicherung vom 19.08. sind **acht** Erzeugnisse dazugekommen; sie hingen
bis heute allein in der Galerie und waren nirgends gesichert.

| Datum | Videos | Bilder |
|---|---|---|
| 20.08.2026 | 2 | 3 |
| 24.08.2026 | 2 | 1 |

Neuer Bestand: `bilder/` **53** · `videos/` **35** · `audio/` **38**. Die
Sollzahlen der Seitenleiste (Image 53 · Video 35) sind damit erreicht. Audio
steht dort auf 73 statt 69 — die vier zusaetzlichen sind die Tonspuren der vier
neuen Videos, eigene Audiodateien sind keine dazugekommen.

**Der Weg war diesmal ein anderer** als der Sammel-Download: Higgsfield liefert
die Dateien ueber `https://d8j0ntlcm91z4.cloudfront.net/user_<konto>/<kennung>.<mp4|png>`
direkt aus. Die Kennung steht im Vorschaubild-Namen der Galerie, die Endung
laesst sich per HEAD-Anfrage bestimmen (mp4 fuer Video, png fuer Bild). Das
umgeht die Falle mit dem Nachladen beim Scrollen, weil nicht die Auswahl in der
Galerie zaehlt, sondern die Liste der Kennungen.

### Offen: die Prompts der acht Neuen

`PROMPTS.md` hat zu diesen acht **keine** Eintraege — die Luecke, die oben als
geschlossen vermerkt ist, steht fuer sie also wieder offen. Die Vorlage der
vier Erzeugnisse vom 24.08. liegt als `andi-prompts-2026-08-24.txt` daneben
(elf Werbespot-Prompts von Andi, Variante 1 ist die Buero/Wiese-Verwandlung).
Welcher Prompt tatsaechlich abgeschickt wurde, ist daraus nicht ablesbar — der
Name im Text wurde vor dem Lauf geaendert.

### Repariert statt neu gerendert

`gyde-buero-wiese-schrift-repariert.mp4` ist der Clip vom 24.08. (074200) mit
richtiger Schrift. Higgsfield hatte an dieser Stelle **"PAKCTIA"** und zwei
Zeilen Buchstabensalat gesetzt. Weil die Einblendung ab Sekunde 4,21 fest an
einer Stelle ueber unscharfer Wiese steht, liess sich die Flaeche aus ihren
Raendern zurueckrechnen (`delogo`) und echt neu beschriften (`drawtext`) —
**ohne Renderlauf, ohne Credits**, und ohne die Verwandlung zu verlieren, die
nur in einem Take gelingt. Die Tonspur ist unveraendert.

**Die Lehre daraus:** `On-screen text:` und `Voice-over:` im Prompt sind
verlorene Muehe. Kein Videomodell setzt einen deutschen Satz richtig. Der Clip
liefert das Bild, Schrift und Stimme kommen danach.

## Die Referenzbilder der Kampagne (24.08.2026)

Die Personen-Aehnlichkeit in den Werbespots entsteht ueber **vier
Referenzbilder**, die bei der Erzeugung des Startbildes mitgegeben werden. Sie
sind das wertvollste Stueck am ganzen Vorhaben und waren bis heute nur auf dem
Desktop (`pics2`) vorhanden — also nirgends gesichert. Der Ordner liegt jetzt
vollstaendig unter `Franz/_fotos/referenz-kampagne/` (30 Dateien, 45 MB,
bitgenau uebernommen).

Die vier sind: `00_studio.png` (Smoking) sowie je eine Aufnahme aus
`IMG_20260801_1358xx` (Nahaufnahme), `IMG_20260801_1500xx` (frontal) und
`IMG_20260801_14592x` (Ganzkoerper).

**Sie decken zusammen Gesicht nah, Halbfigur, Ganzkoerper und formell ab** —
daher die gute Treffsicherheit. Fuer jeden weiteren Spot **dieselben vier**
verwenden; das haelt dieselbe Person durch alle Clips und macht aus Einzelclips
eine Kampagne.

`00_studio.png` faellt aus der Reihe: es stammt nicht aus der Fotosession vom
01.08., sondern ist ein fertiges Studiobild. Woher es kommt, ist nicht
rekonstruierbar.

## Die Spots (24.08.2026)

`spots-9x16.md` enthaelt vier ausgearbeitete Spots im Format **9:16**, je mit
Prompt fuer Startbild und Video: Labyrinth, Baustelle, Buero/Wiese,
Kontrollraum. Aus Andis elf Vorlagen ausgewaehlt und umgeschrieben — ohne
`On-screen text` und ohne `Voice-over`, also **ohne Markennamen im Bild**.

`spot-buero-wiese-9x16.mp4` (1080x1920) ist der fertige dritte Spot: aus dem
3:4-Lauf vom 24.08. auf 9:16 beschnitten, Schrift repariert. Der Beschnitt
haelt beide Szenen — es brauchte dafuer keinen zweiten Renderlauf.

## Stand des Abos (19.08.2026)

Plus Plan, **verlängert sich am 01.09.2026** — dann zum regulären Preis von
49 USD statt der 29 USD des ersten Monats (Todo **#590**: die Ausgabenzeile in
MyTM ist ab dann zu ändern). Guthaben: **730 von 1000 Credits**, Auto-Refill
aus. Bei rund 55 Credits je Clip sind das noch etwa 13 Clips (Todo **#642**).
