# Higgsfield — Prompt-Bibliothek

> Stand: 01.08.2026 · Der Punkt §0.4 aus `plan-higgsfield-monat.md`.
> Alles hier ist **vor** dem Abo geschrieben — im bezahlten Monat wird nur noch
> generiert, nicht mehr überlegt.

## Wie diese Datei benutzt wird

1. **Erst Bilder, dann Video.** Ein Soul-2.0-Bild kostet 0,125 Credits, ein
   Seedance-Video rund 18. Jede Motivsuche — Raum, Licht, Figur, Bildausschnitt —
   passiert auf Bildebene. Erst wenn das Standbild sitzt, wird daraus ein Video
   (Bild als Startframe). Das drückt 3–5 Videoversuche je Shot auf 1–2.
2. **Kontinuität kommt aus dem Startframe**, nicht aus dem Prompt. Der letzte
   Frame eines Clips ist der Startframe des nächsten, wenn derselbe Raum
   wiederkommt.
3. **Roh ist nicht fertig.** Text, Marke, Ton und Abspann kommen lokal dazu
   (`werbung/poolservice/clip.py` als Muster).

## Bausteine

**MARKE** (an jeden Bildprompt anhängen)
```
cinematic, natural light, warm late-afternoon tropical light, shallow depth of
field, realistic skin texture, muted natural colors, no on-screen text
```

**NEGATIV** (immer)
```
no text, no captions, no subtitles, no logos, no watermark, no distorted hands,
no extra fingers, no warped faces, no plastic skin, no oversaturation
```

**Warum kein Text im Bild:** die Modelle schreiben Kauderwelsch, und die Aussage
soll ohnehin lokal eingebrannt werden — DE und EN teilen sich dieselbe Bildspur
(§5 des Plans, halbiert die Menge).

---

## Clip „Alle sind draußen. Du nicht." (Eyecatcher, produktunabhängig)

Zweck: Aufmerksamkeit in der Gruppe, kein Produktbeweis. Läuft neben den
Produkt-Clips, nicht statt ihnen. Enthält bewusst **nichts, was altert** —
keine Preise, keine Bausteinnamen, keine Screenshots.

Länge 15 s (3 × 5 s), 4:5.

### Shot 1 — das Büro (Bild zuerst)

```
Interior of a small cluttered back office in a tropical beach town, late
afternoon. A middle-aged man in a white tank top sits hunched over a desk
covered with stacks of paper, invoices and receipts, an old desktop PC, one dim
desk lamp, blinds almost closed. Behind him an open doorway shows a bright
sunlit beach bar, blown out warm daylight, people relaxing in the distance.
Strong contrast between the dark room and the bright doorway. Camera at desk
height, slightly behind him.
```
Video daraus: **langsam heranfahren** (slow push in). Er sieht kurz zur Tür,
dann wieder auf die Papiere.

### Shot 2 — der Rausschmiss (ohne dass jemand zu sehen ist)

```
Same cluttered office, identical camera position. A forearm in a rolled-up
light blue shirt sleeve enters the frame from the right and sweeps the stacks
of paper off the desk in one motion, then points toward the open sunlit
doorway. Only the arm and hand are visible, the person stays out of frame. The
seated man looks up. Locked-off camera.
```
Der Absender bleibt aus dem Bild und wird erst im Abspann aufgelöst. Das spart
die Charakter-Konsistenz und ist stärker als eine gezeigte Figur.

*Sparfassung:* Dieser Shot lässt sich durch einen harten Schnitt plus Textkarte
ersetzen — spart rund ein Drittel der Credits des ganzen Clips.

### Shot 3 — hinaus (eine Fahrt, kein Schnitt)

```
The same office, now empty and tidy: clean desk, one screen glowing with a
simple weekly schedule, chair pushed in, door wide open. The camera dollies
forward through the doorway and out to a beach bar, where the same man in the
white tank top sits with his back to the camera, a cocktail in front of him,
other guests around, sea and late afternoon sun ahead. One continuous move, no
cut.
```
Ihn von hinten zu zeigen ist Absicht: ohne Soul ID hält das Modell sein Gesicht
zwischen zwei Clips nicht stabil — von hinten fällt das nicht auf.

**Hinweis zum Filter:** Badebekleidung ausdrücklich zu benennen lässt Läufe
häufiger am Inhaltsfilter scheitern, und abgelehnte Läufe kosten trotzdem.
„beach bar, other guests, cocktail" liefert dieselbe Atmosphäre zuverlässig.

### Text (lokal eingebrannt, nicht generiert)

| Shot | DE | EN |
|---|---|---|
| 1 | Alle sind draußen. Du nicht. | Everyone's outside. You're not. |
| 2 | Das muss nicht so sein. | It doesn't have to be. |
| 3 | Ich zeige dir den Weg. · ki-lotse.tech | Let me show you the way. · ki-lotse.tech |

Abspann wie gehabt: Kompass-Logo weiß, Avatar rund, `ki-lotse.tech`.

---

## Clip „Das graue Café wird bunt" (Motiv 7, produktunabhängig)

Zweck: Franz' eigenes Bild aus `project_positionierung_lotse` — der Betrieb
ändert sich nicht, nur seine Last. Wie der Eyecatcher **ohne Produktbeweis und
ohne alternde Aussage**: kein Screenshot, kein Preis, kein Bausteinname.

Länge 15 s (3 × 5 s), 4:5. Ablage `roh/02-cafe/`.

### Die Regel, an der dieser Clip hängt

**Alle drei Shots kommen aus EINEM Standbild.** Der ganze Clip behauptet, es sei
dasselbe Café — sobald das Modell für die bunte Fassung einen eigenen Raum
erfindet, ist die Aussage weg und der Zuschauer merkt es sofort. Also: das graue
Bild erzeugen, bis es sitzt, und die bunte Fassung **aus diesem Bild** ableiten
(Startframe/Bild-zu-Bild), nicht neu prompten. Genau der Fehler, der beim
Eyecatcher am „aufgeräumten Büro" schon einmal einen Versuch gekostet hat.

**Erster Handgriff: den Soul-ID-Charakter abwählen** (× an der Charakter-Kachel).
Franz ist in diesem Clip nicht der Wirt.

### Shot 1 — grau (das Mutterbild, hier wird gesucht)

```
Interior of a small streetside coffee shop in a Thai coastal town, morning.
A man in his fifties in a dark green apron over a plain grey t-shirt stands
behind a wooden counter, looking down at a thick stack of handwritten receipts
and an open spiral notebook. Espresso machine, chalkboard, ceiling fan. Six
empty tables with mismatched chairs, chairs still stacked on two of them. Large
window to the street on the left, flat overcast daylight, no sun, no one else in
the room. Camera at customer height, five metres back, centred on the counter.
```
**MARKE hier ohne die Lichtzeile** — „warm late-afternoon tropical light" würde
gegen den eigenen Prompt arbeiten. Stattdessen anhängen:
```
cinematic, natural light, shallow depth of field, realistic skin texture,
desaturated cold grey-green tones, no on-screen text
```
Video daraus: **langsam heranfahren** (slow push in). Bewegen darf sich fast
nichts — der Ventilator, ein umgeblätterter Zettel. Mehr nicht.

### Shot 2 — bunt (aus dem Startframe von Shot 1)

```
Same room, same camera position, same man in the same dark green apron and grey
t-shirt behind the same counter. Now late afternoon: warm low sun through the
street window, teal and amber colour, every table taken, guests seen from behind
or from the side with faces turned away or cropped, cups and steam on the
tables, string lights on. The counter is clear — no papers, no notebook. The man
stands upright, hands free, talking to someone out of frame.
```
+ MARKE + NEGATIV.

**Dieselbe Kamerafahrt wie Shot 1, gleiches Tempo.** Die Wiederholung ist der
Clou: erst dadurch liest der Zuschauer den harten Schnitt als Vergleich statt
als neue Szene. Jetzt bewegt sich alles — Gäste, Dampf, Licht. Der
Bewegungsunterschied trägt die Aussage genauso wie die Farbe.

Gäste bewusst nur von hinten oder angeschnitten: Gesichter in der Menge fallen
auseinander, und ein leerer Blick im Hintergrund kippt das ganze Bild.

### Shot 3 — hinaus (eine Fahrt, kein Schnitt)

```
The same coffee shop at dusk, now seen from the street: the camera pulls slowly
backwards out through the open door and across the road, the warm lit interior
glowing through the large window, full tables inside, parked scooters and wet
asphalt in the foreground, deep blue evening sky above. One continuous backward
move, no cut.
```
Aus dem **bunten** Startframe. Findet das Modell nicht nach draußen: eigenes
Außen-Startbild erzeugen — der Bruch fällt hier nicht auf, weil vom Innenraum
nur der Fensterausschnitt zu sehen ist.

Bewusst anders als der Eyecatcher, der nach vorn an die Beach Bar führt. Zwei
Clips mit demselben Schlussbild wären in der Rotation austauschbar.

### Text (lokal eingebrannt, nicht generiert)

| Shot | DE | EN |
|---|---|---|
| 1 | Nicht das Café ist müde. | It's not the café that's tired. |
| 2 | Gleicher Raum. Keine Zettel mehr. | Same room. No more paperwork. |
| 3 | Und der Abend gehört dir. | And the evening is yours. |

Der Clip nennt die Lösung nicht — das tut der Abspann („KI & Automatisierung für
kleine Betriebe"). Ein Image-Clip, der zusätzlich erklärt, wird zu keinem von
beidem.

### Credit-Rechnung — tatsächlich: **0**

Gebaut am 01.08.2026, drei Bilder und drei Videos, **ohne einen einzigen
Credit**. Wie das geht, steht unten unter „Der Gratisweg".

---

## Clip „Der Beweis" (Betriebsart Poolservice, Motiv 8)

Zweck: Aufmerksamkeit für die **Direktansprache** an Pool-Service-Betriebe.

**Er ersetzt `werbung/poolservice/` nicht.** Der dortige Clip ist der
Beweis-Clip — echte Screenshots der laufenden Demo, fünf Szenen, DE und EN. Was
ihm fehlt, sind die ersten drei Sekunden: er beginnt mit zwei Textkacheln. Der
hier beginnt mit einem Bild. Reihenfolge in der Ansprache: **erst dieser, dann
der andere**, wenn Interesse da ist.

Länge 15 s (3 × 5 s), 4:5. Ablage `roh/03-pool/`.

Wie beim Café gilt: **Shot 2 kommt aus dem Startframe von Shot 1.** Der Vorwurf
und der Beweis müssen sichtbar derselbe Pool sein, sonst beweist das Bild nichts.
Kein Soul ID (der Techniker ist nicht Franz), keine sichtbaren Gesichter.

### Shot 1 — der Vorwurf (das Mutterbild)

```
A private villa swimming pool in tropical Thailand at midday, seen from the
pool deck. Perfectly clean turquoise water, still surface, two empty sun
loungers, palm shadows on the tiles, a low white villa wall behind, nobody in
the frame. Hard bright midday sun, high contrast, saturated blue. Camera low at
deck height, looking across the water. Cinematic, shallow depth of field,
no on-screen text, no logos, no watermark.
```
Video: **sehr langsame Fahrt über das Wasser**, Licht glitzert, ein Palmenschatten
wandert. Sonst nichts. Die Leere ist der Vorwurf.

### Shot 2 — der Beweis (aus dem Startframe von Shot 1)

```
Same pool, same villa, same time of day, same camera position. Now a pool
service technician in a plain dark blue polo shirt and a cap kneels at the near
edge of the pool, seen from behind and slightly to the side, his face not
visible. He holds a phone up in both hands, photographing the clean water in
front of him. A telescopic pool net and a small test kit lie on the tiles beside
him. Cinematic, shallow depth of field, no on-screen text, no logos, no watermark.
```
Video: er hebt das Telefon, tippt einmal ab; die Kamera bleibt stehen. Dass die
Kamera hier **nicht** fährt, ist Absicht — Shot 1 bewegt sich, Shot 2 hält still.
Das macht den Beweis zum ruhenden Pol.

### Shot 3 — erledigt

```
A white pickup truck with pool cleaning equipment in the back drives slowly
away from the camera down a narrow Thai residential soi at dusk, villa walls and
palms on both sides, warm street lights coming on, wet asphalt, deep blue evening
sky. The camera stays on the road as the truck gets smaller. One continuous
shot, no cut. Cinematic, no on-screen text, no logos, no watermark.
```

### Text (lokal eingebrannt, nicht generiert)

| Shot | DE | EN |
|---|---|---|
| 1 | »Ihr wart letzte Woche nicht da.« | "You weren't here last week." |
| 2 | Doch. Foto, Datum, Name. | Yes we were. Photo, date, name. |
| 3 | Diskussion beendet. | Argument over. |

„Foto, Datum, Name" ist **keine erfundene Oberfläche**: seit `wartung` v1.1.0
hängen genau diese drei Angaben am erledigten Einsatz. Wer mehr behauptet, als
der Beweis-Clip danach zeigen kann, verliert im zweiten Schritt.

**Kein Kundenname.** Strodos gehört ins Gespräch, nicht in eine Datei, die
weitergeleitet wird — dieselbe Regel wie in `werbung/poolservice/skript.md`.

---

## Clip „Der Lotse" (Markenfilm, Motiv 1)

Zweck: der Markenfilm. Er erklärt nicht, was Franz verkauft, sondern **welche
Rolle er einnimmt** — und beantwortet damit stumm den häufigsten Einwand:
„Übernimmt mir da einer mein Geschäft?" Nein. Der Lotse geht wieder von Bord.

Er ist der haltbarste Clip der Halde: **kein Gesicht, kein Screenshot, kein
Preis, kein Bausteinname.** Nichts darin kann veralten, also ist er alle paar
Wochen wieder postbar, während die Betriebsart-Clips rotieren müssen.

Länge 15 s (3 × 5 s), 4:5. Ablage `roh/04-lotse/`.

### Zwei Vorentscheidungen, die hier begründet werden

**Das Firefly-Schiff wird NICHT wiederverwendet** (geprüft 01.08.2026).
`Franz/Logos/Firefly *.mp4` ist nicht die Aufnahme einer Reede, sondern die
Titelkarte des Werbevideos #160: eine gezeichnete Galeone auf einer stilisierten
Weltkarte, 16:9, mit eingebranntem deutschem Text. Illustrationsstil statt Foto,
Text im Bild (bricht die gemeinsame Bildspur für DE und EN), und im
4:5-Beschnitt bleibt von der Karte nichts. `ideen.md` behauptete das Gegenteil —
Annahme, nicht Befund.

**Shot 3 zeigt keinen Bildschirm.** Die Idee sah „Schnitt auf einen echten
Bildschirm" vor. Dagegen sprechen drei Dinge: ein Screenshot altert und nimmt
dem Clip genau die Eigenschaft, wegen der er gebaut wird; er zwingt die
`shots.py`-Kette in einen Markenfilm; und ein 1400 × 875 breites Dashboard wird
im 4:5-Rahmen zur Briefmarke. Stattdessen **führt Shot 3 die Metapher zu Ende**:
das Lotsenboot dreht ab. Den Produktbeweis liefert `werbung/poolservice/`, und
zwar mit echten Oberflächen — dieser Clip muss ihn nicht mitschleppen.

### Die Regel, an der dieser Clip hängt

**Shot 3 kommt aus dem Startframe von Shot 1.** Der ganze Clip behauptet, es sei
dasselbe Schiff in derselben Bucht — nur später und heller. Zweimal „ein
Frachter im Dunst" zu prompten liefert zwei verschiedene Schiffe, und dann geht
niemandem von Bord, sondern es fährt irgendein anderer Frachter weg. Shot 2
(Nahaufnahme der Hände) ist ein Detailschnitt in einem anderen Raum und darf
frisch geprompted werden.

**Erster Handgriff: den Soul-ID-Charakter abwählen** (× an der Charakter-Kachel).
Franz ist hier weder Kapitän noch Lotse.

### Shot 1 — der Frachter im Morgendunst (das Mutterbild, hier wird gesucht)

```
A large cargo ship lying at anchor in a wide bay at dawn, seen from low down on
the water. Thick morning haze, flat pale grey-blue light, the dark hull rising
out of the mist with its outline softened by fog. A small pilot boat with one
white navigation light runs in along the hull from the right, a low bow wave
behind it, tiny against the ship. Calm water, almost no swell, nobody visible.
Camera at water level, wide, the ship filling the left half of the frame.
```
**MARKE hier ohne die Lichtzeile** — „warm late-afternoon tropical light" würde
gegen den eigenen Prompt arbeiten. Stattdessen anhängen:
```
cinematic, natural light, shallow depth of field, cool desaturated blue-grey
tones, no on-screen text
```
+ NEGATIV.

Video daraus: **sehr langsame seitliche Fahrt**, das Lotsenboot schiebt sich am
Rumpf entlang. Sonst bewegt sich fast nichts. `Enhance` abschalten (Falle 5) —
die Reglosigkeit ist der Punkt, das Wasser soll nicht anfangen zu schäumen.

### Shot 2 — die Hände am Steuerrad (frisch, anderer Raum)

```
Close-up of a pair of weathered, sun-darkened hands resting on the wooden spokes
of a ship's helm, seen from behind and slightly above, the person's face and body
out of frame. Worn brass fittings, salt-dulled varnish on the wood. Beyond the
helm, a blurred grey-blue dawn sea through a wheelhouse window. The hands sharp,
the sea soft. Overcast dawn light.
```
+ MARKE (ohne Lichtzeile, wie oben) + NEGATIV.

Video: die Hände korrigieren **einmal** um wenige Grad, dann Ruhe. Kamera steht.
Dass hier nichts fährt, ist Absicht — Shot 1 bewegt sich, Shot 2 hält still,
Shot 3 fährt wieder. Der Ruhepunkt liegt auf dem Satz, der die Aussage trägt.

Kein Gesicht im Bild: Das erfüllt nebenbei die teuerste Soul-ID-Regel („nie eine
zweite Person mit sichtbarem Gesicht") kostenlos — und Hände altern nicht.

### Shot 3 — der Lotse geht von Bord (aus dem Startframe von Shot 1)

```
Same bay, same cargo ship, same camera position at water level. The haze has
lifted, clear pale morning light, the hull now fully visible and under way with
a bow wave building. The small pilot boat turns away from the ship and runs back
towards the open water on the right, its wake curving behind it, getting smaller.
Nobody visible on either boat. One continuous shot, no cut.
```
+ MARKE (ohne Lichtzeile) + NEGATIV.

Findet das Modell aus dem Startframe nicht in die Weiterfahrt: nicht neu
prompten, sondern das **Bild** aus Shot 1 aufhellen lassen (Bild-zu-Bild:
„haze lifted, clear morning light, ship under way") und daraus das Video ziehen.
Der Weg über ein frisches Außenbild ist hier ausdrücklich **nicht** erlaubt —
anders als beim Café, wo vom Innenraum nur der Fensterausschnitt zu sehen war.
Hier ist das Schiff das ganze Bild, ein zweites fällt sofort auf.

### Text (lokal eingebrannt, nicht generiert)

| Shot | DE | EN |
|---|---|---|
| 1 | Der Lotse steuert dein Schiff nicht. | A pilot doesn't steer your ship. |
| 2 | Er kennt die Untiefen. | He knows where the rocks are. |
| 3 | Du bleibst am Steuer. Ich kenne den Weg. | You stay at the wheel. I know the way. |

Der Schlusssatz ist bewusst **nicht** „Ich zeige dir den Weg" wie beim
Eyecatcher: zwei Clips mit demselben Schlussbild und demselben Schlusssatz sind
in der Rotation austauschbar. „Du bleibst am Steuer" sagt zusätzlich etwas, das
sonst nirgends im Material steht — der Kunde gibt nichts aus der Hand.

**Umbrüche stehen von Hand** (`\n` im `CLIPS`-Eintrag). Der automatische
Zeilenumbruch ist gierig und schob „nicht." bzw. „ship." / „are." als Waise in
die zweite Zeile — beim ersten Satz hängt genau an der Verneinung die Aussage.

### Gebaut am 01.08.2026 — **0 Credits**, drei Bilder, drei Videos, kein Fehlschlag

Ergebnis: `fertig/04-lotse-{de,en}-4x5.mp4`, je 18,0 s, 1080 × 1350.

**Die Startframe-Regel hat sich selbst bewiesen:** Auf dem Rumpf steht in Shot 1
*und* in Shot 3 derselbe Schiffsname — *MV Sea Protector*. Es ist nachweislich
dasselbe Schiff, obwohl Nebel und Licht völlig verschieden sind. Genau das hätte
ein zweiter Prompt nicht geliefert.

Zwei Abweichungen vom Prompt, beide zum Besseren übernommen: Shot 1 steht
bugvoraus und mittig statt „linke Bildhälfte", und die Kamera liegt etwas höher
als Wasserlinie. Der Bug wirkt so wuchtiger. Shot 3 wechselte auf eine
Dreiviertelansicht — der Schnitt liest sich dadurch als Zeitsprung, was er sein
soll.

---

## Clip „Zwei Uhren" (Feierabend, produktunabhängig)

Zweck: Er verkauft **nicht Software, sondern Feierabend**. Der wundeste Punkt bei
Leuten, die zum Leben nach Thailand gegangen sind und dann im Laden festsitzen —
und der einzige aus dem Vorrat, der ohne ein einziges Produktwort auskommt.

Wie Eyecatcher, Café und Lotse **ohne Produktbeweis und ohne alternde Aussage**:
kein Screenshot, kein Preis, kein Bausteinname. Eine Uhrzeit altert nicht.

Länge 15 s (3 × 5 s) + Abspann = 18 s, 4:5. Ablage `roh/05-uhren/`.

**Erster Handgriff: den Soul-ID-Charakter abwählen** (× an der Charakter-Kachel).
Der Ladenbesitzer ist nicht Franz.

### Die Mechanik — der Titel ist die ganze Aussage

**Dieselbe Uhrzeit, zwei Ausgänge.** Shot 1: der Laden ist zu, und er setzt sich
noch einmal an den Rechner. Shot 2: dieselbe Uhr, derselbe Zeigerstand — er
klappt zu und geht. Der Vergleich muss der Zuschauer **sehen**, nicht lesen; der
eingebrannte Text bestätigt ihn nur.

Der Farbbogen trägt mit: **kalt → warm.** Shot 1 und 2 liegen im blaugrünen
Neonlicht von der Straße, Shot 3 in einer warmen Glühbirne. Das Café macht
grau → bunt mit der Farbe, dieser Clip macht dasselbe mit dem Licht — und mit
der Zeit, die stehen bleibt.

### Die Regel, an der dieser Clip hängt

**Shot 1 und Shot 2 kommen aus DEMSELBEN Standbild — nicht nur aus demselben
Startframe, sondern aus derselben Datei.** Erzeugt wird ein einziges Mutterbild,
und daraus werden **zwei Videos mit verschiedenen Prompts** gezogen. Damit ist
die Kontinuität nicht wahrscheinlich, sondern zwingend: gleicher Raum, gleiche
Kamera, gleiches Hemd — und vor allem **derselbe Zeigerstand**, weil es
physisch dieselben Pixel sind.

Das nimmt der Uhr ihre Unzuverlässigkeit ab. Videomodelle malen Zifferblätter
gern zu Kauderwelsch; hier ist das gleichgültig, denn verlangt ist nicht
**lesbar**, sondern **gleich**. Genau deshalb steht im Bildprompt „tick marks
instead of numbers" — Striche verunglücken, Ziffern verunglücken sichtbar.

Zwei Bilder zu erzeugen (eines sitzend, eines stehend) wäre der teurere und
schlechtere Weg: Bild-zu-Bild verschiebt bei einer geänderten Körperhaltung
gern auch die Zeiger, und dann ist der Titel widerlegt.

**Nur der Mensch ändert sich.** Licht, Lampe und Kamera bleiben in Shot 2
unangetastet — jede weitere Abweichung gäbe dem Zuschauer eine zweite Variable
und schwächt den Vergleich. Einzige Ausnahme: der Bildschirm geht aus. Das ist
keine Störung, sondern die Handlung.

### Shot 1 — noch einmal hinsetzen (das Mutterbild, hier wird gesucht)

```
Interior of a small shop in a Thai side street at night, seen from the shop
floor. Metal shelves with goods on both sides, the roller shutter at the front
half down, the shop lights already switched off. At the back a cluttered desk
with an open laptop, a receipt spike and a stack of order slips. A man in his
fifties in a plain faded blue short-sleeved shirt sits at the desk in front of
the laptop, the screen lighting his face from below. One warm desk lamp,
everything else lit only by cold blue-green neon spilling in from the street
through the gap under the shutter. On the wall beside the desk a plain round
analogue wall clock, simple hands, tick marks instead of numbers, clearly
visible. Nobody else in the shop. Camera at standing height, six metres back,
centred on the desk.
```
**MARKE hier ohne die Lichtzeile** — „warm late-afternoon tropical light" würde
gegen den eigenen Prompt arbeiten. Stattdessen anhängen:
```
cinematic, natural light, shallow depth of field, realistic skin texture,
cold blue-green night tones with one warm lamp, no on-screen text
```
+ NEGATIV.

Video daraus: **langsam heranfahren** (slow push in). Er tippt, sieht auf den
Schirm, sonst bewegt sich fast nichts. `Enhance` abschalten (Falle 5).

### Shot 2 — dieselbe Uhr (aus DEMSELBEN Bild, anderer Videoprompt)

```
Same shop, same desk, same man, same light. He closes the laptop, pushes the
chair back, stands up and steps out of frame to the right, leaving the empty
chair and the dark laptop behind. The wall clock does not move. Camera pushes
in slowly, exactly as before.
```

**Dieselbe Kamerafahrt wie Shot 1, gleiches Tempo.** Dieselbe Begründung wie
beim Café: erst die Wiederholung liest sich als Vergleich statt als neue Szene.
Hier ist sie nicht Kür, sondern Pflicht — der ganze Clip behauptet, es sei
derselbe Augenblick.

**Der Schluss des Shots ist die Pointe:** der leere Stuhl. Die Montage kürzt
vorne, das Ende überlebt also — genau richtig.

*Wenn Kling die ganze Handlung nicht in fünf Sekunden schafft:* Aufstehen allein
genügt. Der eingebrannte Satz sagt „Du gehst"; das Bild muss es nicht
zu Ende erzählen. Erst wenn er **sitzen bleibt**, ist der Versuch unbrauchbar.

### Shot 3 — davor (frisch, anderer Raum)

```
A small shop front in a Thai side street at night, seen from across the road.
The roller shutter is down and the shop behind it is dark. On the pavement in
front of it a man in his fifties in a plain faded blue short-sleeved shirt sits
on a plastic chair at a small folding table with a bottle and a glass, seen from
behind and slightly to the side, his face not visible, looking down the street.
A warm bulb hangs over his table, string lights along the front, scooters parked
at the kerb, wet asphalt. Further down the road a bright cold blue-white shop
sign. Deep blue night sky. Camera at standing height, across the road, locked
off, not moving.
```
+ MARKE (ohne Lichtzeile, wie oben) + NEGATIV.

**Das Hemd steht in beiden Prompts ausdrücklich mit Farbe drin** („plain faded
blue short-sleeved shirt"). Shot 3 wird frisch geprompted, das Modell hält also
nichts von selbst — die Regel „Kleidung ausdrücklich vorgeben" aus dem Soul-ID-
Test gilt hier ohne Soul ID genauso, nur trägt sie diesmal die Kontinuität.

**Von hinten, kein Gesicht.** Derselbe Kniff wie im Eyecatcher: über zwei
verschiedene Prompts hält kein Modell ein Gesicht, von hinten fällt es nicht auf.

**Die Kamera steht.** Der Eyecatcher fährt am Ende vor, das Café zurück, der
Poolservice lässt einen Pickup wegfahren, der Lotse ein Boot abdrehen. Ein
fünfter Clip, der zum Schluss wieder etwas wegfahren lässt, wäre in der Rotation
austauschbar. Hier kommt niemand weg — er ist **da**, und das ist der Punkt.

Aus demselben Grund ist der Schlussort **nicht** die Beach Bar: die gehört dem
Eyecatcher. Er sitzt vor seinem eigenen, geschlossenen Laden. Der Ort hat sich
nicht geändert, nur sein Verhältnis dazu — dasselbe Leitmotiv wie beim Café,
aber ein anderes Bild.

### Text (lokal eingebrannt, nicht generiert)

| Shot | DE | EN |
|---|---|---|
| 1 | 3 Uhr früh. Und du sitzt noch da. | 3 a.m. You're still at the desk. |
| 2 | Gleiche Uhrzeit. Du gehst. | Same time. You're leaving. |
| 3 | Dafür bist du hergekommen. | This is what you came for. |

Die Uhrzeit steht im Text, damit die Aussage auch dann trägt, wenn das Modell
das Zifferblatt verunglückt — und sie **richtet sich nach dem Bild, nicht
umgekehrt**. Geplant war 23:40; das Modell hat die Zeiger auf 3 Uhr gestellt,
also heißt es 3 Uhr. Ein Zuschauer, der die Uhr liest, hätte den Widerspruch
sonst gesehen, und die ganze Mechanik des Clips lädt ihn ausdrücklich dazu ein,
genau dorthin zu schauen. 3 Uhr früh ist obendrein das härtere Bild.

Der Schlusssatz nennt weder Lösung noch Werkzeug. „Dafür bist du hergekommen"
ist der einzige Satz im ganzen Material, der den Zuschauer bei seinem eigenen
Grund packt, hier zu sein — und er altert nie. Was verkauft wird, sagt der
Abspann.

**Umbrüche stehen von Hand** (`\n` im `CLIPS`-Eintrag), Lehre aus „Der Lotse".

### Gebaut am 02.08.2026 — **0 Credits**, zwei Bilder, drei Videos, kein Fehlschlag

Ergebnis: `fertig/05-uhren-{de,en}-4x5.mp4`, je 18,0 s, 1080 × 1350.

**Die Ein-Bild-Regel hat sich belegt, und zwar messbar.** Aus dem Schlussbild
beider Shots geschnitten und nebeneinandergelegt: Minutenzeiger auf 12,
Stundenzeiger auf 3 — in beiden identisch, obwohl der eine Shot den Mann am
Schirm zeigt und der andere den leeren Stuhl. Zwei getrennt erzeugte Bilder
hätten das nicht geliefert; ein per Bild-zu-Bild abgeleitetes zweites Bild
vermutlich auch nicht.

**Das Zifferblatt ist Kauderwelsch** — statt der 9 steht eine 0, die 5 ist
doppelt. Belanglos, und genau der Grund, warum im Bildprompt „tick marks instead
of numbers" steht (das Modell hat sich nicht daran gehalten). Verlangt war
**gleich**, nicht **lesbar**, und gleich ist es.

**Der Text musste dem Bild folgen, nicht umgekehrt.** Geplant war 23:40, das
Modell stellte die Uhr auf 3. Da die Mechanik des Clips den Zuschauer
ausdrücklich auffordert, auf die Uhr zu sehen, wäre der Widerspruch aufgefallen.
Also heißt es jetzt „3 Uhr früh" — und das ist obendrein das härtere Bild.

**Zwei Abweichungen vom Prompt, beide übernommen:** Der Laden wurde ein
Ersatzteil-/Kramladen mit tiefen Regalen statt eines Minimarkts — die Regalflucht
gibt der Heranfahrt mehr Tiefe, als der Prompt verlangt hatte. Und Shot 2 fährt
etwas weniger weit heran als Shot 1; im Schnitt liest sich das nicht als Fehler,
weil Raum, Licht und Uhr identisch bleiben.

**Am Werkzeug abgelesen (zusätzlich zu den zwölf bekannten Fallen):**

13. **`Turn to video` schlägt oft fehl und schließt nur das Fenster.** Zwei von
    drei Versuchen taten gar nichts. Was hilft: die Kachel in der **Mitte**
    anklicken (an den Rändern liegen Herz/Download/`…`), volle acht bis zehn
    Sekunden warten, bis das Fenster wirklich steht, und den Knopf dann über
    sein Element ansteuern statt über eine Bildschirmposition.
14. **Ein zweites Video aus demselben Bild braucht `Turn to video` gar nicht.**
    Nach dem ersten Generate bleibt das Startbild im Formular stehen — Prompt
    ersetzen, Unlimited prüfen, nochmal Generate. Genau so sind Shot 1 und 2
    entstanden, und das ist der bequemste Weg zur Ein-Bild-Regel.
15. **Läufe überlappen wirklich.** Zwei Videos und ein Bild liefen gleichzeitig,
    rund 3–4 Minuten je Video. Wer seriell wartet, verschenkt die Hälfte der Zeit.
16. **Das Startbild lässt sich im Formular nicht tauschen** (ergänzt Falle 4):
    Ein Klick auf das vorhandene Vorschaubild öffnet nur eine Großansicht, keinen
    Bildwähler.
17. **Die Datei-Adresse lässt sich nicht erraten.** `…_thumbnail.webp` durch
    `.mp4` zu ersetzen liefert 404. Der Download-Knopf an der Kachel (erscheint
    beim Überfahren) legt sie als `hf_<datum>_<zeit>_<uuid>.mp4` im
    Downloads-Ordner ab; von dort umbenennen nach `roh/<clip>/`.

---

## Clip „Die gute Fee" (MyPro, Motiv 6)

> ⚠ **Dieser Clip gehört nicht zu KI-Lotse.** Er ist für die **gemeinsame Firma
> mit Andi**, und die hat noch keinen Namen und kein Erscheinungsbild. Alles
> Markenhafte darin ist **Platzhalter zu Demozwecken**: der grüne Grund, das
> Kompass-Logo, der Avatar, `ki-lotse.tech` im Abspann und im Sprechtext von
> Shot 3. Wird der Clip wirklich verwendet, **wird der Abspann komplett neu
> gemacht** — das Erscheinungsbild überlegt sich Andi.
>
> **Nicht in die KI-Lotse-Rotation stellen.** Er verkauft nicht KI-Lotse.

Zweck: MyPro verkaufen, ohne die Oberfläche zu zeigen. Das verstaubte Büro ist
die Betriebsart-freie Fassung von „veraltete Software" — sie passt auf jeden
Betrieb und altert nicht.

Länge 18 s (3 × 5 s + Abspann), 4:5. **Der erste Clip, der bewusst Credits
ausgibt** — Begründung unten.

### Die Regel, an der dieser Clip hängt

**Der Zauberstab wechselt die Hand.** Eine Fee, die hereinfliegt, alles richtet
und wieder geht, sagt stumm gesehen: *ein anderer macht das für dich.* Genau das
ist MyPro nicht — dort baut der Kunde selbst, mit seinem eigenen KI-Abo. Also
bringt die Fee den Stab, gibt ihn ab, und **der Mann schwingt ihn selbst**. Erst
dann stimmt das Bild mit dem Satz überein, und erst dann funktioniert der Clip
ohne Ton.

Damit steht die Fee in derselben Figur wie der Lotse: sie kommt an Bord, macht
ihre Arbeit und geht wieder von Bord. Der Kunde gibt nichts aus der Hand.

**Der Raumwechsel ist hier ausdrücklich erlaubt** — anders als beim Eyecatcher
und beim Lotsen. Dort behauptete der Clip, es sei derselbe Raum bzw. dasselbe
Schiff, deshalb war ein neu generierter Raum ein Fehler. Hier ist die Verwandlung
die Aussage: aus dem engen Kabuff wird ein heller Raum mit großer Fensterfront.
Was zusammenbleiben muss, ist nicht die Einrichtung, sondern **der Mann und die
Kameraposition** — und die kommen aus der Startframe-Kette.

**Die Kette:** Mutterbild A → Shot 1. Letzter Frame von Shot 1 → Shot 2. Letzter
Frame von Shot 2 → Shot 3. Das ist Regel 2 dieser Datei, hier zum ersten Mal über
drei Glieder. Frame herausziehen geht lokal:

```
ffmpeg -sseof -0.1 -i roh/06-fee/01-grab.mp4 -frames:v 1 -q:v 2 roh/06-fee/frame-01.png
```

**Erster Handgriff: den Soul-ID-Charakter abwählen** (× an der Charakter-Kachel).
Der Mann am Schreibtisch ist der Kunde, nicht Franz — mit stehendem Charakter
trägt er Franz' Gesicht, und dann sitzt der Anbieter im eigenen Elend.

### Shot 1 — das Grab (das Mutterbild, hier wird gesucht)

```
A man in his fifties seen from directly behind, sitting at a desk in a cramped
old-fashioned office, shoulders rounded, head slightly lowered. In front of him
a beige CRT monitor from the nineties showing a dense grey spreadsheet, the only
real light source in the room. Dust hanging thick in the air, cobwebs in the
upper corners, stacks of yellowed paper and ring binders along the walls. Behind
him a small window with closed dusty blinds, letting in thin slats of grey light.
Faded brown and grey tones, everything worn and tired. Camera behind the man at
shoulder height, slightly above, the monitor glow filling the centre of the frame.
```
**MARKE hier ohne die Lichtzeile** — „warm late-afternoon tropical light" würde
den ganzen Shot kaputtmachen. Stattdessen anhängen:
```
cinematic, dim available light, shallow depth of field, realistic skin texture,
desaturated brown-grey tones, no on-screen text
```
+ NEGATIV.

Video daraus: **fast reglos**, ein sehr langsames Heranschieben an Rücken und
Bildschirm. Der Staub treibt in den Lichtschlitzen, die Schultern senken sich
einmal mit dem Atem. Sonst bewegt sich nichts. In der letzten Sekunde treibt
**ein kleiner warmer Lichtpunkt oben rechts ins Bild** — das ist der Haken in
den Schnitt. `Enhance` abschalten (Falle 5): die Reglosigkeit ist der Punkt.

### Shot 2 — die Fee bringt den Stab (aus dem letzten Frame von Shot 1)

```
Same office, same camera behind the man. A small winged fairy the size of a hand,
glowing warm gold, flies in from the upper right and comes to rest beside the
man's shoulder, a trail of fine sparks behind her. Where the sparks fall, the
floating dust lights up. She holds out a slender wand towards him and he reaches
for it and takes it. The room is still dark and grey; the fairy and the wand are
the only warm light. One continuous shot, no cut.
```
+ MARKE (ohne Lichtzeile, wie oben) + NEGATIV.

**Das Nehmen ist der teuerste Handgriff des ganzen Clips** und der, an dem die
Aussage hängt. Wenn das Modell die Übergabe nicht bringt, lieber diesen Shot
nachziehen als weiterbauen — ein Clip, in dem der Stab bei der Fee bleibt, sagt
das Gegenteil.

Sparfassung, falls die Übergabe nach drei Anläufen nicht sitzt: Die Fee lässt den
Stab **fallen**, er landet auf dem Schreibtisch, seine Hand kommt ins Bild und
nimmt ihn. Eine fallende Gerade kann jedes Modell, eine Übergabe zwischen zwei
Figuren nicht.

### Shot 3 — die Verwandlung (aus dem letzten Frame von Shot 2)

```
Same office, same camera behind the man, who now holds the wand. He raises it.
The room transforms around him in one continuous movement: the small blinded
window widens into a floor-to-ceiling glass front, sunlight floods in, dust and
cobwebs dissolve, the paper stacks and ring binders disappear, the worn furniture
becomes a clean modern desk in a bright room with plants, the beige CRT becomes a
slim bright screen. Colour returns to everything. The man turns towards the
camera and he is beaming. One continuous shot, no cut.
```
**Hier MARKE mit der Lichtzeile** — dies ist die eine Einstellung im Clip, in die
das warme Licht der Marke gehört. + NEGATIV.

**Den Zoom nicht bekämpfen.** Bild-zu-Video erzwingt eine langsame Hineinfahrt
(Gattungsmerkmal, an Firefly *und* Higgsfield belegt — Rezept A4). Beim
KI-Lotse-Intro war das tödlich, weil dort passgenaue Overlays drüberlagen; hier
arbeitet die Fahrt für den Shot. Also nicht „static camera" prompten und sich
ärgern, sondern die Fahrt einplanen.

**Der Schluss ist die Pointe** — das strahlende Gesicht liegt am Ende der
Bewegung. Beim Kürzen auf 5 s gilt deshalb wie immer: **vorne abschneiden, nicht
hinten** (`max_shot` in `montage.py`).

### Text (lokal eingebrannt, nicht generiert)

| Shot | DE | EN |
|---|---|---|
| 1 | Software von gestern? | Software from yesterday? |
| 2 | Nicht mehr auf dem Stand\nvon heute? | Not where it should be\ntoday? |
| 3 | MyPro ist dein Zauberstab.\nSchwingen musst du ihn. | MyPro is your magic wand.\nYou do the waving. |

Karte und Stimme sagen hier **dasselbe** — die Sätze sind kurz genug zum Lesen
und vollständig genug zum Sprechen. Eine Ausnahme: Im Sprechtext von Shot 3
steht **„DU"** in Großbuchstaben (`sprech_de`), auf der Karte klein.

**Kein KI-Lotse, keine Domain** — weder gesprochen noch geschrieben. Siehe den
Kasten oben: Der Clip gehört der gemeinsamen Firma, nicht KI-Lotse.

### Die drei Textfehler, die diese Fassung ersetzt hat

Die erste Fassung war in beiden Sprachen unbrauchbar. Was dabei gelernt wurde,
gilt für jeden weiteren Clip:

1. **„Now you're the fairy" geht im Englischen nicht.** *Fairy* ist dort auch
   ein Schimpfwort für Schwule; der Satz landet völlig woanders als gemeint.
   **Bei jedem englischen Text die Nebenbedeutung prüfen, nicht nur die
   Übersetzung.**
2. **Die Karten erzählten nach, was man ohnehin sieht.** Man sieht eine Fee, und
   der Text sagte „Fee". Verschenkte Fläche — der Text soll sagen, was das Bild
   *nicht* kann.
3. **„Schwingen musst du ihn selbst" gegen „Schwingen musst DU ihn".** Beide
   sind richtig; ohne Betonung klingt der zweite abgeschnitten, mit
   Kontrastbetonung ist er vollständig. Gewählt wurde der zweite, und zwar aus
   einem Grund, der über den Satz hinausgeht (Franz, 14.08.2026):

   > **„du" ist eine Aufforderung, „selbst" ist eine Einschränkung.**

   Derselbe Sachverhalt, zwei Haltungen: *du* heißt „du darfst", *selbst* heißt
   „dir hilft keiner". Wer Ermächtigung verkauft, darf an der Schlussstelle
   nicht aus Versehen Alleinsein verkaufen.

### Die Stimme kommt nicht von `edge-tts`

**ElevenLabs v3 über Higgsfield**, Stimme „Arthur", die Fee „Juno". Grund:
`edge-tts` hat „veraltete" zu englischem Kauderwelsch verschliffen — dieselbe
Falle wie damals bei „ki-lotse.tech" im Loom-Video, nur diesmal mitten im Wort.

Drei Dinge, die dabei zählen:

- **Die Regieanweisung steht im Skript.** `[disappointed][tired]` auf Shot 1
  und 2, `[cheerful][excited]` auf Shot 3 — der Stimmungsbogen folgt dem Bild
  vom staubigen Büro zum strahlenden Gesicht (Franz' Vorgabe). Eine Stimme, drei
  Haltungen, kein Stimmwechsel.
- **Die Fee ist eine zweite Stimme**, 2,8 s nach Beginn von Shot 2 eingemischt —
  genau dann, wenn sie im Bild an der Schulter steht und nicht mehr nur ein
  Lichtpunkt ist. Gemischt wird **lokal mit ffmpeg** in eine Datei; `montage.py`
  kennt nur eine Sprachdatei je Shot.
- **`montage.py` erzeugt nur, was fehlt.** Fertige MP3s in
  `sprecher/<sprache>/06-fee/` bleiben stehen — deshalb braucht der Weg über
  Higgsfield keine Zeile Code. Wer neu erzeugen will, löscht die Dateien.

Kosten: **0,15 bis 0,3 Credits je Zeile**, acht Zeilen rund 2,25. Sprache ist
damit so billig wie Bilder — die Credit-Frage entscheidet sie nicht.

### Der Abspann bewegt sich — und wird trotzdem nicht generiert

Erster Clip mit **bewegtem Abspann**: „MyPro" blitzt auf, als hätte es der
Zauberstab geschrieben (weißer Schein, Funkenkranz, ein letztes Aufziehen von
88 auf 100 %), danach kommen Satz, Domain und Name nacheinander dazu.

**Das rendert `montage.py` lokal, Bild für Bild mit PIL** — kein Modell kommt
daran. Videomodelle schreiben bei Text Kauderwelsch (Baustein-Regel ganz oben in
dieser Datei), und beim KI-Lotse-Intro hat dieselbe Einsicht schon einmal zum
Selberrendern geführt. Schrift ist Handwerk.

Eingeschaltet wird das über `held` im `CLIPS`-Eintrag; ohne dieses Feld bleibt
alles beim Standbild. **Das ist Absicht:** eine Marke, die bei jedem Post anders
auftritt, ist keine Marke mehr. Der bewegte Abspann gehört den Clips, die ein
**Erzeugnis beim Namen nennen** — die fünf produktfreien behalten die ruhige
Markenfläche. Stellschrauben: `TAKT` (wann was kommt), `HELD_GROESSE`, `FUNKEN`.

**Was hier steht, ist Platzhalter** (siehe Kasten oben). Nützlich ist daran nur
die *Naht*: `held` und `abspann` sind die Stellen, an denen ein anderer Name und
andere Zeilen eingesetzt werden, ohne den Clip anzufassen. Was zusätzlich
getauscht werden muss, wenn das Erscheinungsbild der gemeinsamen Firma steht:
`AKZENT` (der grüne Grund), die beiden Assets `logo-icon-weiss.png` und
`avatar-franz-rund-512.png`, die Zeile `ki-lotse.tech` in `abspannbilder()` —
und der Sprechtext von Shot 3, der die Domain ansagt.

### Am Werkzeug abgelesen (14.08.2026) — die halbe Wegweisung oben ist überholt

Beim Bauen dieses Clips hat sich fast jede Annahme aus dem August-Durchlauf
geändert. **Was hier steht, sticht die Abschnitte „Der Gratisweg" und „Am
Werkzeug abgelesen (01.08.)".**

- **Der Gratisweg über Nano Banana 2 ist zu.** Das Modell trägt keine
  UNLIMITED-Kennzeichnung mehr, und sobald man es wählt, **verschwindet der
  Unlimited-Schalter ganz aus der Leiste**; Generate verlangt 1,5 Credits.
  Gratis sind jetzt **Seedream 5.0 lite** und **Seedream 4.5**. Die Motivsuche
  lief auf Seedream 4.5 (2K, Unlimited an): **fünf Bilder, 0 Credits.**
- **Seedance ist bei 2.5 und fällt für die Startframe-Kette aus.** Es kostet 33
  statt 72 — aber es hat **kein Startbild-Feld mehr**, sondern „References", und
  der Referenz-Wähler nimmt die Auswahl nicht an (jede Kachel trägt einen Knopf
  „Check eligibility", offenbar eine Freigabeprüfung). Auch „Edit Video" hilft
  nicht: das ist Video-zu-Video-Bearbeitung, kein Verlängern.
- **Kling 3.0 kann 1080p für 17,5 Credits.** Das ist der Fund. Kling hat das
  Startbild-Feld, das die ganze Kette trägt, und liefert **1244 × 1660** statt
  der 828 × 1108, aus denen die fünf älteren Clips hochgerechnet sind. Ein
  ganzer Clip kostet damit **52,5 Credits**, nicht 600.
- **Ein Kaufangebot fängt den ersten Generate-Klick ab** („Boost credits" für
  mehr parallele Läufe, mit Balance-Anzeige). Nichts kaufen, wegklicken, zweiter
  Klick läuft. **Der erste Klick erzeugt nichts** — wer nicht nachsieht, glaubt,
  der Lauf sei gestartet.
- **`Turn to video` setzt das Modell auf Kling 3.0 zurück**, nicht nur den
  Unlimited-Schalter. Das ist hier kein Schaden, weil Kling ohnehin das Ziel ist.
- **Das Prompt-Feld ist kein Formularelement**, sondern ein bearbeitbarer
  Bereich: Werte lassen sich nicht setzen, nur anklicken → alles markieren →
  tippen.
- **Falle 14 bestätigt:** Ein zweites und drittes Video aus demselben Bild
  braucht `Turn to video` nicht. Prompt ersetzen, Generate — Startbild,
  Auflösung und Modell bleiben stehen. So sind alle drei Shots entstanden.

**Und die Ein-Bild-Regel hat wieder gewonnen:** Statt der geplanten Frame-Kette
über drei Glieder kamen alle drei Shots aus **demselben Mutterbild** mit drei
Bewegungs-Prompts — wie beim Café und bei „Zwei Uhren". Der Übergang trägt
trotzdem: Shot 2 endet damit, dass er den Stab nimmt, Shot 3 beginnt damit, dass
er ihn von unten hochhebt.

**Zwei Prompt-Lücken, die je einen Anlauf gekostet haben:**

1. **Sag, was im Bild NICHT sein soll, sonst erfindet es das Modell.** Ohne
   Verbot stand eine Fotokamera oben auf dem Monitor.
2. **Sag, was die Figur anhat.** Ohne Kleidungsangabe saß der Mann oben ohne und
   muskelbepackt am Schreibtisch — unfreiwillig komisch. `fully clothed, no bare
   shoulders, no muscular physique` gehört in die Negativliste jeder Figur.

### Credit-Rechnung — tatsächlich: **52,5**

| Posten | Menge | Credits |
|---|---|---|
| Bildsuche Mutterbild (Seedream 4.5, Unlimited) | 5 Bilder | 0 |
| Shot 1 — Kling 3.0, 7 s, 1080p | 1 Anlauf | 17,5 |
| Shot 2 — die Übergabe | 1 Anlauf | 17,5 |
| Shot 3 — die Verwandlung | 1 Anlauf | 17,5 |
| **Summe** | | **52,5** |

**Kein einziger Fehlschlag auf Videoebene** — weil die fünf Anläufe alle auf
Bildebene passiert sind, wo sie nichts kosten. Das ist Regel 1 dieser Datei, zum
vierten Mal bestätigt.

Kontostand vorher 960, nachher rund 907. **Damit ist die Ausgangsfrage
beantwortet und zugleich verschoben:** Das Guthaben lässt sich über Auflösung
nicht verbrauchen. Wer 960 Credits nicht verfallen lassen will, macht **mehr
Clips**, nicht teurere — bei 52,5 je Clip sind das rund siebzehn weitere.

---

## Montage — was nach dem Generieren passiert

`montage.py` macht aus den Rohclips den fertigen Post. Die Bildspur bleibt für
beide Sprachen dieselbe, nur Text und Stimme wechseln.

```
python -X utf8 montage.py --clip 02-cafe --dummy   Platzhalter, Kette prüfen
python -X utf8 montage.py --clip 02-cafe --beide   DE und EN bauen
python -X utf8 montage.py --beide                  Eyecatcher (Vorgabe)
python -X utf8 montage.py --ohne-stimme
```

Jeder Clip steht in `montage.py` unter `CLIPS`: Shot-Dateinamen und die beiden
Textzeilen. Ablage der Rohclips im Unterordner des Clips —
`roh/02-cafe/01-grau.mp4`, `02-bunt.mp4`, `03-hinaus.mp4`. Ergebnis liegt in
`fertig/<clip>-<sprache>-4x5.mp4`. Der Eyecatcher liegt aus historischen Gründen
flach in `roh/` und behält das (`ordner: ""`).

**Ein neuer Clip ist ein Eintrag in `CLIPS`, kein neues Skript.**

Was die Kette erledigt:

- **Beschnitt auf 4:5.** Egal ob Higgsfield 16:9, 9:16 oder 1:1 liefert — es
  wird auf die Bildmitte beschnitten, nie mit schwarzen Balken gefüllt.
- **Kernsatz eingebrannt**, über einer Abdunklung nach unten hin. Ohne die wäre
  weißer Text auf hellem Strand unlesbar. Stellschraube: `VERLAUF` in
  `montage.py`.
- **Abspann** mit Logo, Avatar und `ki-lotse.tech` als eigenes Segment.
- **Ton**: Stimme (edge-tts, dieselbe multilinguale Stimme für DE und EN) über
  einem leisen Musikbett, am Schluss auf −16 LUFS gebracht.
- **Originalton der Rohclips wird verworfen.** Was die Videomodelle an Audio
  mitliefern, ist für einen Markenpost unbrauchbar.

Ist ein Satz länger als sein Bild, sagt das Skript es beim Bauen — dann wird der
Satz gekürzt, nicht der Clip gedehnt.

**Gekürzt wird vorne, nicht hinten.** Kling liefert 7 s, drei davon plus Abspann
wären 21 s und damit über der 8–20-s-Regel. Bei einer Kamerafahrt liegt die
Pointe aber am Ende — die Einstellung, auf die zugefahren wird. Wer hinten
abschneidet, wirft genau das Bild weg, wegen dem der Shot existiert. Stellschraube
ist `max_shot` je Clip (02-cafe: 5 s → 18 s gesamt).

## Der Gratisweg (01.08.2026, zweiter Durchlauf — ändert die Kostenrechnung)

**Der ganze Café-Clip hat null Credits gekostet.** Die „10 Credits je Video" aus
dem ersten Durchlauf gelten nur, solange man den Schalter nicht kennt:

- **Bilder:** Modell auf ein Modell mit `UNLIMITED`-Kennzeichnung stellen
  (**Nano Banana 2** — Googles Bildmodell, genau richtig für „gleicher Raum,
  anderes Licht") und den **Unlimited**-Schalter in der Werkzeugleiste umlegen.
  Der Knopf zeigt dann statt einer Zahl `Unlimited ✦`.
  **Falle:** Die Bildanzahl über 1 zu stellen schaltet Unlimited stillschweigend
  ab. Gratis heißt: ein Bild je Lauf, dafür beliebig oft.
- **Video:** **Kling 3.0**, dann die Auflösung von 4K auf Standard stellen —
  darunter erscheint der Hinweis „Change to std for Unlimited" — und den
  **Unlimited mode** einschalten. Der Knopf zeigt dann `Generate Unlimited`.
  Ergebnis: 720p, 7,04 s, 828 × 1108.
- **Der Gratismodus steht in der Warteschlange:** rund 5 Minuten je Video statt
  Sekunden. Das ist der ganze Preis.

**Fallen, die je einen Anlauf gekostet haben:**

1. **`Turn to video` setzt den Unlimited-Schalter jedes Mal zurück.** Vor jedem
   Generate nachsehen, ob am Knopf eine Zahl steht.
2. **Seedance 2.0 trägt eine `FREE`-Kennzeichnung und kostet 72 Credits.** Beim
   Auswählen springt es auf 8 s/1080p. Die Kennzeichnung meint nicht den Preis.
3. **Ein Modellwechsel im Videoformular wirft das Startbild heraus.** Erst das
   Modell wählen, dann das Bild schicken.
4. **Das Startbild lässt sich im Formular nicht setzen** — der leere Rahmen
   öffnet einen Dateidialog. Der einzige Weg ist Bild öffnen → `Turn to video`.
5. **`Enhance` abschalten,** wenn der Prompt Reglosigkeit verlangt. Shot 1 lebt
   davon, dass sich fast nichts bewegt; eine automatische Prompt-Aufhübschung
   arbeitet dagegen.
6. Beim Seitenwechsel springt ein **Rabatt-Popup mit Countdown** auf („61 % OFF").
   Wegklicken. Dasselbe Theater wie am Kauftag.

**Nachtrag 01.08.2026 (beim Bauen von „Der Lotse" am Werkzeug abgelesen):**

7. **Die Bildwerkstatt öffnet auf „Nano Banana Pro", nicht auf „Nano Banana 2".**
   Pro kostet 1,5–2 Credits je Bild und trägt **keine** UNLIMITED-Kennzeichnung;
   der Banner „Nano Banana Pro & 2 UNLIMITED" meint den Ultra-Plan. Das Modell
   muss also jedes Mal aktiv umgestellt werden — erst danach lässt sich der
   Unlimited-Schalter überhaupt sinnvoll umlegen.
8. **Der Unlimited-Schalter der Bildwerkstatt fällt auch beim bloßen Neuladen
   der Seite zurück**, nicht nur bei `Turn to video`. Vor jedem Generate auf den
   Knopf sehen: steht dort eine Zahl, kostet es.
9. **Im Videoformular ist „Unlimited mode" unsichtbar, solange 4K eingestellt
   ist.** Der Schalter erscheint erst unterhalb der Auflösung, wenn diese auf
   1080p oder 720p steht. Abkürzung: Bei 4K steht dort die Zeile
   **„Change to std for Unlimited"** — ein Klick darauf erledigt beides.
10. **Falle 3 bestätigt, und sie ist teurer als sie klingt:** Ein Modellwechsel
    im Videoformular wirft nicht nur das Startbild hinaus, sondern setzt auch
    Auflösung und Unlimited zurück. Passiert das mitten im Ablauf, hilft nur:
    Modell zurückstellen → `Turn to video` erneut → Auflösung → Unlimited →
    Prompt prüfen. In dieser Reihenfolge.
11. **Der Prompt im Videoformular bleibt beim Startbildwechsel stehen.** Nach
    `Turn to video` steht dort noch der Text des vorigen Shots. Wer ihn nicht
    ersetzt, animiert das neue Bild mit der alten Anweisung.
12. **Klicks ins Formular gehen leicht daneben**, weil die Leiste beim Tippen
    umbricht und die Schaltflächen verrutschen. Sicherer ist, das Prompt-Feld
    über sein Element anzusteuern statt über eine Bildschirmposition.

**Der Ablauf, der ohne Umweg durchläuft:**
Modell Kling 3.0 → Bild öffnen → `Turn to video` → Prompt ersetzen → Auflösung
720p → Unlimited an → am Knopf prüfen, dass dort **„Generate Unlimited"** steht
→ Generate. Rund 3–5 Minuten je Video; die drei Läufe können sich überlappen.

## Am Werkzeug abgelesen (01.08.2026, erster Durchlauf)

Der Clip ist gebaut. Was dabei anders war als angenommen:

- **Bilder kosten im Plus-Plan gar nichts.** Sie laufen gegen ein eigenes
  Kontingent („free gens", Stand 2.980) statt gegen die Credits. Die Regel
  „Motivsuche auf Bildebene" ist damit noch günstiger als gerechnet.
- **Ein Video kostet 10 Credits** (Kling 3.0, 5 s, 720p). Der ganze Clip mit
  drei Shots und acht Standbildern: **30 Credits**. Nicht 60–120.
- **Der Soul-ID-Charakter ist in der Bildwerkstatt voreingestellt.** Wer ihn
  nicht aktiv entfernt (× an der Charakter-Kachel), bekommt Franz' Gesicht auf
  jede Figur im Bild — auch auf den Mann im Unterhemd. Für Clips ohne Franz
  ist das der erste Handgriff.
- **Die Presets sind Stil-Looks, keine Kamerafahrten.** Kamerabewegung gehört in
  den Prompt, das Preset bleibt auf `GENERAL`.
- **Kontinuität kommt aus dem Startframe, nicht aus dem Prompt.** Shot 2 und 3
  wurden aus *demselben* Startbild wie Shot 1 erzeugt — gleicher Raum, gleiche
  Kamera. Der Versuch, für Shot 3 ein eigenes „aufgeräumtes Büro" zu
  generieren, lieferte einen sichtbar anderen Raum und wurde verworfen.
- **Kling liefert 828 × 1108** (≈ 3:4), egal was die Oberfläche als
  Seitenverhältnis anzeigt. Der Beschnitt auf 4:5 verliert dadurch fast nichts,
  aber die Breite wird auf 1080 hochgerechnet — sichtbar weicher als echtes
  1080p. Falls das stört: höhere Auflösung kostet mehr Credits.

## Credit-Rechnung für diesen Clip

| Posten | Menge | Credits |
|---|---|---|
| Bildvarianten für 3 Motive | 30–60 Bilder | 4–8 |
| Videos (1–2 Versuche je Shot) | 3–6 | 55–110 |
| **Summe** | | **60–120** |

Mit der Sparfassung (Shot 2 als Schnitt) rund 40–75. Zum Vergleich: Starter hat
200 Credits im Monat, Plus 1.000. Ohne die Bild-zuerst-Regel läge derselbe Clip
bei 160–270 — also fast einem ganzen Starter-Monat für ein einziges Video.

---
---

# Kampagne „Musst du nicht" — Clip 07 und 08

> Angelegt 14.08.2026. Gerüst, Variationsachse und die Auflösung der Regel
> „Keine erfundenen Kunden" stehen in `ideen.md` §„Kampagne Musst du nicht".
> **Für den Test nur Deutsch** — die englische Spur kommt erst, wenn Andi
> zugestimmt hat.

## Was hier anders ist als bei Clip 01–06

1. **Eine Einstellung, zwei Leute, ein Dialog.** Kein Schnitt, keine Fahrt. Die
   neuen Modelle liefern Sprache und Lippen aus demselben Lauf — die Tonspur
   wird **nicht** getrennt gebaut. Das heißt zugleich: **kein Nachbessern.**
   Sitzt die Betonung nicht, wird der ganze Clip neu gewürfelt. Deshalb muss der
   Text vor dem ersten Lauf stehen; am Bild lernen ist hier zu teuer.
2. **Zehn Sekunden, nicht fünf.** Der Dialog passt nicht in einen 5-s-Lauf. Ein
   Clip = ein 10-s-Lauf, also rund 20 Credits statt 10.
3. **Die MARKE aus §Bausteine gilt NICHT.** Tropisches Spätnachmittagslicht ist
   KI-Lotse. Diese Kampagne spielt in Mitteleuropa und lebt von Alltäglichkeit.
4. **Kamera immer fest.** Wackelkamera macht aus der Szene eine Doku — und aus
   dem Straßeninterview damit eine gefälschte Umfrage. Der feste, komponierte
   Rahmen ist das, was die Szene als Szene ausweist.
5. **Erster Handgriff wie immer: Soul-ID abwählen** (× an der Charakter-Kachel).
   Franz kommt in keinem der beiden Clips vor.

**MARKE „Musst du nicht"** (an jeden Bildprompt anhängen)
```
plain everyday realism, flat natural daylight, Central European setting, muted
everyday colours, realistic skin texture, ordinary clothing, locked-off camera,
eye-level, no on-screen text
```

**NEGATIV** (zusätzlich zum Block aus §Bausteine)
```
no handheld shake, no documentary look, no readable signage, no brand logos
```

---

## Die Methode, die alles davor überholt: **englisch drehen, deutsch vertonen**

Franz' Einfall vom 14.08., beim Bully-Versuch bestätigt: *„was wenn wir sie
englisch sprechen lassen, das sollte im Video super funktionieren und
nachvertonen müssen wir für deutsch sowieso."*

**Der Gedanke ist zwingend.** Die Tonspur wird ohnehin ersetzt — also verschenken
wir mit deutschem Dialog genau den Bereich, in dem das Modell gut ist. Auf
Englisch stimmen nicht nur die Laute; **die ganze Darstellung wird besser**:
Betonung, Blicke, Pausen, Timing. Das Stolpern über ch und ä steckt auch im
Gesicht, nicht nur im Ohr. Urteil Franz zum Ergebnis: *„perfekt auf englisch."*

**Die Bedingung:** Englische Münder formen englische Wörter. Eine deutsche
Tonspur darüber hält nur, wenn die Bildgestaltung es verzeiht. **Drei Wege, alle
am selben Tag erprobt:**

1. **Weite Einstellung** — Küche, Bar. Münder klein, Abweichung unsichtbar.
2. **Etwas vor dem Mund** — Bully, Vollgitter. Dann sind sogar Großaufnahmen frei.
3. **Gegenlicht / Silhouette** — Bühne. **Der freieste Weg von allen:** Ist die
   Figur ein Scherenschnitt, gibt es überhaupt keine sichtbare Mundbewegung, und
   man kann *jeden* Text in *jeder* Sprache darüberlegen. Franz: *„man sieht
   keine Mundbewegungen, also ziemlich egal, man kann jeden Text den man will
   drauflegen."*

In einer ausgeleuchteten Großaufnahme ohne Abdeckung geht es nicht.

**Merke, wie Weg 3 entstanden ist:** Von drei Startframe-Fassungen hat Claude die
dunkle als *fehlerhaft* bezeichnet — „der Sänger ist mitverdunkelt, er spricht
doch". Franz hat sie trotzdem gewählt. Der vermeintliche Fehler war der Vorteil.
**Ein dunkles Gesicht ist kein Mangel, sondern Freiheit für die Tonspur.**

**Das Handwerk dabei: der englische Text wird nicht übersetzt, er wird auf Länge
geschrieben.** Die Sprechfenster im Bild müssen zu den deutschen Aufnahmen
passen, sonst nützt die bessere Darstellung nichts. Silben abgleichen, nicht
Bedeutung:

| Deutsch | Silben | Englisch | Silben |
|---|---|---|---|
| Musst du nicht arbeiten? | 6 | Shouldn't you be working? | 6 |
| Die Bestellungen hab ich mir gebaut, mit MyPro. Läuft, während ich hier steh. | 22 | I built the ordering myself, with MyPro. It runs while I'm standing here. | 21 |
| Also nicht? | 3 | So you don't? | 3 |
| Muss ich nicht. | 3 | I don't have to. | 4 |

## Multi-shot funktioniert — und ist an die Mundabdeckung gekoppelt

Der Schalter **Multi-shot** (Video-Werkstatt, über dem Prompt) hat zwei
Betriebsarten, **Auto** und **Custom**. Auf **Auto** wählt das Modell die
Auflösung selbst, ohne jede Kameraangabe im Prompt. **Er ist keine Attrappe.**

Ergebnis beim Bully-Versuch, 15 s: Totale → **Detail-Insert** (Stock, Puck,
Schlittschuh) → **Nah** auf den einen → **Gegenschnitt nah** auf den anderen →
Totale. Fünf Auflösungen, echter Schuss-Gegenschuss. Das ist Montage, nicht
Kamerafahrt.

> **Die Kopplung, die man sich merken muss: Multi-shot baut Großaufnahmen.**
> Damit geht es nur zusammen mit deutscher Vertonung, **wenn der Mund verdeckt
> ist.** Ohne Abdeckung erzwingt Multi-shot, dass man den Modellton behält —
> also den Akzent.

**Nebenwirkung, die Arbeit macht:** Das Modell legt bei einer Sporthalle
durchgehend Raumgeräusch unter den ganzen Clip. Damit findet
`silencedetect=noise=-32dB` die Sprechfenster nicht mehr, weil nirgends Stille
ist. Für die Vertonung muss die Schwelle höher oder es braucht einen anderen
Weg — Handwerk, kein Hindernis, aber einzuplanen.

## Clip 07 — „Die Küche" (Frau fragt Mann, Unterton: Sorge)

Länge 10 s, 4:5. Ablage `roh/07-kueche/`. Der leere Platz ▢ ist hier mit
**Dienstplänen** gefüllt — ein Betrieb mit Personal.

### Startframe (Bild zuerst, kostet nichts)

Modell **Seedream 4.5**, 2K, Unlimited an — der Gratisweg vom 14.08. Nano Banana
ist zu. Erster Handgriff: **Soul-ID abwählen** (× an der Charakter-Kachel).

**Gebaut am 14.08.2026, zweiter Anlauf — das ist das Mutterbild:**
```
Wide two-shot of a plain Central European family kitchen, mid-morning, grey
overcast daylight through a window. Camera at eye level, locked off, standing
back from the scene: both people are fully visible from head to knee with clear
space around them, nothing cropped at the edges of the frame. On the left a man
in his late forties in a plain dark grey t-shirt and jeans sits at a wooden
kitchen table, leaning back in his chair, relaxed, one hand around a coffee mug
that stands on the table, a tablet lying flat on the table in front of him. On
the right, in the open doorway of the same kitchen, a woman in her forties in a
plain light blouse and jeans stands holding a laundry basket against her hip,
stopped mid-step, looking over at him with a questioning expression. Everyday
kitchen: kettle, fruit bowl, tea towels on the oven handle, plain cupboards.
Plain everyday realism, flat natural daylight, muted everyday colours, realistic
skin texture, ordinary clothing, no on-screen text.
```

**Der erste Anlauf war unbrauchbar und warum:** Er stand als „medium wide
two-shot, both fully in frame" da — das Modell hat beides überhört, den Mann am
linken Rand angeschnitten und **den Tisch ganz weggelassen**. Ohne Tisch fehlt
die Kaffeetasse-und-Tablet-Gruppe, also das einzige Bildzeichen dafür, dass der
Mann schon fertig ist. Was geholfen hat, war nicht „wide", sondern die
ausdrückliche Anweisung, **wo die Kamera steht** („standing back from the
scene") und **was das Bild zeigen muss** („from head to knee", „nothing cropped
at the edges"), dazu `no close-up, no cropped bodies` in der Negativliste.

**Negativliste für diesen Startframe** (zusätzlich zum Block aus §Bausteine und
der MARKE-Negativliste dieser Kampagne):
```
fully clothed, no bare shoulders, no muscular physique, no wall clock,
no laptop, no smartphone, no pets, no flowers on the table
```

Die Kleidungsangabe und das ausdrückliche Verbot stehen hier, weil beim Fee-Clip
genau diese zwei Lücken je einen Anlauf gekostet haben: ohne Kleidungsangabe saß
die Figur oben ohne da, ohne Verbot erfand das Modell Gegenstände dazu. Die Uhr
ist verboten, weil Modelle auf Zifferblätter Kauderwelsch schreiben — die
Tageszeit erzählt das Licht.

### Am Werkzeug abgelesen (14.08.2026, Startframe Clip 07)

- **Die Bildanzahl schaltet Unlimited ab.** Wer von 1/4 auf 2/4 stellt, verliert
  den Gratisweg lautlos: der Schalter springt auf Aus und Generate verlangt
  wieder Credits. **Unlimited gilt nur für ein Bild je Lauf.** Also lieber
  mehrmals einzeln laufen lassen als die Anzahl hochdrehen.
- **Beim Unlimited-Lauf zieht der erste Klick.** Das Kaufangebot, das im
  Fee-Durchlauf den ersten Generate-Klick abgefangen hat, kam hier nicht — es
  hängt offenbar an Läufen, die Credits kosten.
- **Ein Gratis-Bild dauert 1–3 Minuten**, nicht Sekunden: erst „Processing"
  (Warteschlange), dann „Generating". Das ist der eigentliche Preis des
  Gratiswegs. Wer glaubt, es hänge, klickt ein zweites Mal und stellt sich in
  die Schlange dahinter.
- **4:5 gibt es in der Seitenverhältnis-Liste nicht** (1:1, 4:3, 3:4, 16:9,
  9:16, 2:3, 3:2, 21:9). **3:4** bleibt die Wahl, wie bei allen älteren Clips.
- **Kein Soul-ID-Charakter aktiv** — bei Seedream 4.5 stand keine Charakter-
  Kachel in der Leiste, Franz' Gesicht kam auf keine der beiden Figuren.

### Das Videomodell kann kein Deutsch — der Beweis steht in vier Wörtern

Zwei Läufe, zusammen 57,5 Credits, beide mit demselben Ergebnis: Bild und
Lippen tadellos, die Sprache nach Ausländern, die es versuchen. Der zweite Lauf
hatte ausdrücklich `native German accent, no foreign accent` im Prompt. Es half
nichts.

**Franz hat gehört, woran es liegt, und das ist die eigentliche Erkenntnis:**
Es scheitert an „ni**ch**t", „wirkli**ch**", „Dienstpl**ä**ne", „a**r**beiten",
„all**ei**ne" — also an **ch (Ich-Laut), ä, r, ei**. Das sind genau die Laute,
die es im Englischen nicht gibt. Das Modell spricht Deutsch mit einem englischen
Lautvorrat: Es formt die Wörter, aber die Phoneme fehlen ihm.

**Daraus folgt eine Regel, die für alle künftigen Clips gilt:**

> **Das Videomodell macht Bild, Takt und Körper. Die Stimme kommt von
> ElevenLabs. Immer.**

Nicht weil es billiger ist (25–32,5 Credits gegen 0,9), sondern weil kein Prompt
einem Modell Laute hinzufügt, die es nie gelernt hat.

### Was die Achsel mit der Sprechmelodie macht

Franz' Frage beim zweiten Lauf: *Wenn er beim letzten Satz mit den Achseln
zuckt, ergibt das nicht von selbst die Sprechweise?* — **Ja, und darin liegt der
einzige Vorteil des Videomodells.** Bei ElevenLabs hat die Stimme keinen Körper:
kein Raum, kein Stuhl, kein Gegenüber, keine Schulter. Ein Tag ist eine
Behauptung über Gefühl, keine Bewegung. Das Videomodell berechnet Geste und Satz
gemeinsam.

Messbar geworden ist das am Takt: Der erste, ungeführte Lauf sprach mit **0,16 s
je Silbe** (gehetzt), der geführte mit **0,18 s** (normal), und die umgeschriebene
Zeile hat sich von selbst eine Atempause in der Mitte genommen — sechs
Sprechblöcke statt vier. **Körperregie im Prompt zahlt sich also aus, auch wenn
der Ton hinterher ersetzt wird**: Sie erzeugt den Takt, in den die echte Stimme
dann hineinpasst.

### Geschrieben klingt vorgelesen

Zwischenstand, den Franz am ElevenLabs-Ton gehört hat: *„hört sich nicht nach
gesprochen an, sondern nach vorgelesen."* Ursache war nicht die Stimme, sondern
der **Satzbau**:

> geschrieben: Ich hab mir die Dienstpläne mit MyPro gebaut. Die laufen allein.
> gesprochen:  Die Dienstpläne hab ich mir gebaut, mit MyPro. Laufen jetzt von allein.

Zwei Handgriffe machen den Unterschied: **nachschieben** („mit MyPro" ans Ende
statt in die Mitte) und **weglassen** (kein Subjekt im zweiten Satz). Das ist
der Fingerabdruck von Sprache, und die Satzmelodie folgt zwangsläufig.
Bemerkenswert: Es war genau **die eine Zeile, die den Produktnamen trägt** —
dort sickert Werbesprache ein, die anderen drei klangen nie vorgelesen.

### Besetzung: die Stimme gehört zur Figur, nicht zum Ohr

Gecastet wurden neun Stimmen an derselben Zeile, 2,4 Credits insgesamt.

| Stimme | Urteil |
|---|---|
| Arthur | **Erzähler.** „Wie aus einem Graf-Bobby-Film." Für die Fee richtig, für eine Küche nie. Braucht für 18 Silben 4,64 s gegen Johns 3,76 — ein Viertel mehr. |
| John | Dynamik stimmt, Stimme nervt („vom Nebentisch im Café"). |
| Marcus | Gute Stimme, träge und undynamisch. |
| Grady | Schläft. |
| Holden | Sehr gut — **aber ein distinguierter Herr**, passt nicht zum Mann am Küchentisch. |
| Archie | Zu jugendlich. |
| **Fraser, Benji** | **Beide passend.** Gewählt: Benji (der knappere). |
| **Helena** | Frau, mittleres Alter — sitzt auf Anhieb. |

**Die Regel dahinter:** Das Bild besetzt die Rolle, nicht das Ohr. Holden war
die schönste Stimme im Test und trotzdem falsch. Und: Der Stimmenfilter kennt
Geschlecht und Alter, aber **keine Sprache** — Arthur wird nicht einmal als
„mittleres Alter" geführt, was den Erzähler-Verdacht schon vorher verraten hätte.

### Sprache-zu-Sprache ist kein sauberer Tausch

Versuch, Johns Sprechweise mit Marcus' Stimme zu verbinden: MP3 in ein
Mini-Video verpackt (der Reiter **nimmt nur Video**, keine Tondatei), durch
`Voice Change` geschickt, Tonspur wieder herausgelöst. 1 Credit.

Das Timing wird auf zwei Hundertstel genau übernommen (3,74 s gegen Johns
3,76 s) — **aber die Klangfarbe driftet.** Franz: *„die Stimme von Marcus ist
Richtung John gedriftet."* Es ist eine Mischung, kein Transplantat. Für
„Rhythmus von A, Stimme von B" **unbrauchbar**; wer eine bestimmte Stimme will,
muss sie suchen, nicht bauen.

### „Also" wird englisch gelesen — phonetisch schreiben hilft

Letzter Stolperstein: Helena las „Also nicht?" als englisches *ˈɔːlsoʊ*. Kein
Wunder — bei einer zweiwörtrigen Zeile fehlt jeder deutsche Kontext, und „also"
ist ein englisches Wort.

**Die Lösung: `Alzo nicht?` ins Sprachfeld schreiben.** Das Z erzwingt das
stimmhafte S des deutschen *ˈalzo*. Gegenprobe „Wirklich nicht?" scheiterte am
Ich-Laut — dieselbe Falle wie beim Videomodell, nur seltener.

> **Merksatz: phonetisch schreiben, was gesprochen wird; richtig schreiben, was
> zu lesen ist.** Der eingebrannte Untertitel behält „Also nicht?".

### Der Ablauf, der am Ende funktioniert hat

1. **Startframe** auf Seedream 4.5, Unlimited, 3:4 — 0 Credits.
2. **Videolauf** Kling 3.0, **zwei Sekunden länger als der Text braucht**, mit
   Körperregie und Haltung im Prompt. Der Ton ist Wegwerfware, aber er setzt den
   Takt.
3. **Sprechfenster messen:** `silencedetect=noise=-32dB:d=0.25` auf den fertigen
   Clip. Das sind die Anker.
4. **Zeilen einzeln in ElevenLabs v3** mit Regie-Tags, phonetisch geschrieben wo
   nötig.
5. **Vorlauf und Nachlauf wegschneiden**, jede Zeile **mittig auf ihr Fenster**
   legen (nicht auf dessen Anfang), mit `atrim` + `adelay`.
6. **Raumton darunter:** braunes Rauschen unter 200 Hz (Kühlschrank) plus ein
   Hauch rosa Rauschen — zusammen bei `volume=0.016` und `0.005`. Gegen die
   Sprecherkabinen-Stille; man soll ihn nicht hören, sondern vermissen, wenn er
   fehlt.
7. **Tafeln als PNG in Clip-Größe rendern** (PIL), nicht generieren und nicht
   abfotografieren.
8. **Untertitel als ASS-Datei**, nicht als SRT.

**Falle bei den Untertiteln:** Über die SRT-Route rechnet libass die
Schriftgröße gegen eine angenommene Bildhöhe von 288 Pixeln hoch — bei 1660 px
Bildhöhe wird `FontSize=54` zu rund 310 Pixeln und füllt den halben Schirm. Eine
**ASS-Datei mit `PlayResX`/`PlayResY` auf die echte Bildgröße** löst das; die
Vorlage liegt als `roh/07-kueche/untertitel-de.ass`.

**Skripte der Sitzung** (Arbeitsordner, nicht im Repo): `bauen.ps1` baut die
ganze Kette in zwei Durchgängen, `tafel_musst.py` und `tafel_traumpaar.py`
rendern die zwei Tafeln.

### Die Stimme aus dem Videomodell ist unbrauchbar — und das ist kein Unfall

Kling liefert Dialog, Lippen und Ton aus einem Lauf, und die Lippen sitzen
tadellos. **Das Deutsch klingt trotzdem nach Ausländern, die es versuchen** —
dazu schläfrig, weil dem Modell nie gesagt wurde, *wie* gesprochen werden soll.

**Die Regel, die daraus folgt: Bild vom Videomodell, Stimme von ElevenLabs.**
Ein Kling-Lauf kostet 25 Credits und ist nicht nachbesserbar; vier ElevenLabs-
Zeilen kosten zusammen **0,9 Credits**. Wer die Sprache im Videomodell zu
reparieren versucht, zahlt das Fünfundzwanzigfache für ein Glücksspiel auf genau
die Fähigkeit, die es gerade nicht gezeigt hat.

Besetzung: **Helena** (Frau, mittleres Alter) und **Arthur** (Mann) — Arthur ist
aus dem Fee-Clip erprobt, auch für das Wort „MyPro". Regie über Inline-Tags:
`[curious]` auf die Frage, `[surprised]` auf die Nachfrage, `[amused][dry]` auf
beide Antworten des Mannes. Die Tags sind der ganze Unterschied zwischen wach
und eingeschlafen.

**Der Filter der Stimmenliste kennt Geschlecht und Alter, aber keine Sprache.**
Frau + mittleres Alter lässt sechs übrig (Helena, Isla, Juno, Maeve, Nadine,
Opal). Ohne Anhören hilft nur der Vorname als Indiz für die Herkunft der
Sprecherin.

### Das Bild diktiert den Takt, nicht der Text

Der fertige Clip hat **feste Sprechfenster**, und die kann keine Tonspur dehnen.
Gemessen mit `silencedetect` an `01-kueche.mp4`:

| Zeile | Fenster im Bild | ElevenLabs netto | zu lang um |
|---|---|---|---|
| Musst du nicht arbeiten? | 0,97 s | 1,22 s | 0,25 s |
| Ich hab mir … Die laufen allein. | 2,82 s | 3,40 s | 0,58 s |
| Also nicht? | 0,70 s | 1,12 s | 0,42 s |
| Muss ich nicht. | 0,77 s | 1,06 s | 0,29 s |

**Kling spricht schneller als ein Mensch** — 0,16 s je Silbe auf den ersten
beiden Zeilen, das ist gehetzt. Natürliches Deutsch braucht überall rund ein
Fünftel mehr. Drei Handgriffe fangen das auf:

1. **Vorlauf wegschneiden.** ElevenLabs legt 0,1–0,2 s Stille vor jede Zeile und
   bis zu 0,6 s dahinter. Roh sind die vier Dateien 9,84 s, netto 6,80 s.
2. **Mittig auf die Mundbewegung legen**, nicht auf deren Anfang. Dann verteilt
   sich der Überhang auf beide Seiten — 0,3 s Vorlauf fallen weniger auf als
   0,6 s Nachlauf, bei dem der Mund schon steht und die Stimme weiterredet.
3. **Letztes Bild halten.** `tpad=stop_mode=clone:stop_duration=0.45` verlängert
   den Clip auf 10,5 s, damit die Pointe ausklingen kann. Ein Standbild vor der
   Tafel ist ohnehin die bessere Montage.

**Fürs nächste Mal:** Den Videolauf gleich **zwei Sekunden länger** bestellen als
der Text braucht. Bei 2,5 Credits je Sekunde kosten die zwei Sekunden 5 Credits —
deutlich weniger als das Gefummel danach, und die Stimme darf atmen.

Der Befehl steht in `scratchpad/ton.ps1` (Sitzung 14.08.); die Sprachdateien
liegen nach Hausbrauch in `sprecher/de/07-kueche/`.

### Videoprompt (aus dem Startframe)

```
Locked-off camera, no camera movement. The woman in the doorway speaks first,
then the man at the table answers without getting up, takes a sip of coffee
during the pause, and answers again. Natural German dialogue, calm everyday
tone, no gestures beyond the coffee mug.

Woman: "Musst du nicht arbeiten?"
Man: "Ich hab mir die Dienstpläne mit MyPro gebaut. Die laufen allein."
Woman: "Also nicht?"
Man: "Muss ich nicht."

Pronounce "MyPro" as "Mai-Pro", English "my" plus German "Pro".
```

### Der Takt — warum genau diese Fassung

Der Dialog muss in einen Lauf von 10 s passen. Gerechnet in Silben (rund
0,27 s je Silbe, dazu ~0,3 s je Sprecherwechsel):

| Zeile | Silben | Dauer |
|---|---|---|
| Musst du nicht arbeiten? | 6 | 1,6 s |
| Ich hab mir die Dienstpläne mit MyPro gebaut. | 12 | 3,2 s |
| Die laufen allein. | 5 | 1,4 s |
| Also nicht? | 3 | 0,8 s |
| Muss ich nicht. | 3 | 0,8 s |
| vier Sprecherwechsel | | 1,2 s |
| **Summe** | | **≈ 9,0 s** |

Damit bleibt rund eine Sekunde für den Schluck Kaffee in der Pause — der Beat,
der die Pointe trägt.

**Zwei Schnitte machen das möglich:**

1. **„jetzt" gestrichen** — „Die laufen allein" statt „Die laufen jetzt allein".
   Das „jetzt" behauptet ein Vorher-Nachher, das die Szene ohnehin zeigt.
2. **„Also musst du nicht." → „Also nicht?"** — kürzer und besser. Der
   Fragende behält damit seine Rolle (die Erkenntnis gehört ihr, nicht ihm),
   aber es klingt nach echter Nachfrage statt nach Aufsagen. Der Echo-Bau
   *musst → muss* bleibt erhalten.

**Fällt die Rechnung im Lauf länger aus**, ist die Reihenfolge zum Kürzen:
erst „Also nicht?" ganz weg (dann fehlt aber der Zuschauer-Stellvertreter),
dann „Die laufen allein." Die Frage und die Pointe sind unantastbar.

**Die Aussprache ist ein echtes Risiko.** Weil Bild und Ton aus einem Lauf
kommen, kostet ein falsch betontes „MyPro" den ganzen Clip. Die Ausspracheregel
gehört deshalb in den Prompt, nicht in die Hoffnung.

### Text (lokal eingebrannt, DE)

| Sekunde | Zeile |
|---|---|
| 0–1,8 | Musst du nicht arbeiten? |
| 1,8–5,3 | Ich hab mir die Dienstpläne mit MyPro gebaut. |
| 5,3–6,9 | Die laufen allein. |
| 6,9–8,0 | Also nicht? |
| 8,0–10 | Muss ich nicht. |
| Tafel | **Musst du nicht.** |

---

## Clip 08 — „Die Straße" (ZURÜCKGESTELLT, 14.08.2026)

> **Nicht bauen.** Für den Test wird nur Clip 07 gedreht. Dieser Clip bleibt
> ausgearbeitet liegen, damit die zweite Beziehung (Neugier statt Sorge) fertig
> in der Schublade steht, falls Clip 07 trägt. Sein Dialog ist noch auf dem
> alten Stand ohne Produktnamen — vor dem Bauen nachziehen.

(Interviewerin fragt Passanten, Unterton: Neugier)

Länge 10 s, 4:5. Ablage `roh/08-strasse/`. ▢ ist hier mit **Angeboten** gefüllt —
ein Einzelunternehmer. Bewusst ein anderes Ding als in Clip 07: die Serie soll
Breite zeigen, nicht ein Produkt wiederholen.

**Dieser Clip ist der heikle.** Umfrage-Optik ist die Form einer Kundenstimme.
Er ist nur zu bauen, wenn die drei Griffe aus `ideen.md` sitzen: keine Zahl,
kein Betriebsname, sichtbare Kennzeichnung — und feste Kamera.

### Startframe

```
A pedestrianised shopping street in a small Central European town, midday, flat
overcast light. A woman in her thirties in a plain jacket holds a small handheld
microphone toward a man in his fifties in a plain work polo shirt, who stands
next to a parked bicycle holding an ice cream cone. Ordinary passers-by blurred
in the background, plain shop fronts without readable signage. Medium two-shot,
eye level, locked-off camera.
```

### Videoprompt

```
Locked-off camera, no camera movement, no handheld shake. The woman with the
microphone asks, the man answers between two licks of the ice cream, she follows
up, he answers. Natural German dialogue, friendly everyday tone, both relaxed.

Woman: "Dienstag, elf Uhr. Müssten Sie nicht arbeiten?"
Man: "Ich hab mir meine Angebote gebaut. Die schreiben sich jetzt selber."
Woman: "Also müssen Sie nicht."
Man: "Muss ich nicht."
```

### Text (lokal eingebrannt, DE)

| Sekunde | Zeile |
|---|---|
| 0–2 | Dienstag, elf Uhr. Müssten Sie nicht arbeiten? |
| 2–5 | Ich hab mir meine Angebote gebaut. Die schreiben sich jetzt selber. |
| 5–7 | Also müssen Sie nicht. |
| 7–10 | Muss ich nicht. |
| Tafel | **Musst du nicht.** |

---

## Clip 09 — „Die Bar" (Frau fragt Mann, Unterton: Erstaunen)

Franz' Szene vom 14.08.2026, vorgezogen vor Clip 08 (Straße), weil sie die
zweite Beziehung ohne die Doku-Falle liefert. Länge 13 s, 3:4.
Ablage `roh/09-bar/`. ▢ ist mit **der Abrechnung** gefüllt.

**Die Beziehung ist Erstaunen, nicht Sorge.** In der Küche fragt sie besorgt, ob
er sich das leisten kann; hier ist sie überrascht und erfreut, dass er schon da
ist. Derselbe Satz, anderer Unterton — genau die Achse, auf der die Serie läuft.
Der Ort erzählt die Uhrzeit von selbst, wie beim Bett-Einfall.

### Der Text

```
Sie: Musst du nicht noch arbeiten?
Er:  Die Abrechnung hab ich mir gebaut, mit MyPro. Läuft seit sechs.
Sie: Also nicht?
Er:  Muss ich nicht.
     (Gläser, kein Wort)
```

**Drei Eingriffe in Franz' Rohfassung, jeder mit einem Grund:**

1. **„was mir viel Zeit erspart" gestrichen.** Das ist ein Erfolgsversprechen und
   verstößt gegen den ersten der drei Griffe aus `ideen.md` (kein Ergebnis, keine
   Zahl). Ersetzt durch **„Läuft seit sechs."** — sagt dasselbe, behauptet aber
   nichts: ein Zustand, kein Nutzen, und er erklärt nebenbei, warum er um diese
   Zeit an der Bar sitzt.
2. **„den Ablauf vereinfacht" → „die Abrechnung".** „Ablauf" ist die blasse
   Mitte zwischen „was mit KI" und einem Ding, das man anfassen kann.
3. **Der Trinkspruch „auf MyPro" gestrichen, das Anstoßen bleibt — stumm.** Auf
   eine Software anzustoßen ist der Moment, in dem der Sketch zur Werbung kippt:
   Bis dahin erwähnt jemand beiläufig etwas, danach wird ein Produkt gefeiert.
   Die Geste allein ist stärker, weil der Zuschauer die Verbindung selbst zieht.

„Also nicht? / Muss ich nicht." steht wörtlich wie in Clip 07. **Das ist Absicht
und die Signatur der Serie** — an der Wiederholung erkennt man beim zweiten Clip,
dass es ein Format ist.

### Der Whisky steht schon da — und das spart Credits

Franz' Rohfassung hatte sechs Körperaktionen: hereinkommen, Hand auf die Hüfte,
setzen, dem Kellner winken, Glas bekommen, anstoßen. **Ein Kellner, der ein Glas
bringt und übergibt, ist genau die Stelle, an der diese Modelle Matsch
produzieren** — Hände und Objekte lösen sich ineinander auf. Clip 07 hat
funktioniert, weil er still war.

Deshalb steht der Whisky vor dem freien Hocker, bevor der Clip beginnt. Das
nimmt zwei Aktionen heraus **und erzählt mehr**: Er wurde erwartet. Der Barmann
bleibt im Hintergrund, unscharf, ohne Handlung.

### Startframe

Modell Seedream 4.5, 2K, 3:4, Unlimited. Soul-ID abwählen.

```
Wide two-shot of a quiet hotel bar in the evening, warm low light, dark wood bar
counter, softly lit bottles on the shelf behind it. Camera at eye level, locked
off, standing back from the scene: both people fully visible from head to knee
with clear space around them, nothing cropped at the edges of the frame. On the
left a woman in her forties in an elegant red evening dress with shoulder straps
sits on a bar stool, turned half sideways towards the room, a champagne flute in
her hand, relaxed. Next to her an empty bar stool, and on the counter in front of
that stool a tumbler of whisky already poured. On the right a man in his forties
in a dark suit has just stepped into the frame and is reaching out to put his
hand on her hip. Far in the background, out of focus, a bartender stands still
behind the counter. Plain everyday realism, warm natural bar light, muted
colours, realistic skin texture, fully clothed, no on-screen text.
```

Negativliste zusätzlich: `no nudity, no neon, no crowd`.

**Warum der Mann schon im Bild steht:** Ein Startframe ohne ihn zwingt das Modell,
eine Figur aus dem Nichts hereinlaufen zu lassen — teurer Zufall. Steht er am
rechten Rand und greift bereits, bleibt der Auftritt eine einzige Bewegung.

### Gebaut am 14.08.2026 — **37,5 Credits**, kein Fehlschlag

| Posten | Menge | Credits |
|---|---|---|
| Startframe, vier Anläufe (Seedream 4.5, Unlimited) | 4 Bilder | 0 |
| Stimmprobe auf die heiklen Wörter | 2 Zeilen | 0,45 |
| Besetzung: vier Frauenstimmen + Holden | 5 Zeilen | 1,5 |
| Restliche zwei Zeilen in Petra und Holden | 2 Zeilen | 0,3 |
| Fehlgriff (Zeile mit falscher Stimme erzeugt) | 1 Zeile | 0,15 |
| **Videolauf Kling 3.0, 14 s, 1080p** | 1 Anlauf | **35** |
| **Summe** | | **37,4** |

Gegen die knapp 60 Credits von Clip 07 — bei einer Sekunde mehr Länge und einer
schwierigeren Szene. Der Unterschied ist **kein zweiter Videolauf**: Der Text
stand vorher fest, und die Aussprache war für 0,45 Credits geprüft.

Besetzung: **Petra** (sie) und **Holden** (er). Fenster im fertigen Bild:
3,05–4,67 / 5,96–9,11 / 10,26–10,97 / 12,24–12,91. Raumton ist hier eine Spur
lauter als in der Küche und liegt höher (Gemurmel statt Kühlschrank):
`brown lowpass 180 @0.015` plus `pink 200–1800 @0.009`.

### Zwei Funde, die beim nächsten Clip Zeit sparen

**Die Kameraposition beschreiben, nicht die Personen.** Zwei Anläufe scheiterten
daran, dass jemand mit dem Rücken zur Kamera stand — erst als im Prompt stand,
*wo die Kamera steht* und dass der Tresen quer durchs Bild läuft, kamen beide
Gesichter. Derselbe Griff wie „standing back from the scene" bei der Küche.

**Die Stimme gehört zur Figur, nicht zur Sprache.** Holden war in der Küche als
„distinguierter Herr" falsch und sitzt im Anzug an der Hotelbar auf Anhieb. Wer
nach dem Bild besetzt statt nach dem Ohr, spart die halbe Sucherei.

**Was das Modell verweigert hat:** einen zweiten Barhocker, viermal, trotz
`no side table, no round table, no cocktail table, no coffee table`. Es stellt
stattdessen einen Hocker als Ablage für den Whisky hin. Konsequenz: Der Mann
**bleibt stehen** statt sich zu setzen — was ohnehin drei Körperaktionen spart.

### Die heiklen Wörter — vor dem Videolauf prüfen

`Abrechnung`, `Läuft`, `noch`, `nicht` — ch, äu, r. **Die Reihenfolge ist hier
umgekehrt: erst die Stimmen, dann das Bild.** Eine Aussprache lässt sich später
phonetisch reparieren (`Alzo`), ein *Wort* aber nicht: Ein Wortwechsel ändert die
Mundbewegungen, und die sind nach dem Videolauf eingebacken. Ein Credit
Stimmprobe schützt 32,5 Credits Bildlauf.

## Clip 10 — „Das Bully" (Mitspieler fragt Mitspieler) · GEPLANT

Franz' Szene vom 14.08.2026. Zwei Hobbyspieler in voller Montur am Bullypunkt,
der eine steht bereit, der zweite kommt dazu, der erste schaut auf. Dialog.
Dann Anpfiff, und der erste spielt dem zweiten den Puck zu.

### Warum dieser Clip die Regeln ändert

**Der Helm verdeckt den Mund — und hebt damit die Fessel auf, an der alles
andere hängt.** Weil die Stimme immer ersetzt wird, waren bisher alle
Einstellungen weit: In einer Großaufnahme sieht man, dass die Lippen nicht zur
Tonspur gehören. Ein **Vollgitter** macht das gleichgültig.

**Deshalb ist das der Clip für Franz' Multi-shot-Versuch** (Idee vom 14.08.):
die Kamera nicht festnageln, sondern das Modell die Auflösung selbst wählen
lassen — Schnitte, Winkel, Nähe. Der Schalter dafür heißt **Multi-shot** und
steht in der Video-Werkstatt über dem Prompt-Feld; bisher nie benutzt. Freie
Kamera und untergelegte Stimme schließen sich sonst aus; mit Helm nicht mehr.

**Warum Eishockey und nicht Football** (Franz' Alternative): Ein Vollgitter
verdeckt so zuverlässig wie ein Facemask; Eishockey ist im deutschen Sprachraum
die plausiblere Szene; und das Bully ist von Natur aus eine Zweiereinstellung
mit eingebautem Startsignal, während der Snap elf Leute drumherum braucht.

### Die Bedingung, ohne die der Witz nicht funktioniert

**Es müssen Hobbyspieler sein, und die Halle muss leer sein.** Profis am Bully
*sind* bei der Arbeit — dann ist „Musst du nicht arbeiten?" sinnlos. Zwei
Erwachsene mit Eiszeit am **Dienstagvormittag** erklären die Frage, ohne sie zu
erklären. Wie die Bar die Uhrzeit erzählt hat.

Nebeneffekt: In einer vollen Halle müssten die beiden schreien, und unsere
ElevenLabs-Aufnahmen sind Gesprächslautstärke. Die leere Halle löst auch das.

### Der Text

```
A: Musst du nicht arbeiten?
B: Die Bestellungen hab ich mir gebaut, mit MyPro. Läuft, während ich hier steh.
A: Also nicht?
B: Muss ich nicht.
   (Anpfiff, Zuspiel)
```

▢ ist **die Bestellungen** — drittes Ding nach Dienstplänen und Abrechnung, alle
drei anfassbar. Der Nachsatz macht den **Ort zum Argument**: Es läuft, obwohl er
in voller Montur auf dem Eis steht. Zustand, kein Nutzen.

**„während" ist geprüft und bestätigt** (14.08., Holden, 0,3 Credits) — trotz ä
*und* ch. Die Gegenprobe „Läuft auch ohne mich" war sogar **länger** (4,16 s
gegen 4,00 s), weil die Stimme vor „auch ohne mich" eine Pause setzt. Also
bleibt „während": knapper und näher an der Szene.

### Besetzung — die Stimme gehört zur Figur *und* zur Rolle

**Der Fragende ist John** (Franz' Entscheidung 14.08.). Genau die Stimme, die in
Clip 07 als Antwortender verworfen wurde — *„diese nervige Stimme, vom
Nebentisch im Café."* Als Fragender ist das die richtige Qualität: einer, der
sich einmischt, ohne gefragt zu sein.

**Das erweitert die Regel aus Clip 09.** Dort hieß sie: die Stimme muss zur
Figur im Bild passen (Holden = Anzug an der Hotelbar). Hier kommt dazu: **sie
muss zur Rolle im Dialog passen.** Der Antwortende muss gelassen klingen, sonst
prahlt er; der Fragende darf ruhig stören. Eine Stimme, die für die eine Rolle
untauglich ist, kann für die andere die beste sein.

Der Antwortende ist noch offen — nach der Figur eher ein Benji-Typ (Hobbyspieler
in Montur) als ein Holden.

Bisherige Fragende der Serie: Ehefrau (Sorge) · Partnerin (Erstaunen) ·
Mitspieler (Neugier mit Ellbogen). Erster männlicher Fragender.

### Gebaut am 14.08.2026 — **37,8 Credits**, kein Fehlschlag

| Posten | Menge | Credits |
|---|---|---|
| Startframes, drei Fassungen | 3 Bilder | 0 |
| Stimmprobe „während" | 2 Zeilen | 0,3 |
| **Videolauf Kling 3.0, 15 s, 1080p, Multi-shot Auto** | 1 Anlauf | **37,5** |
| **Summe** | | **37,8** |

**Gewählter Startframe: die Tiefen-Fassung** — er groß im angeschnittenen
Vordergrund, der zweite weit hinten. Der Anschnitt wäre bei Küche und Bar ein
Fehler gewesen; hier ist er richtig, weil das Gitter Nähe erlaubt. Und er gibt
dem Modell einen Anlass, die Kamera zu bewegen: eine Figur, die durch die ganze
Bildtiefe kommt, lädt zum Umschneiden ein.

**Ergebnis:** Fünf Auflösungen inklusive Detail-Insert und Schuss-Gegenschuss,
Gitter durchgehend vor dem Mund, Zuspiel am Schluss im Bild. Der Pfiff fehlt —
die 15 Sekunden waren voll. Franz: *„passt super."*

**Fassung:** englisch gesprochen, **deutsch untertitelt**, kein deutscher Ton.
Begründung: Die englische Sprechweise ist das Ergebnis des Versuchs — *„es ist
wirklich gesprochen und nicht gelesen"* —, und eine ElevenLabs-Spur darüber
würde genau das wieder zudecken. Der Clip muss ohnehin stumm funktionieren
(eingebrannter Text), also trägt der Untertitel die Aussage und der Ton das
Spiel. Eine deutsche Fassung bleibt jederzeit möglich; Petra und Holden liegen.

**Die Untertitel sitzen auf gemessenen, nicht gehörten Fenstern.** Bei
durchgehendem Hallengeräusch trennt erst `silencedetect=noise=-24dB:d=0.30`
Sprache von Raum. Gefundene Fenster: 6,71–7,51 / 8,14–11,90 / 12,38–13,27 /
13,94–15,04. Die Zuordnung zu den vier Zeilen ist ein Schluss aus der
Reihenfolge und den Nahaufnahmen, kein Beleg — beim Bauen gegenhören.

### Was noch offen ist

- Der Zuspiel am Schluss ist der riskante Beat (kleines schnelles Objekt über
  Eis), so wie das Anstoßen es in Clip 09 war.
- **Wir verlieren die Gesichter.** In Küche und Bar haben sie die Szene
  getragen. Zwei Vermummte, die über Bestellungen reden, hat einen eigenen Witz
  — aber es ist ein anderer Ton, und das sollte bewusst so sein.
- Bei freier Kamera bleibt `no handheld shake` in der Negativliste: Geschnitten
  und bewegt ist Inszenierung, gewackelt ist Doku.

## Abspann für beide — was hier NICHT hingehört

Kein Kompass, kein Avatar, kein `ki-lotse.tech`. Das Erscheinungsbild der
gemeinsamen Firma macht Andi; bis dahin trägt der Clip nur:

- die Tafel **Musst du nicht.**
- eine Zeile Kennzeichnung: *Szene, mit KI erzeugt.*

Die Kennzeichnung ist kein Kleingedrucktes, sondern der Griff, der die Clips von
einer gefälschten Referenz trennt. Sie gehört sichtbar ins Bild, nicht an den
unteren Rand.

## Credit-Rechnung für den Test

| Posten | Menge | Credits |
|---|---|---|
| Startframes suchen (beide Clips) | 20–40 Bilder | 0 (freies Kontingent) |
| Video 10 s, 1–2 Läufe je Clip | 2–4 Läufe | 40–80 |
| **Summe für beide Clips** | | **40–80** |

Ein misslungener Lauf kostet den vollen Preis, weil nichts nachgebessert werden
kann. Deshalb erst den Startframe festzurren, dann einmal sauber laufen lassen.

---

## Clip „Bau dir was du willst" (Wiese, Motiv 12) — IN ARBEIT

Franz' Idee vom 20.08.2026: Ein Mann sitzt mit dem Laptop auf einer leeren
Wiese, tippt, und ein Geschaeft erscheint. Er tippt wieder, das naechste. Dann
haemmert er los und eine ganze Stadt steht da. Ein einziger Satz am Schluss:
**„Bau dir was du willst."**

### Zwei Vorentscheidungen, die hier begruendet werden

**Hochformat heisst: die Stadt waechst nach oben.** Die Kanaele sind 9:16, in
der Breite ist kein Platz. Also Tuerme statt Ausdehnung — der staerkere Effekt,
aber das Mutterbild muss den Himmel freihalten: Horizont tief, Figur klein.

**Der Mann wird von hinten gezeigt.** Nicht aus Scheu: Jede Wachstumsstufe wird
aus der vorigen abgeleitet, und Gesichter fallen beim Ableiten auseinander
(dieselbe Regel wie bei den Cafe-Gaesten). Von hinten schaut der Zuschauer
ausserdem mit ihm auf den leeren Horizont, statt ihn anzusehen.

### Die Regel, an der dieser Clip haengt

**Eine Kette, kein Faecher.** Stufe N+1 wird aus Stufe N abgeleitet, NICHT
jedesmal aus dem Mutterbild. Nur so enthaelt jede Stufe alles, was die vorige
zeigte — sonst springen die Haeuser beim harten Schnitt herum.

### Shot 1 — die leere Wiese (das Mutterbild, hier wird gesucht)

```
Extreme wide landscape shot of a vast empty green meadow under a huge open sky,
vertical format. The horizon line sits very low, about one quarter up from the
bottom edge, so roughly three quarters of the picture is empty pale sky. A
single small human figure sits alone in the grass in the lower part of the
frame, seen from far away and from directly behind: a man cross-legged with an
open laptop on his knees, tiny in the frame, no taller than one tenth of the
frame height, his face not visible. He wears a plain grey t-shirt and jeans.
Unbroken rolling grassland runs to the horizon in every direction, empty and
untouched. Nothing is built anywhere. Soft even daylight from a high overcast
sky, no sun in the frame, no hard shadows. Camera about forty metres behind him
at chest height, locked off, the whole figure small and complete with wide empty
space above and around him. Plain everyday realism, muted natural colours,
realistic grass texture, no on-screen text.
Negative: no text, no captions, no logos, no watermark, no close-up, no medium
shot, no portrait framing, no large figure, no shoulders filling the frame, no
cropped body, no high horizon, no tractor tracks, no field furrows, no crops, no
distorted hands, no warped faces, no plastic skin, no oversaturation, no golden
hour, no sunset, no lens flare, no dramatic clouds, no buildings, no houses, no
roads, no fences, no power lines, no trees, no readable screen, no face visible.
```

**MARKE hier ohne die Lichtzeile** — „warm late-afternoon tropical light" wuerde
gegen den eigenen Prompt arbeiten, genau wie beim grauen Cafe.

**Das flache Wolkenlicht ist kein Stimmungsentscheid, sondern Technik:** Wenn
spaeter Gebaeude ins Bild wachsen, muessen deren Schatten zum Licht passen. Bei
diffusem Licht kann fast nichts nicht passen; bei tiefstehender Sonne faellt
jede Stufe auseinander.

**Teuer gelernt beim ersten Wurf:** *„a few metres behind him"* nimmt das Modell
woertlich — der Mann fuellte die untere Bildhaelfte und der Horizont sass in der
Mitte. Es braucht eine echte Zahl (vierzig Meter) UND eine Groessenangabe
(ein Zehntel der Bildhoehe) UND die Negativliste gegen Portraetnaehe.

Gebaut: `dc7522cc-42c4-4401-bed0-311f5fc12daf` (Seedream 4.5, 9:16, 0 Credits).

### Shot 2 — der erste Laden (aus dem Startframe von Shot 1)

```
Keep the reference image exactly as it is: the same meadow, the same rolling
hills, the same low horizon line, the same pale overcast sky, the same small man
seen from directly behind sitting cross-legged in the grass with an open laptop
on his knees, same grey t-shirt and jeans, same size and same position in the
frame, same camera, same light. Change one single thing: far away on the horizon
line behind him, small in the distance, one modest single-storey shop now stands
in the grass, plain and ordinary, flat roof, one lit shop window facing the
meadow. Everything else stays empty and unchanged.
Negative: no text, no captions, no logos, no watermark, no city, no skyline, no
additional buildings, no roads, no cars, no people, no change to the man, no
change to his size, no change to the sky, no change to the camera angle, no
close-up, no golden hour, no sunset, no trees, no fences, no power lines.
```

Gebaut: `6a024075-57eb-4b16-b6c8-814bb88a883f` — **die Kette traegt**: Mann,
Groesse, Licht und Huegel unveraendert, ein Laden mehr.

### Der eine Lauf, der alles macht — GEBAUT

**Die Standbildkette war ein Umweg.** Franz am 20.08.: *„warum mehr shots, lass
ihn einfach laufen“* — und er hatte recht. Ein einziger Kling-3.0-Lauf mit dem
Mutterbild als Startframe macht das ganze Wachstum in einem Take.

```
The camera holds completely still, locked off, the framing stays exactly as in
the start image. The man sits in the grass with his back to the camera and types
on the laptop. Behind him, far away on the empty horizon, a single small building
fades into existence. He types again and two more appear beside it. Then he types
faster and faster, and in one continuous movement the settlement grows into a
dense city that rises up into the sky: rows of houses, then blocks, then tall
towers stacking upward until they fill the upper half of the frame, windows
lighting up in the dusk. The city grows out of the horizon line and never comes
closer to him. The man stays small, unchanged and seen from behind the whole
time, still typing. Photorealistic, soft overcast daylight, no cut, one
continuous shot.
```

Gebaut: `dd0f9f5c-ff66-467a-b1ef-6ebeb16d0c9e` — Kling 3.0, 720x1280, 5,0 s,
**10 Credits**. Liegt in `roh/12-wiese/` samt `verlauf.png` (fünf Frames
nebeneinander).

**Die zwei Sätze, die den Shot tragen:** *„The city grows out of the horizon line
and never comes closer to him“* hält die Kamera davon ab, auf die Stadt
zuzufahren, und *„The man stays small, unchanged and seen from behind the whole
time“* hält die Figur fest, während hinter ihr alles umgebaut wird. Ohne beides
wandert bei so einer Verwandlung erfahrungsgemäß der Bildausschnitt mit.

**Der Beleg, dass Kling das kann, lag im eigenen Bestand:** der Fee-Clip vom
14.08. (`e9679ee8`) verwandelt ein ganzes Zimmer in einem Take — Fenster wird
Glasfront, Staub löst sich auf, Möbel werden neu. Wer bei einem Verwandlungs-Shot
zuerst an eine Standbildkette denkt, hat den eigenen Vorrat nicht geprüft.

### Zweiter Lauf: freilassen — GEBAUT, und der bessere

Franz nach dem ersten Lauf: *„lass ihm freien Lauf, die Häuser sollen aufpoppen,
die Kamera muss nicht stillstehen“*. Dieselbe Szene, alle Fesseln raus — keine
Negativliste, kein `locked off`, kein `never comes closer`:

```
The man hammers away on the laptop keyboard, faster and faster. With every burst
of typing, buildings pop into existence on the horizon behind him — one snaps
into place out of nothing, then three at once, then a whole row, then dozens,
each appearing abruptly and in rhythm with his keystrokes. The village becomes a
town, the town becomes a city, and the city keeps shooting upward: towers burst
out of the ground and stack higher and higher into the sky, windows lighting up
as dusk falls. The camera pulls back and tilts up to follow the skyline as it
rises above him. Energetic, joyful, photorealistic, one continuous shot.
```

Gebaut: `5bc8cb5f-512e-4370-8ac2-3f96d8aa38c8` — Kling 3.0, 5,0 s, 10 Credits.
Verlauf in `verlauf2.png`.

**Der Unterschied zum ersten Lauf ist groß, und er kommt aus drei Wörtern:**

| | Lauf 1 (gebändigt) | Lauf 2 (frei) |
|---|---|---|
| Rhythmus | Gebäude wachsen gleichmäßig ein | einzeln, ruckartig — erst **ein** Turm, dann drei |
| Bauhöhe | flache Kästen am Horizont | Hochhäuser, die aus dem Boden schießen |
| Schluss | Reihenhaus-Silhouette | Großstadt in der Dämmerung, Fenster beleuchtet |

`pop into existence` und `snaps into place` erzeugen das Aufpoppen, das
`in rhythm with his keystrokes` bindet es an das Tippen, und
`towers burst out of the ground` hebt die Bauhöhe. Die Kamerafreigabe
(`pulls back and tilts up`) kostet nichts an Ruhe — der Mann bleibt klein und
unverändert, obwohl nichts mehr festgeschrieben ist.

**Die Lehre:** Bei einem Verwandlungs-Shot bremsen Negativlisten das Ergebnis.
Sie gehören in die Bildsuche (wo eine falsche Kameranähe das Motiv zerstört),
nicht in den Bewegungsprompt.

### Der Schnitt

Harte Schnitte im Takt der Tastenanschlaege, nicht ueberblendet. Der letzte Beat
ist der einzige, der ein echter Videolauf sein muss (Kamerarueckzug ueber die
fertige Stadt); alles davor traegt die Standbildkette.

### Text (lokal eingebrannt, nicht generiert)

Eine einzige Tafel am Schluss: **Bau dir was du willst.** Kein Sprecher, kein
Produktname im Bild — deshalb greift die Regel „Keine erfundenen Kunden" hier
praktisch nicht, anders als bei [[Kampagne — Musst du nicht]].

### Fallen der Bild-Werkstatt (Stand 20.08.2026)

1. **Die Werkstatt liegt unter `/ai/image?model=…`**, nicht mehr unter `/image`.
2. **Jedes Laden der Werkstatt wirft ein Werbe-Popup** („Organize. Share.")
   ueber die Bedienleiste, das Klicks abfaengt. Erst schliessen, dann bedienen.
3. **Jedes Laden setzt alles zurueck**: Modell auf Nano Banana Pro, Format auf
   3:4, Unlimited auf aus, Referenzbild weg. Der Knopf zeigt dann „Generate 1"
   statt „Unlimited ✦" — das ist die Pruefung, die den Credit rettet.
4. **Das Referenzbild kommt nur ueber das „+" in der Werkstatt.** Der
   Reference-Knopf in der Galerie-Detailansicht wirft einen bloss zurueck in die
   Galerie. Im „+"-Menue ist das RECHTE Symbol ein Dateidialog (blockiert den
   Browser), das LINKE fuehrt zu den eigenen Assets.
5. **Ein Modellwechsel wirft das Referenzbild NICHT heraus** — anders als im
   Videoformular (Falle 3 oben).
6. **Seedream kann 9:16 direkt.** Die Bilder vom 14.08. waren alle 3:4; das
   Hochformat kam damals erst ueber Kling.
7. **Das Werbe-Popup NUR mit einem echten Klick auf das X schliessen.** Wer es
   per Skript aus dem DOM entfernt, laesst zwei Dinge zurueck, die die ganze
   Seite lahmlegen: den Abdunkel-Layer (`fixed inset-0 bg-black/65`, z-index
   1000), der jeden Klick abfaengt, und **`pointer-events: none` auf dem
   `<body>`**, das die Dialog-Bibliothek beim Oeffnen setzt und nur beim
   regulaeren Schliessen zuruecknimmt. Danach sehen alle Knoepfe normal aus und
   reagieren auf nichts mehr — auch `Reference` und `Recreate` nicht. Das hat am
   20.08. die Stufen 3 und 4 gekostet; beide Ursachen waren gefunden und
   beseitigt, die Oberflaeche kam trotzdem nicht zurueck. Nur ein Neuladen der
   Seite hilft zuverlaessig.
