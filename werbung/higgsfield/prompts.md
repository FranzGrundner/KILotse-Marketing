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
