# Plan: Der Higgsfield-Monat

> **Franz · KI-Lotse · Pattaya** · Stand: 01.08.2026 · Status: **Plan, nichts gekauft**
> Grundlage: Recherche 30.07.2026 (siehe Memory `project_bild_video_abo`), Posting-Schleife,
> Kanäle-Tracker.

---

## 0. Das Ziel steht über dem Werkzeug (01.08.2026)

**Franz' Ziel: 2 Kunden pro Monat.** Damit ändert sich der Zweck des Sprints.

Überschlagsrechnung (Schätzung, muss durch echte Zahlen ersetzt werden, sobald der
Tracker welche hat): 2 Aufträge ≈ 5–6 Erstgespräche ≈ 20–30 ernsthafte Kontakte im
Monat. Der geplante Rhythmus (1 DE + 1 EN Post pro Woche) liefert rund 8 Kontaktpunkte.
**Die Lücke ist Reichweite, nicht Materialqualität.**

Konsequenz für den Higgsfield-Monat:

- Die Halde ist **kein Vorrat für die Gruppen-Rotation**, sondern **Munition für die
  Direktansprache**: je Betriebsart ein kurzer Clip, den Franz einem *konkreten* Betrieb
  auf LINE/WhatsApp schickt oder im Erstgespräch zeigt.
- Damit steigen die Betriebsart-Clips (§5, Nr. 8–12) von Beiwerk zum **wichtigsten Teil**
  der Halde, und die allgemeinen Image-Clips rutschen nach hinten.
- **Vorrang hat immer die Ansprache selbst.** Wenn eine Woche die Wahl steht zwischen
  „einen Clip fertig machen" und „fünf Betriebe anschreiben", gewinnt das Anschreiben.
  Material ohne Ansprache bringt null Kunden; Ansprache ohne Material bringt welche.

## 1. Worum es geht

Ein Monat Higgsfield, bewusst als **Produktionssprint**: In diesem Monat wird so viel
Material erzeugt, dass die Facebook-Schleife danach **ohne Abo** monatelang weiterläuft.
Das Abo wird am Ende des Monats gekündigt.

**Die tragende Regel des Sprints:** Alles, was kein Abo braucht, passiert **vorher**.
Skripte, Bildlisten, Prompts, Fotos, Ablage, Renderkette. Im bezahlten Monat wird nur
noch generiert und montiert. Wer im bezahlten Monat noch überlegt, was er eigentlich
sagen will, bezahlt Nachdenken zum Credit-Preis.

---

## 2. Abgrenzung: was Higgsfield kann und was nicht

| Bedürfnis | Werkzeug | Im Sprint? |
|---|---|---|
| Wiedererkennbare **Franz-Figur** über viele Bilder (Soul ID) | Higgsfield | ✅ Kern |
| **Kurze Clips / Kamerafahrten** als Post-Material (b-roll) | Higgsfield | ✅ Kern |
| **Bildwelt** für Posts, Paketseiten, Vorschaukarten | Higgsfield | ✅ Kern |
| **Franz spricht ein Skript** (Gesicht + Lippen + Stimme) | HeyGen (Favorit lt. Recherche) | ⚠️ separat, siehe §7 |
| Homepage-Animation | CSS/SVG/Lottie, **kein KI-Video** | ❌ bewusst draußen |
| Produkt-Screenshots (Prospekt, Paketseiten) | `shots.py`, echte Ansichten | ❌ **niemals KI** |
| Logo | SVG aus `Franz/_design` | ❌ **nie generieren** |

---

## 3. Phase 0 — vor dem Kauf (kostenlos, ca. 2–3 Abende)

Reihenfolge ist wichtig: **Schritt 0.1 ist das Tor.** Fällt er durch, wird nicht gekauft.

### 0.0 Fotos aufnehmen — der Schritt VOR dem Test (Befund 01.08.2026)

Der vorhandene Bestand reicht nicht. Gesichtet wurden sechs Dateien
(`Franz/Comfy/input/*`, `Homepage/shots/franz.png`), es sind aber nur **drei
verschiedene Aufnahmen**: zweimal derselbe Strand-Schnappschuss in zwei
Schnitten, dreimal dasselbe überbelichtete Meerfoto (einmal rund maskiert),
und ein gutes Studiobild im Smoking (`franz_figur.png`). Ein Trainingssatz aus
Beinahe-Dubletten lernt ein Foto auswendig statt ein Gesicht — und das Meerfoto
bringt genau die Falle aus #330 mit: **helles Blass hinter grauem Haar**.

Zehn Minuten mit dem Handy, dann steht der Test auf festem Grund:

- **8–10 Aufnahmen**, alle scharf, Kopf und Schultern, Gesicht füllt etwa ein
  Drittel des Bildes.
- **Hintergrund ruhig und mitteldunkel** — Wand, Vorhang, Hecke. **Nicht** Himmel,
  Meer oder helle Sandfläche: graues Haar hat dieselbe Signatur wie heller
  Hintergrund und verschwindet darin.
- **Licht weich und von vorn**: Schatten im Zimmer neben einem Fenster, oder
  draußen im Schatten. Kein Mittagslicht von oben, kein Gegenlicht.
- **Winkel durchspielen:** frontal · ¾ links · ¾ rechts · einmal Profil.
- **Zwei Mienen:** neutral und lächelnd. Auf fünf von sechs Altbildern ist es
  dasselbe Lächeln — das lernt das Modell als Merkmal mit.
- **Mit und ohne Brille** je ein paar Bilder, sonst wird das Gestell Teil der
  Identität und lässt sich später nicht mehr weglassen.
- Kein Hut, keine Sonnenbrille, keine starke Nachbearbeitung, kein Beauty-Filter
  des Handys.
- Kleidung darf gleich bleiben — die Vielfalt soll in Winkel, Licht und Miene
  liegen, nicht im Hemd.

Ablage: `Franz/Comfy/input/soulid/` (der Ordner `input/` ist bewusst
gitignored — persönliche Aufnahmen gehören nicht in die Versionsverwaltung).

**Am Werkzeug abgelesen (01.08.2026), Zusammensetzung des Satzes:**

- **Mindestens 5 Bilder, damit es weitergeht; ab 20 wird die Ampel grün**, bis
  80 sind erlaubt. Der Dialogsatz „Upload up to 5 photos to continue" meint die
  Untergrenze, nicht die Obergrenze — dieser Irrtum hat einen Anlauf gekostet.
- **Das schwächste Bild bestimmt die Qualitätsnote.** Ein auf 431 px
  beschnittenes Studiofoto zog den ganzen Satz auf „Bad", obwohl die
  Handyfotos 1944 px hatten. Kleine Altbilder deshalb weglassen, auch gute.
- **Mischung**, damit nichts fehlt und nichts einbetoniert wird:
  – Der Großteil Kopf-und-Schultern (die Identität lernt das Modell aus dem Gesicht).
  – **Ein paar OHNE Brille**, sonst wird das Gestell Teil der Identität und lässt
    sich nie mehr wegprompten.
  – **Ein paar von jemand anderem auf Augenhöhe.** Reine Selfie-Sätze sind
    durchweg von leicht unten aufgenommen; das Modell übernimmt diese
    Verzerrung (größere Nase, kürzere Stirn) in JEDE spätere Szene.
  – **Zwei Halbfiguren und ein Ganzkörper.** Nicht für die Identität, sondern
    damit das Modell die Statur nicht erfindet — sonst steht in weiten
    Einstellungen jemand mit dem richtigen Gesicht und fremder Figur da.
    Dabei nah genug bleiben, dass das Gesicht scharf ist (~3–4 m, nicht mehr):
    ein Gesicht von hundert Pixeln trägt nichts bei und verdünnt den Satz.
- Ein Charakter kostet **25 Credits** — bei 1.000 Credits im Monat ist ein
  zweiter Anlauf mit besserem Bildersatz billig. Lieber früh testen und einmal
  nachtrainieren als lange den perfekten Satz suchen.

### 0.1a ERGEBNIS des Ähnlichkeitstests (01.08.2026) — BESTANDEN mit v2

Zwei Charaktere trainiert, dieselben sechs Szenen mit denselben Prompts:

| Szene | v1 (17 Selfies) | v2 (29 Bilder, gemischt) |
|---|---|---|
| Porträt Studio | verjüngt, retuschiert | **echtes Alter, ohne Alterswort im Prompt** |
| Café | Alter ok, Ähnlichkeit mittel | gut — aber Modell wählte ein **Unterhemd** |
| Poolservice | brauchbar | gut, verwendbar |
| Laden, 2 Personen | Identität übergesprungen | **schlimmer**: zweites Gesicht noch näher am eigenen |
| Straße, Profil | gut | gut |
| Hafen, weit | Gesicht verschwunden | erkennbar (engere Einstellung gewählt) |

**Franz erkennt sich wieder.** Der Test ist bestanden — die Franz-Figur kann die
Halde tragen. **Gearbeitet wird ausschließlich mit v2.**

**Die tragende Erkenntnis: Die Verjüngung kam aus dem Bildersatz, nicht aus dem
Modell.** 17 Selfies mit ausgestrecktem Arm im hellen Licht haben das Gesicht
geglättet; Aufnahmen auf Augenhöhe von einer zweiten Person haben das ohne
jeden Prompt-Kniff korrigiert. Wer Ähnlichkeit will, ändert den Bildersatz,
nicht den Prompt.

**Vier Regeln für jeden Prompt, teuer erkauft:**

1. **NIE eine zweite Person mit sichtbarem Gesicht.** Das Modell setzt die
   trainierte Identität ein zweites Mal ins Bild — und je markanter der
   Charakter, desto auffälliger die Kopie (v2 ist hier schlechter als v1).
   Kunden nur von hinten, angeschnitten oder aus dem Bild heraus.
2. **Kopf mindestens ein Drittel der Bildhöhe.** In der Totale zerfällt die
   Identität zuerst.
3. **Kleidung ausdrücklich vorgeben.** Ohne Angabe wählt das Modell frei — im
   Café-Bild wurde daraus ein ärmelloses Unterhemd, unbrauchbar für eine Marke,
   die Vertrauen verkauft.
4. **Alters-Anker ist bei v2 nicht mehr nötig**, schadet aber nicht.

### 0.1 Der Ähnlichkeitstest (Gratis, 10 Credits/Tag)
Genau hier ist Comfy bei #330 gescheitert: Porträt-Ähnlichkeit. Soul ID ist der einzige
Grund, Higgsfield gegenüber einem billigeren Aggregator (Krea ~$9, Freepik ~$5,75) zu
bevorzugen. Also zuerst beweisen, dass es hält:

- 3–5 gute Referenzfotos aussuchen (frontal, seitlich, verschiedenes Licht, scharf,
  **kein Sonnenbrillen-/Hutbild**). Falle aus #330: graues Haar wird von Werkzeugen gern
  als Hintergrund gelesen — Fotos mit dunklem, ruhigem Hintergrund bevorzugen.
- Soul ID trainieren, dann 6 Testbilder in verschiedenen Szenen/Winkeln erzeugen.
- **Abbruchkriterium:** Erkennt ein Bekannter Franz auf 5 von 6 Bildern ohne Vorwarnung?
  Nein → nicht kaufen, stattdessen Aggregator für reine Bildwelt oder ganz lassen.

### 0.2a ECHTE ZAHLEN, am Konto abgelesen (01.08.2026)

Am 01.08. im angemeldeten Konto nachgesehen. **Drei Annahmen der Recherche vom
30.07. waren falsch** — deshalb steht hier ab jetzt die belegte Fassung:

| | Preis (monatlich) | Credits/Monat | Seedance-Videos |
|---|---|---|---|
| **Starter** | **$15** | 200 | ~11 |
| **Plus** | **$49** | 1.000 | ~44 |
| **Ultra** | **$99** (danach $129) | 3.000 | ~133 |

- **Falsch war:** „Starter $15 nur im Jahresabo, monatlich 50–60 % teurer".
  $15 **ist** der Monatspreis. Ein Monatssprint kostet also nicht mehr als gedacht.
- **Falsch war:** „Soul ID ist mit den 10 Gratis-Credits/Tag testbar."
  **Ein Charakter zu trainieren kostet 25 Credits.** Das Gratiskonto hat 10 und
  kann nicht aufladen — die Credits-Schaltfläche führt direkt auf die Bezahlseite
  („Upgrade plan to buy credits"). **Das Kauftor aus §0.1 ist im Gratiskonto
  nicht durchführbar.**
- **Falsch war:** „Verbrauch steht nicht auf der Preisseite." Er steht an jedem
  Knopf: Charakter trainieren 25, ein Soul-2.0-Bild **0,125**.

**Was daraus folgt — die entscheidende Rechnung:**
Bilder sind faktisch gratis (200 Credits = 1.600 Bilder). Der Engpass ist
**Video**. Starter reicht für ~11 Videos im Monat, und die Halde soll 10–12
**brauchbare** Motive haben — bei 3–5 Versuchen je Motiv. Starter deckt also
genau einen Versuch je Motiv und keinen einzigen Fehlschlag.
**Für die Halde ist Plus ($49) die kleinste ehrliche Stufe.**
Starter ($15) ist die kleinste Stufe, um **das Kauftor überhaupt zu testen**.

### 0.2 Preise und Credits am Kauftag selbst prüfen
Die Zahlen vom 30.07. veralten in diesem Markt in Wochen. Vor dem Klick auf der Preisseite
selbst nachsehen und hier eintragen:

- [ ] Monatspreis (nicht Jahrespreis! monatlich ist 50–60 % teurer) der passenden Stufe
- [ ] **Credits pro Monat** und **Verbrauch je Modell** (Kling ~6, Sora 2 / Veo 3.1 40–70)
- [ ] Wasserzeichen ja/nein auf der gewählten Stufe
- [ ] **Kommerzielle Nutzung erlaubt?** — das Material wird für Werbung eingesetzt, das ist
      keine Nebensache
- [ ] Was passiert mit Credits und erzeugten Dateien **nach der Kündigung**
      (Credits verfallen ohnehin nach 90 Tagen, aber: bleibt die Galerie abrufbar?)

**Credit-Budget rechnen, bevor gekauft wird:** Credits ÷ Verbrauch = Anzahl Versuche.
Realistisch sind 3–5 Versuche je brauchbarem Clip. Wenn die Rechnung nicht auf ~40–60
Generierungen kommt, ist die Stufe zu klein.

### 0.3 Die Halde inhaltlich festlegen (siehe §5)
Jeder geplante Clip bekommt **vorher**: Zweck, Zielgruppe (DE/EN), Kernsatz, Bildidee,
Format. Ohne diese Liste wird der Monat ein Sammelsurium.

### 0.4 Prompt-Bibliothek anlegen
Eine Datei `werbung/higgsfield/prompts.md` mit den wiederkehrenden Bausteinen:
Marken-Look (Teal, ruhig, Pattaya-Licht), Franz-Figur (Soul ID), Kamerabewegung je Szene.
Higgsfields eigentliche Stärke sind die **Kamera-Presets** — die gehören in die Bibliothek,
nicht in den Kopf.

### 0.5 Ablage und Renderkette vorbereiten
- Ordner `Franz/Marketing/werbung/higgsfield/{roh,fertig}` + Namensschema
  `<nr>-<thema>-<sprache>-<format>.mp4`
- **Wichtig:** die Roh-Clips aus Higgsfield sind *b-roll*, kein fertiger Post.
  Text, Marke, Avatar-Abspann und Stimme kommen wie bisher lokal dazu — `video.py`
  und `sprecher.py` können das schon. Vor dem Kauf einmal durchspielen, dass ein
  fremder mp4-Clip als Szene in `video.py` läuft.

---

## 4. Der Produktionsmonat — 4 Wochen

### Woche 1 — Identität und Beweis
- Soul ID final trainieren (bestes Fotoset aus 0.1).
- **Erster kompletter Post-Clip fertig bis Tag 3** und sofort raus in die laufende
  FB-Rotation.
- Bildwelt-Grundstock: 15–20 Standbilder mit der Franz-Figur (Profilbild, Post-Köpfe,
  „Franz erklärt", „Franz vor Ort").

> **Warum sofort posten:** Es ist unbewiesen, dass Videoposts in diesen Gruppen besser
> laufen als Text. Zwölf Videos auf Halde zu legen, bevor ein einziges gemessen wurde,
> ist genau die Wette, die die Posting-Schleife eigentlich vermeiden soll.

### Woche 2 — Messen und Kurs korrigieren
- Reaktion auf den ersten Videopost ablesen (Tracker in `kanaele.md`), gegen die
  Textposts halten.
- Danach entscheiden: **mehr Video** (Halde wie geplant), **anderes Format**
  (z. B. Standbild-Karussell statt Clip) oder **weniger Video, mehr Bildwelt**.
- Parallel läuft die Produktion der Clips 2–5 aus §5.

### Woche 3 — Durchproduzieren
- Clips 6–12, Betriebsart-Clips.
- Jeder Clip **sofort** fertig montiert und exportiert — nichts als „mache ich später
  fertig" liegen lassen. Nach der Kündigung gibt es kein Nachlegen.

### Woche 4 — Ernten und schließen
- Lücken füllen, schwache Clips ersetzen.
- **Alles herunterladen** (Roh + fertig), lokal sichern.
- **Kündigen** — Termin dafür am Kauftag sofort in den Kalender, nicht „dann denk ich
  dran". Verlängert sich das Abo unbemerkt, ist der ganze Spar-Gedanke hin.
- Redaktionsplan schreiben: welcher Clip wann in welche Gruppe. Die Halde ist erst dann
  etwas wert, wenn feststeht, wann sie ausgespielt wird.

---

## 5. Die Halde — konkreter Inhalt

**Zielgröße: 10–12 Clip-Motive.** Bei Franz' Rhythmus (1 DE + 1 EN pro Woche, dieselbe
Variante frühestens nach 2–3 Wochen wieder) reicht das für rund ein Quartal. Mehr zu
produzieren heißt, Material zu erzeugen, das veraltet, bevor es dran ist.

**Trick, der die Menge halbiert:** DE und EN teilen sich dieselbe Bildspur. Nur
Texteinblendung und Sprecherspur unterscheiden sich — und die kommen lokal dazu.
Also 10–12 Motive → 20–24 fertige Posts.

| # | Motiv | Quelle im Repo | Bildidee |
|---|---|---|---|
| 1 | Intro „Wer ist der KI-Lotse" | `posts/variante-1-intro-*` | Franz-Figur, Pattaya-Licht, ruhige Kamerafahrt |
| 2 | Problem: Zettelwirtschaft | `posts/variante-2-problem-*` | Papierstapel/Excel-Chaos → Ordnung |
| 3 | Freebie Behördenformulare | `posts/variante-3-freebie-*` | TM7/90-Tage, Formular wird ausgefüllt |
| 4 | Fallstudie MyTM | `werbung/case-study-mytm.md` | — |
| 5 | Fallstudie Strodos | `werbung/case-study-strodos.md` | — |
| 6 | Vorher/Nachher | `werbung/post-vorher-nachher-*` | harter Schnitt grau → farbig |
| 7 | **„Das graue Café wird bunt"** | `project_positionierung_lotse` | Genau dieses Bild ist als *Video* stark und als Standbild schwach — hier zahlt sich der Sprint aus |
| 8–12 | Je ein Clip für die 4–5 stärksten Betriebsarten | Paketseiten / Prospekt | Café, Condo/Vermietung, Spa, Poolservice, Makler |

Dazu **Standbilder**: Profilbild, Post-Köpfe, Vorschaukarten-Motive, ein Motiv je
Betriebsart für die Paketseiten.

**Was hinter den Nummern steckt — und der unausgearbeitete Vorrat — steht in
`werbung/higgsfield/ideen.md`.** Dort ist je Idee vermerkt, ob sie Produktbeweis
braucht (dann lokal mit echten Screenshots bauen) oder reine Atmosphäre ist
(dann Higgsfield über den Gratisweg). Wer den nächsten Clip baut, sucht sich
dort einen aus.

### Stand 01.08.2026

Fertig sind **01 Eyecatcher**, **07 Das graue Café wird bunt** (als `02-cafe`)
und der erste Betriebsart-Clip **Poolservice** (als `03-pool`), jeweils DE und
EN. **Zusammen null Credits** — siehe `prompts.md` §„Der Gratisweg". Damit ist
die Kostenannahme dieses Plans überholt: der Engpass ist nicht mehr Video,
sondern Wartezeit. Das gehört in die Abo-Entscheidung zu **#457**.

---

## 6. Technische Regeln für Facebook

- **Ohne Ton verständlich.** Facebook spielt stumm an. Text ist eingebrannt, nicht
  als „Untertitel-Datei" gedacht.
- **Erste 3 Sekunden entscheiden.** Der Kernsatz steht am Anfang, nicht der Markenname.
- **Format 4:5 oder 1:1** für den Feed, nicht 16:9 — das Video soll die Spalte füllen.
- **Länge 8–20 Sekunden.** Was länger ist, gehört auf die Homepage, nicht in eine Gruppe.
- **Domain fürs Ohr schreiben:** im Sprechtext „ki-lotse punkt tech", im Bild die Domain
  normal. (Lehre aus dem Werbevideo #160.)
- Abspann wie im bestehenden Video: Avatar (RGBA, runde Fassung) + weißes Kompass-Logo
  aus der SVG.

---

## 7. Was der Sprint **nicht** löst

- **Der sprechende Franz.** Wenn ein Gesicht ein Skript aufsagen soll, ist das HeyGen
  (Gratisstufe: 3 Videos mit Wasserzeichen — dieser Test kostet nichts und sollte in
  Phase 0 nebenher laufen, damit die Entscheidung auf Anschauung beruht statt auf
  Vermutung). Er kann dieselben Videos auf Englisch mit demselben Gesicht — das ist der
  eigentliche Hebel für die englischsprachigen Gruppen.
- **Homepage-Animationen.** Bleibt CSS/SVG. Ein 5-MB-Clip auf einer gerade erst
  abgenommenen Seite ist ein Rückschritt.
- **Produktbilder.** Screenshots bleiben echte Screenshots. Ein KI-Bild an der Stelle
  verspricht etwas, was die App nicht zeigt — dieselbe Falle wie #433.

---

## 8. Fallen, die den Monat wertlos machen können

1. **Credits verfallen nach 90 Tagen**, Übertrag gibt es keinen. Nicht am letzten Tag
   die Hälfte übrig haben.
2. **Kündigung vergessen.** Kalendereintrag am Kauftag, 3 Tage vor Ablauf.
3. **Alles nur in der Cloud.** Vor dem Ende alles lokal ziehen.
4. **Halde altert.** Keine Preise, keine Paketzusammensetzungen, keine „seit X Wochen"-
   Aussagen in die Clips — sonst ist das Material tot, sobald sich etwas ändert. Die
   Clips müssen in drei Monaten noch stimmen.
5. **Monatlich statt jährlich zahlen** ist Absicht (der Sprint soll enden), kostet aber
   50–60 % Aufschlag — das ist der Preis der Kündbarkeit und muss in die Rechnung.

---

## 9. Sofortstart — die nächsten 7 Tage (ab Sa 01.08.2026)

Nichts davon wartet auf das Abo. Die Punkte mit 💰 kosten Geld, alle anderen nichts.

### Heute, Sa 01.08. — **Samstag ist in vielen FB-Gruppen der einzige Self-Promo-Tag**
- [ ] **EN-Post der Woche 1** endlich raus. Er fehlt seit dem 29.07., weil „Pattaya
      EXPATS" entgegen dem Namen deutschsprachig ist. Ziel: „Pattaya Business Network",
      Variante 2 (Problem EN) — liegt fertig in `posts/`.
- [ ] **Soul-ID-Gratistest** starten (10 Credits/Tag, §3.1). Das ist das Kauftor.
- [ ] **HeyGen-Gratistest** anlegen (3 Videos mit Wasserzeichen). Läuft nebenher.

### So 02.08.
- [ ] Testbilder beurteilen → Kaufentscheidung. Bei Bestehen: 💰 Monatsabo kaufen,
      **Kündigungstermin sofort in den Kalender** (3 Tage vor Ablauf).
- [ ] Zielliste Direktansprache anlegen: **20 konkrete Betriebe in Pattaya/Jomtien**
      mit Name, Betriebsart, Kontaktweg. Quelle: Google Maps + FB. Betriebsarten, für
      die ein Paket fertig liegt und ein Referenzkunde existiert, zuerst.

### Mo 03.08. – Fr 07.08.
- [ ] **Poolservice zuerst.** Strodos ist ein echter, laufender Referenzkunde in genau
      dieser Branche — „das habe ich für einen Pool-Service gebaut, hier ist es live"
      ist das stärkste Argument, das Franz hat. Erste 5 Betriebe ansprechen.
- [x] **Erster Betriebsart-Clip (Poolservice/Wartung) fertig — 01.08.2026.**
      `werbung/poolservice/poolservice-clip-de.mp4` (4:5, 23 s, Skript und
      Begründungen in `werbung/poolservice/skript.md`). Gebaut wie #160: lokal
      mit PIL/ffmpeg, Bilder sind **echte Screenshots** der laufenden Demo, also
      **ohne Higgsfield-Credits**. Verwendung: direkt in der Ansprache, nicht in
      einer Gruppe streuen.
- [ ] **Di 04.08.: PEC-Meeting** (Pattaya Expats Club, Dienstag vormittags). Steht seit
      Wochen mit ⭐⭐⭐ in `kanaele.md` und ist nie besucht worden. Offline-Kontakt in
      Pattaya ist der kürzeste Weg zu einem Erstgespräch, den es hier gibt.
- [ ] **#427 Auswertung ab 05.08.**: Zahlen des ersten Posts in den Tracker, daraus die
      Entscheidung, ob Gruppen-Posts überhaupt tragen.

### Was in dieser Woche NICHT passiert
Homepage-Umbau, neue Bausteine, Prospekt-Feinschliff. Das Produkt ist verkaufsfertig —
20 Bausteine, 11 Pakete, Demo-Firma, Preise, Prospekte. **Es fehlt kein Baustein,
es fehlen Gespräche.**

---

## 10. Offene Entscheidungen

- [ ] Stufe: Starter / Plus / Ultra — hängt am Credit-Bedarf aus §3.2
- [ ] Läuft der HeyGen-Gratistest parallel? (Empfehlung: ja, kostet nichts)
- [ ] Startdatum des Sprints — die Woche-1-Auswertung des ersten FB-Posts (#427, ab
      05.08.) sollte vorliegen, damit die Halde auf Erkenntnissen aufbaut
- [ ] Welche 4–5 Betriebsarten bekommen einen Clip?
