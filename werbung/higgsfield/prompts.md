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
