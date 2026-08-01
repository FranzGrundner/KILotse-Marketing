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

## Montage — was nach dem Generieren passiert

`montage.py` macht aus den Rohclips den fertigen Post. Die Bildspur bleibt für
beide Sprachen dieselbe, nur Text und Stimme wechseln.

```
python -X utf8 montage.py --dummy      Platzhalter erzeugen und Kette prüfen
python -X utf8 montage.py --beide      DE und EN bauen (aus roh/)
python -X utf8 montage.py --ohne-stimme
```

Ablage: Rohclips als `roh/01-buero.mp4`, `roh/02-arm.mp4`, `roh/03-hinaus.mp4`
(die Namen stehen in `montage.py` unter `SHOTS`). Ergebnis liegt in
`fertig/01-eyecatcher-<sprache>-4x5.mp4`.

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
