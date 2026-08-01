# Status: Franz KI-Lotse Werbevideo (Stand für Chat-Fortsetzung)

## UPDATE 2026-07-04 — Design-/Inhalts-Überarbeitung (noch NICHT abgenommen)
Alle 11 Slides wurden nach einem Review überarbeitet und neu generiert.
Die "abgenommen"-Vermerke unten beziehen sich auf den ALTEN Stand.
Änderungen (alle in make_slides.py):
- Hintergrund: Orange/Magenta-Blobs raus, nur noch Teal/Grün/Blau (ruhiger, markenkonform)
- Ecklogo größer (180px-Kreis statt 150), Logo-Text jetzt halbwegs lesbar
- Slide 2: persönliche Zeile neu ("Ich bin Österreicher, lebe in Pattaya…"),
  KI-Logos einheitlich als 3 gleich große Kreis-Badges in einer Reihe, Panel vergrößert
- Slide 3: STOP-Schild + Hörsaal-Foto entfernt, nur noch pairprogramming.jpg zentriert;
  Text jetzt "zwei Beispiele aus meinem Alltag" (statt "zwei Tools" — wegen MyNote)
- Slide 4: liste-kalender.jpg nicht mehr über Quellgröße skaliert (war unscharf)
- Slide 5: Text ohne "korrekte Zeitzone" (Technik-Detail → Nutzen), mytm-Screenshot
  komplett sichtbar (690px breit, Quell-Seitenverhältnis), gcal_mockup-Events beschriftet
- Slide 6: "mytm" → "MyTM"
- Slide 9: Kicker "Mein Angebot" → "Referenz"
- Slide 11: "Termin buchen" → "Kostenloses Erstgespräch (30 Min)", QR-Code zum
  Calendly-Link ergänzt (Links im Video sind nicht klickbar), Portrait höher gesetzt
- Offen: Clips neu rendern (siehe "Nächste Schritte" unten)

## Ziel
Persönliches Werbevideo für Franz (KI-Lotse · Pattaya) — KEIN reines Feature-Demo,
sondern Franz erklärt in Ich-Form, dass er bei KI-Einstieg hilft UND selbst
umsetzt, am Beispiel der Projekte mytm/MyNote und MyDocs. Format 16:9, 1920x1080,
stumm (keine Audio/TTS), Text-Slides + Webcam-Bubble unten rechts durchgehend.

## Arbeitsordner
`C:\Claude\Franz\MyTM\loom_video\`
- `make_slides.py` — erzeugt alle 11 Slides (Python/Pillow)
- `slides/` — die 11 generierten PNGs (1920x1080)
- `clips/`, `render_clips.sh`, `concat_list.txt` — Video-Rendering (ffmpeg)
- `photos/` — Stockfotos + Screenshots: presenter.jpg, pairprogramming.jpg,
  liste-kalender.jpg, mynote screenshot.jpeg (liegt im Root, nicht in photos/),
  checkboxes.jpg (To-do-Illustration), mytm_screenshot.png (echter Demo-
  Screenshot, siehe unten), `formulare/` (tm47.png, tm7.png, lebens.png —
  aus MyDocs/system/muster gerenderte Blanko-Vorlagen, keine echten Daten)
- `logos/` — claude.png, gemini.png, chatgpt.png (echte KI-Logos, von Wikimedia
  Commons, User hat sich bewusst für echte Logos statt eigener Icons entschieden)
- `webcam_bubble.png` — echtes rundes Portraitfoto von Franz (336x336, einzige
  echte Portrait-Quelle im Projekt)
- Finales Video (alte Version) liegt in `C:\Claude\Franz\Marketing\werbung\franz-ki-lotse-werbevideo.mp4`
  — MUSS nach Fertigstellung der neuen Slides NEU gerendert werden.

## Finales Skript (11 Slides, ALLE freigegeben — Stand Ende dieser Session)
1. **Hook (10s):** "Du hast schon von KI gehört." + 3 Fragen (Was ist das? / Was
   kann das? / Was bringt mir das?) — mit 🤷 Shrug-Emoji rechts
2. **Wer ich bin (15s):** Franz-Vorstellung + Claude/Gemini/ChatGPT-Logos unten
   rechts verteilt + großes Fragezeichen dahinter (transparent)
3. **Überleitung (10s):** "Statt nur zu reden..." + 2 echte Fotos (presenter.jpg
   mit STOP-Schild, pairprogramming.jpg)
4. **mytm Problem (15s):** Liste/Kalender-getrennt-Problem + liste-kalender.jpg
5. **mytm Lösung (20s):** Text + Screenshot-Collage aus 3 echten/nachgebauten
   App-Ansichten mit Testdaten: mytm-Taskboard (echter Screenshot vom
   Demo-Server, Playwright/Chrome-Channel), MyNote-Aufgabenliste (echter
   Screenshot), Google-Calendar-Wochenraster (programmatisch nachgebaut,
   siehe Learnings) — **abgenommen**
6. **MyNote (15s):** Handy-Mockup mit echtem MyNote-Screenshot, leicht gekippt
   (-7°) mit weichem Schatten + grüner Sync-Badge 🔄 unten links (Bezug zu
   mytm-Sync) — **abgenommen**
7. **MyDocs Problem (15s):** Text + aufgefächerter Formular-Stapel (3 echte
   Blanko-Vorlagen aus MyDocs/system/muster: TM47 oben/gerade, TM7 + Lebens-
   bestätigung schräg dahinter) — **abgenommen**
8. **MyDocs Lösung (20s):** "Leer → automatisch ausgefüllt"-Vergleich auf Basis
   der echten TM47-Vorlage, mit frei erfundenen Beispieldaten (Muster Max,
   Austria, Pattaya, P1234567 etc. — keine echten Personendaten) — **abgenommen**
9. **Mein Angebot (20s):** "Beides sind keine Sonderfälle..." — Text auf
   Segoe UI Black/56pt vergrößert (vorher Regular/44pt, wirkte zu dünn für die
   Aussage) — **abgenommen**
10. **So arbeite ich mit dir (20s):** Starthilfe/Planung/Umsetzung, 3-stufig +
    checkboxes.jpg (To-do-Illustration) unten rechts, leicht gekippt mit
    Schatten — **abgenommen**
11. **CTA (15s):** "Lass uns reden!" + Calendly/Linktree/LINE-Kontaktdaten +
    Logo jetzt mit weißem Kreis-Hintergrund (vorher auf dunklem Panel fast
    unsichtbar) + großes rundes Portraitfoto von Franz (webcam_bubble.png)
    rechts mit grünem Rahmen — **abgenommen**

## Design-System (in make_slides.py, gilt für ALLE Slides)
- Hintergrund: `vibrant_bg(seed)` — dunkle Navy-Basis (#0A0E1A) + 4 verschwommene
  Farb-Blobs (Teal/Indigo-Blau/Orange/Magenta), Position variiert leicht pro
  Slide (Parameter `seed`)
- Schrift: **Segoe UI Black** (`seguibl.ttf`) für Überschriften/Bold, **Segoe UI
  Regular** (`segoeui.ttf`) für Fließtext — NICHT mehr Arial
- Text-Lesbarkeit: `text_panel()` — abgedunkeltes, leicht transparentes
  rounded-rect Panel hinter Textblöcken
- Branding: Kompass-Logo oben rechts in weißem Kreis (`show_logo_corner=True`,
  vorher war Logo auf dunklem Kreis kaum sichtbar — FIX bereits eingebaut)
- Footer: "Franz · KI-Lotse · Pattaya — KI & Automatisierung nebenbei" unten
  links auf jeder Slide
- Fotos/Screenshots: `photo_frame(path, w, h)` — rounded-rect Crop-Helper
  (wiederverwendbar für alle Slides)
- Emoji: `seguiemj.ttf` (Windows Segoe UI Emoji) für einfache Illustrationen,
  funktioniert gut mit `embedded_color=True`. ACHTUNG: ZWJ-Sequenzen (z.B.
  🧑‍💻) rendern NICHT korrekt in diesem Font — nur einzelne Emoji-Codepoints
  verwenden (z.B. 💻 statt 🧑‍💻)

## Wichtige Learnings / Entscheidungen
- User sieht im Chat ab und zu gesendete Bilder NICHT (intermittierendes
  Problem, nicht klar reproduzierbar) — bei "sehe ich nicht" einfach nochmal
  exakt dasselbe Bild erneut senden, meist klappt es beim 2. Versuch. Immer nur
  EIN Bild pro Nachricht senden.
- User ist explizit KEIN Designer ("wahnsinnig schlecht im Design") — braucht
  visuelle Vorschläge zum Reagieren, keine abstrakten Fragen. Am besten: 2-3
  konkrete Varianten bauen und zeigen statt nach Präferenzen zu fragen.
- Echte KI-Logos (Claude/Gemini/ChatGPT) werden bewusst verwendet, obwohl
  offizielle Richtlinien für kommerzielle Nutzung eigentlich eine Erlaubnis
  verlangen — User hat das Risiko nach Aufklärung bewusst in Kauf genommen.
- Freie Stockfotos (Unsplash) sind ok für Fotos (presenter, pair programming) —
  Lizenz erlaubt kommerzielle Nutzung ohne Attribution.
- mytm/MyDocs Demo-Daten: falls ein echter App-Screenshot gebraucht wird,
  NIEMALS die echte `cockpit.db` verwenden — es gibt ein Demo-Setup:
  `C:\Claude\Franz\MyTM\loom_video\make_demo_db.py` (erzeugt
  `demo_cockpit.db` mit neutralen Test-Daten "Kunde A/B/Marketing") +
  `demo_mytm_launch.py` (Wrapper, der mytm_server.py mit MYTM_DB=demo_cockpit.db,
  MYTM_SKIP_GCAL=1 auf Port 8876 startet — Port 8876 ist im Frontend
  hart-kodiert, siehe `SERVER_URL` in script.js). Ein Eintrag "mytm-demo" wurde
  bereits in `C:\Claude\.claude\launch.json` angelegt für preview_start.
  ACHTUNG: Browser-Screenshots über preview_screenshot können nicht direkt als
  Datei gespeichert werden — nur im Chat ansehen möglich. Für den echten
  mytm-Screenshot (Slide 5) wurde stattdessen Playwright direkt per Python
  benutzt (`p.chromium.launch(channel="chrome")` — nutzt das bereits
  installierte System-Chrome, kein zusätzlicher Browser-Download nötig) und
  der Screenshot direkt als PNG gespeichert (`photos/mytm_screenshot.png`,
  Task-Board-Ausschnitt ohne den nicht-authentifizierten Google-Login-Button).
- Google-Calendar-Screenshot: User wollte kein echtes Google-Login automatisiert
  (Privatsphäre/Testdaten-Grund) — Entscheidung: programmatisches Nachbauen
  (`gcal_mockup()` in make_slides.py: Wochenraster mit Google-Farbpalette,
  keine echten Daten) statt echtem Login oder Fake-Icon.
- MyDocs-Formulare: echte Blanko-Vorlagen aus `MyDocs/system/muster/*.pdf`
  (TM47, TM7, Lebensbestätigung) mit PyMuPDF (`fitz`) zu PNG gerendert
  (`photos/formulare/`). NIEMALS die echten ausgefüllten PDFs aus
  `MyDocs/produktion/dokumente/` verwenden (enthalten Franz' echte Daten).
- Für Slide-8-Vergleich ("leer → ausgefüllt") wurden frei erfundene
  Beispieldaten direkt auf die TM47-Vorlage gezeichnet (Koordinaten empirisch
  per Crop-Iteration gefunden, siehe `make_slides.py` Slide-8-Block) — Text
  muss auf der jeweiligen Formularlinie sitzen, nicht nur ungefähr in der Nähe.

## Nächste Schritte
1. Alle 11 Slides sind fertig durchgesehen und abgenommen (siehe Skript oben).
2. `render_clips.sh` läuft mit alten Zeiten (10,15,10,15,20,15,20,20,20,15s) —
   passt noch zur 11-Slide-Struktur, sollte aber gegengecheckt werden
3. Clips neu rendern, concat, Webcam-Bubble-Overlay neu drüberlegen
   (bestehender Workflow in render_clips.sh + ffmpeg concat + overlay, siehe
   frühere Kommandos), Output nach
   `C:\Claude\Franz\Marketing\werbung\franz-ki-lotse-werbevideo.mp4` kopieren
