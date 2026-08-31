# Higgsfield — gesicherter Bestand

**Gezogen am 19.08.2026** aus `higgsfield.ai/assets` (Konto Franz Grundner,
Plus Plan). Anlass ist Todo **#457**: Higgsfield sagt zu den Erzeugnissen
ausdrücklich *„your generations aren't guaranteed to be saved past the end of
your subscription"* — die Galerie ist nach einem Abo-Ende also **nicht**
garantiert erreichbar, und Restcredits verfallen sofort zum Periodenende.

## Was hier liegt

**Nachgezogen am 30.08.2026** — der letzte Stand vor dem Ende des Abos.

| Ordner | aus Higgsfield | Größe |
|---|---|---|
| `bilder/` | 86 | 275 MB |
| `videos/` | 46 | 394 MB |
| `audio/` | 38 | 2 MB |
| **gesamt** | **170** | **671 MB** |

Die 170 sind der **vollständige** Bestand: Higgsfield zählt in der Seitenleiste
„All Assets 170", und die Typ-Filter nennen **Image 86 · Video 46 · Audio 84**.

*(Die Größen sind hier die der `hf_`-Dateien allein, frisch nachgemessen. Die
Ordner sind größer, weil die eigenen Fassungen mit darin liegen.)*

> **Dreiundzwanzig Stück sind am 30.08.2026 hier entstanden** — drei
> Tarain-Spots: sechzehn Startbilder und sieben Clips. Sie sind noch am selben Tag
> gesichert worden, weil das Abo ausläuft.

> **Die Audio-Zahl geht auf, und das ist der Beleg:** 46 Video-Tonspuren + 38
> eigenständige Audios = 84. Dieselbe Rechnung stimmte schon am 19.08. (31 + 38
> = 69). Wer nur die 38 zählt und die 84 daneben sieht, hält den Bestand für
> unvollständig — er ist es nicht.
>
> **Eine Feinheit seit 30.08.:** Alle sieben Clips dieses Tages sind mit *Ton aus*
> gerendert und haben **keine** Tonspur — die Galerie zählt trotzdem je ein
> Audio-Erzeugnis dazu. Die Rechnung stimmt also weiter, die Dateien sind aber
> wirklich stumm.

Zeitraum der Erzeugung: **01.08. bis 30.08.2026**, in sieben Blöcken (30.08. · 27.08. ·
25.08. · 24.08. · 20.08. · 14.08. · 03./02./01.08.). Das Datum steckt im
Dateinamen (`hf_JJJJMMTT_…`) — **daran lässt sich jederzeit nachzählen, welche
Blöcke gesichert sind**, ohne die Galerie zu öffnen.

**Drei fertige Tarain-Spots liegen in `videos/`:**

| | Datei | |
|---|---|---|
| 1 | `spot-tara-9x16.mp4` (9,54 s) | Die Waage — Sturz und Aufheben; `-text` daneben mit den Platzhalterzeilen |
| 2 | `spot-schlitz-9x16.mp4` (9,46 s) | Es kommt zurück — abgelehnt, dann angenommen; `-text` daneben mit den Platzhalterzeilen |
| 3 | `spot-schablone-9x16.mp4` (8,25 s) | Die Schablone — heute passt sie, nächstes Jahr nicht mehr; `-text` daneben |

Der erste sagt *melden*, der zweite *und es hält*, der dritte *und nächstes Jahr
auch noch*. Einzelheiten in `videos/PROMPTS.md`.

**In `videos/` liegen zusätzlich 14 eigene Dateien** (die 9×16-Spots, die
Rohlinge, der reparierte Wiesen-Clip). Sie tragen keinen `hf_`-Namen und zählen
nicht zum Higgsfield-Bestand — wer die Ordner bloß zählt, kommt deshalb auf 60
Videos und wundert sich.

### Was am 30.08.2026 noch gefehlt hat

Dreizehn Dateien: **zwölf Bilder vom 27.08.** und **ein Video vom 25.08.**
Aufgefallen sind sie nicht beim Ansehen, sondern beim **Zählen** — die Ordner
schienen voll, und die Annahme *„wir haben schon alles"* hätte gehalten, wenn
niemand die Typ-Filter dagegen gehalten hätte. Die letzte Sicherung davor war
am 24.08.; sechs Tage genügten für dreizehn Dateien.

## Wie gesichert wurde

Über den Sammel-Download der Galerie: Datumsblock auswählen → `Download` →
Higgsfield packt ein ZIP. Die Archive lagen danach im Downloads-Ordner und sind
hier nach Typ einsortiert; vorhandene Dateien wurden **nie** überschrieben.

**Eine Falle dabei, die zählt:** Die Galerie lädt beim Scrollen nach, und ein
Klick auf den Datumskopf wählt nur die **bereits geladenen** Kacheln. Beim
ersten Durchgang fehlten deshalb fünf Dateien. Verlässlicher sind die
Typ-Filter links (*Image · Video · Audio*) — dort steht die Sollzahl daneben und
lässt sich gegen den Ordner hier zählen.

## Referenzbild: nur ueber die Galerie, nie ueber das Dateifeld

Das **Dateifeld** neben dem Prompt (`+`) nimmt eine ferngesteuert eingesetzte
Datei **nicht** an: der Ladekringel laeuft eine halbe Minute und hinterlaesst
eine **leere Kachel** — kein Vorschaubild, kein Fehler, keine Meldung. Zweimal
probiert, mit 1,2 MB PNG und mit 100 KB JPEG, beide Male dasselbe.

**Der Weg, der traegt:** Das Bild in der Galerie oeffnen und dort den Knopf
**`Reference`** nehmen (steht neben `Recreate`, unter `Turn to video`). Damit
wird ein Erzeugnis aus dem eigenen Bestand zur Vorlage — genau so ist am
30.08. frueh die 9:16-Justitia aus der Querformat-Fassung entstanden.

**Woran man den Fehlschlag erkennt, bevor er Credits kostet:** In der leeren
Kachel steht kein Bild. Wer sie stehen laesst, generiert ohne Vorlage und
bekommt eine Bildwelt, die nur ueber den Prompt zusammenhaengt.

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

## Nachtrag 31.08.2026 — Andis drei Spots und der Paragraphenwald

**Vierundfünfzig Erzeugnisse an einem Tag — GESICHERT am 31.08.2026.**

| | Anzahl | Credits |
|---|---|---|
| Startbilder | 36 | 64 |
| Clips (Kling 3.0, 1080p, Ton aus) | 18 | 157,5 |
| **gesamt** | **54** | **~222** |

Guthaben danach: **253 von 1000**, am Konto abgelesen.

**Am Nachmittag kamen drei weitere Runden dazu** — der neu gebaute Stempel für
Spot 2A, Franz' Paragraphen-Slalom und die Abfahrtshocke. Stand nach allem:

| | lokal | Seitenleiste |
|---|---|---|
| `bilder/` | **149** | Image 149 |
| `videos/` | **75** | Video 75 |
| `audio/` | 38 | (113 = 75 Tonspuren + 38 eigene) |

Guthaben am Ende: **103 von 1000**.

Dazu kam am Abend noch **Spot 6, der Schalter** — Franz' dritte Idee: ein Paket
voller Paragraphen wird abgewiesen, eine dritte Hand sammelt die Paragraphen zu
einem Etikett, und dann wird es angenommen.

Neuer Bestand nach der ersten Sicherung war `bilder/` **122** · `videos/` **64** ·
`audio/` **38**. Die beiden ersten Zahlen waren **exakt die Sollzahlen der
Seitenleiste** (Image 122 · Video 64) — damit ist der Bestand nachweislich
vollständig. Die 190,9 MB der 54
neuen Dateien sind bitweise geprüft: alle mp4 tragen `ftyp isom`, alle achtzehn
Clips messen 5,04 s bei 1076×1924 und haben keine Tonspur.

⚠ **Die Dateinamen tragen UTC, nicht Bangkok.** Alles, was an diesem Vormittag in
Thailand entstanden ist, heißt `hf_20260830_2…` — es gibt **kein einziges**
`hf_20260831_`. Wer nach dem Kalendertag sucht, findet nichts und hält den Tag
für ungesichert. **Der verlässliche Abgleich läuft gegen den lokalen Bestand,
nicht gegen das Datum.**

⚠ **Der Stichtag ist der 01.09.2026, nicht der 02.** Die Einstellungsseite sagt
*„Subscription active until September 1, 2026"*; das rote Band im Seitenkopf sagt
„Plan ends in 2 days" und ist **falsch herum gerundet**. Wer sich auf das Band
verlässt, verliert einen Tag.

Was gerendert wurde: **Andis drei Spots** (The Missing Number · Valid Isn't
Accepted · Yours to Sign, je zwei bis drei Einstellungen) und **Franz' eigene
Idee, der Paragraphenwald** — ein Mann von hinten mit einem Paket vor einem Wald
aus §-förmigen Stämmen, die zurückweichen, während die Szene in Sommer kippt.
Alle Prompts und der Montageplan stehen in `spots-andi-2026-08-31.md`.

**Drei Handgriffe, die dort ausführlich stehen und Zeit kosten, wenn man sie
nicht kennt:** die Vollansicht blättert mit den Pfeiltasten; `Create Video` hält
1080p/Ton-aus nur ohne Seiten-Neuladen (danach wieder 720p mit Ton, 10 statt
8,75 Credits); und das Fenster „ORGANIZE. SHARE. CREATE TOGETHER" kommt bei jeder
Navigation und schluckt auch Scroll-Befehle.

**Und eine Korrektur an der Schrift-Regel:** sie gilt für *Sätze*. Ein einzelnes
englisches Wort in einer Oberfläche sitzt — ein Startbild trägt die
Spaltenüberschrift `WEIGHT` fehlerfrei.

### Der Sicherungsweg vom 31.08. — schneller als der Sammel-Download

Nicht über die Galerie-Auswahl (die hat die Nachlade-Falle), sondern über die
**Kennungen**:

1. `higgsfield.ai/asset/all` öffnen. Die Kachel-Vorschauen tragen den vollen
   Dateinamen: `<user>/hf_JJJJMMTT_hhmmss_<uuid>_thumbnail.webp`.
2. Im **Scroll-Container** (nicht am Fenster! die Seite scrollt in einem inneren
   `div`) schrittweise nach unten fahren und die Namen laufend in ein `Set`
   sammeln — die Galerie ist virtualisiert, weggescrollte Kacheln verschwinden
   aus dem DOM.
3. Gegen den lokalen Bestand differenzieren.
4. Holen von **`https://d8j0ntlcm91z4.cloudfront.net/<user>/<name>.<png|mp4>`** —
   Endung per HEAD bestimmen (200 = Treffer, 403 = falsche Endung).

Kontonummer: `user_3HIukLfgZm9qTyEUt1mm9SQyutP`.

⚠ **`cdn.higgsfield.ai` liefert NICHT aus** — jede Anfrage dort endet auf 404,
obwohl die Vorschaubilder über diesen Namen laufen. Nur der CloudFront-Name
trägt. Das kostet eine Viertelstunde, wenn man es nicht weiß.

**Die Zahl der gefundenen Kennungen muss Image + Video der Seitenleiste
ergeben** (186 = 122 + 64). Audio-Erzeugnisse haben keine Bildvorschau und
fehlen in dieser Liste — das ist richtig so, nicht unvollständig.

## Stand des Abos (30.08.2026): gekündigt

Die Abo-Seite sagt **„Subscription cancelled. You won't be billed again"** — es
verlängert sich am 01.09. also **nicht** mehr (Todo **#590**: die Ausgabenzeile
in MyTM fällt damit weg statt zu steigen). Restguthaben laut Seite: **576 von
1000**, vor den Läufen dieses Tages; davon sind 8 für die vier Bilder und 8,75
für den Spot weggegangen.

Der ganze Tag hat **93 Credits** gekostet: sieben Clips à 8,75 und vier
Bildläufe à 8. Rest also rund **483**.

**Was übrig ist, verfällt zum Periodenende.** Bei 8,75 Credits je Clip
(1080p, Ton aus — nicht die alten 55, die aus einem 4K-Lauf stammten) stecken
darin noch rund **60 Clips**. Das ist der eigentliche Inhalt von Todo **#642**:
nicht *ob* noch Clips gehen, sondern welche vor dem Stichtag noch entstehen
sollen. **Bei diesem Verhältnis ist Rendern billiger als Überlegen** — beim
zweiten Lauf sind deshalb gleich zwei Fassungen entstanden statt einer
Entscheidung am Standbild.
