# Werbespots 9:16 — Arbeitsblatt

**Stand 24.08.2026.** Vier Spots, abgeleitet aus Andis elf Prompts
(`andi-prompts-2026-08-24.txt`). Format durchgehend **9:16**.

**Die drei Startbilder sind erzeugt.** Was noch fehlt, sind die Videos daraus.

## Die Regel, die über allem steht

Andis Prompts enthalten je eine Zeile `On-screen text:` und eine Zeile
`Voice-over:`. **Beide sind hier gestrichen.** Kein Videomodell setzt einen
deutschen Satz richtig — der Lauf vom 24.08. hat daraus „PAKCTIA" plus zwei
Zeilen Buchstabensalat gemacht. Schrift und Stimme kommen nach dem Rendern
dazu.

Nebeneffekt, der hier zählt: **die Clips enthalten keinen Markennamen.** Sie
altern also nicht, während der Name noch offen ist.

Und der Ton wird ebenfalls weggeworfen. Higgsfield hat am 24.08. eine Stimme
darübergelegt, die **nicht einmal die verlangte Sprache trifft** — Andis Prompt
sagt ausdrücklich `Voice-over (German)` plus Aussprachehinweis, herausgekommen
ist etwas, das nach Spanisch klingt. Das ist kein Feinschliff-Problem: die
Zeile im Prompt wird nicht befolgt. Die fertigen Fassungen hier liegen deshalb
**stumm** vor; die Stimme kommt aus ElevenLabs.

Zweite Regel: **Negativlisten kurz halten.** Beim Wiesen-Clip am 20.08. hat
sich gezeigt, dass lange Verbotslisten die Bewegung im Bild bremsen. Ein
knappes „No lettering." am Ende reicht.

## Der Ablauf je Spot

1. **Startbild** erzeugen — Bildwerkzeug, Modell *Nano Banana Pro*,
   Seitenverhältnis **9:16**, mit **denselben vier Referenzbildern**.
   Kostet **2 Credits**.
2. **Video** daraus erzeugen (image-to-video), 7 Sekunden. Die Verwandlung
   steckt im Videoprompt, nicht in einem zweiten Bild. Rund **55 Credits**.

**Das Seitenverhältnis wird am Startbild eingestellt** und vererbt sich ans
Video. Es steht standardmäßig auf 3:4 — daher kam das Format vom 24.08.

## Die vier Referenzen

Sie liegen in `Franz/_fotos/referenz-kampagne/`:

| Datei | Rolle |
|---|---|
| `00_studio.png` | formell, Smoking |
| `IMG_20260801_135806.jpg` | Nahaufnahme, dunkler Hintergrund |
| `IMG_20260801_150003.jpg` | frontal |
| `IMG_20260801_145919.jpg` | Ganzkörper |

**Für alle Spots dieselben vier verwenden.** Sie decken zusammen Gesicht nah,
Halbfigur, Ganzkörper und formell ab — das ist der Grund, warum die Ähnlichkeit
sitzt, und die Klammer, die aus vier Clips eine Kampagne macht.

### Die Smoking-Falle

**Die Referenzen färben auf die Kleidung ab.** Beim ersten Baustellen-Bild
stand Franz im **Smoking** mitten im Bauschutt — `00_studio.png` hatte die
Garderobe mitgeliefert. Deshalb steht in jedem Startbild-Prompt jetzt:

```
(use the attached character references for his face only, not for his clothing).
He wears a plain light blue business shirt with the sleeves rolled up,
no jacket and no tie.
```

Das hellblaue Hemd ist zugleich das, was er im fertigen Spot 3 trägt — die
Kleidung ist damit über alle vier Spots dieselbe, so wie das Gesicht.

---

## Spot 1 — Labyrinth → Straße

*Der stärkste im Stapel: das Bild ist wörtlich ein Lotse.*

**Startbild — fertig:** `hf_20260824_122745_6349f02e-ec0b-4caf-83a1-7f6c544ef45e.png`

```
Photorealistic vertical photograph, 9:16. A man in his mid-sixties with grey
hair and thin metal-rimmed glasses (use the attached character references for
his face only, not for his clothing). He wears a plain light blue business
shirt with the sleeves rolled up, no jacket and no tie. He stands in the middle
of an immense dark labyrinth. Its walls are built from towering stacks of paper
documents, invoices, printed spreadsheets, flowcharts and fragments of code,
rising far above his head. Narrow corridors branch off in several directions.
Cold blue-grey overhead light, deep shadows, faint dust in the air. He stands
still, shoulders tense, looking to one side, uncertain which way to go. Full
body visible, camera slightly below eye level. Cinematic, shallow depth of
field, muted desaturated colours.
```

**Video (7 s) — offen**

```
The camera pushes slowly forward past him. Ahead, a bright opening tears open
in the wall of documents and warm golden sunlight floods into the labyrinth.
He turns towards it and walks through. Behind him the paper walls dissolve and
blow away. He emerges onto a wide clean modern road running straight to the
horizon under an open sky, soft glowing guide lines along its surface. He
slows, straightens his shoulders and smiles. One continuous take, smooth
forward camera movement, cold light turning warm. No lettering.
```

---

## Spot 2 — Baustelle → fertiges Gebäude

*Trägt den Softwarebau, ohne ihn erklären zu müssen.*

**Startbild — fertig:** `hf_20260824_122543_db94a81a-616b-419c-9695-37e375eb4165.png`

*(Die erste Fassung `hf_20260824_121951_dd23e3d0-…` ist die mit dem Smoking —
liegt zur Anschauung daneben, ist aber unbrauchbar.)*

```
Photorealistic vertical photograph, 9:16. A man in his mid-sixties with grey
hair and thin metal-rimmed glasses (use the attached character references for
his face only, not for his clothing). He wears a plain light blue business
shirt with the sleeves rolled up, no jacket and no tie. He stands in the middle
of a chaotic construction site. Building plans, tools, stacked materials,
scaffolding and half-finished concrete walls are scattered all around him.
Overcast grey daylight, dust. He holds a rolled-up plan at his side and looks
at the mess with a frustrated, uncertain expression. Full body visible, camera
at eye level. Cinematic, shallow depth of field, muted colours.
```

**Video (7 s) — offen**

```
The camera slowly rises and orbits around him. The scattered plans, tools and
materials lift off the ground, straighten and assemble themselves in the air
around him. The scaffolding falls away to reveal a finished modern glass
office building standing in bright clear daylight behind him. He lowers the
plan, looks up at the building and smiles. One continuous take, smooth rising
camera movement, grey light turning bright. No lettering.
```

---

## Spot 3 — Büro → Wiese

**Fertig, kein Renderlauf nötig.** Liegt als `spot-buero-wiese-9x16.mp4`
(1080×1920, stumm) vor: aus dem 3:4-Lauf vom 24.08. beschnitten, Schrift
repariert, Tonspur entfernt.

Kein neues Startbild nötig.

---

## Spot 4 — Kontrollraum → ein Dashboard

*Spricht die IT-Seite an.*

**Startbild — fertig:** `hf_20260824_122320_2113da48-1b27-489a-a4fc-b14909e24c77.png`

```
Photorealistic vertical photograph, 9:16. A man in his mid-sixties with grey
hair and thin metal-rimmed glasses (use the attached character references for
his face only, not for his clothing). He wears a plain light blue business
shirt with the sleeves rolled up, no jacket and no tie. He sits in a dark
control room surrounded by dozens of screens on the walls around and above him,
showing alerts, dashboards, tickets, emails and project charts. Their blue glow
is the only light on his face. He sits slightly hunched, overwhelmed by the
amount of information. Camera behind and slightly above him, his silhouette
against the wall of screens. Cinematic, deep shadows.
```

**Video (7 s) — offen**

```
The dozens of screens slide inward and merge into one single large clean
display in front of him. The clutter on it resolves into a calm, well ordered
overview. The room brightens as warm light rises. He leans back in his chair,
relaxed, and nods slightly. One continuous take, slow forward camera movement,
cold blue light turning warm. No lettering.
```

---

## Was noch zu tun ist

Drei Videos: **Spot 1 · 2 · 4**, je aus dem fertigen Startbild. Rund 55 Credits
je Stück, also etwa 165 zusammen.

**Guthaben:** 645 Credits am 24.08. vor den Startbildern; fünf Bilder à 2
Credits sind weggegangen (eines davon der verworfene Smoking-Versuch), es
sollten also rund **635** übrig sein. Das Abo verlängert sich am **01.09.**,
Restcredits verfallen dann.

Falls es knapp wird: **Spot 1 ist der, den du sicher haben willst.**

## Was danach kommt

- **Schrift** — wird nachträglich gesetzt, so wie bei Spot 3 geschehen. Kostet
  keine Credits und ist jederzeit änderbar, auch nachdem der Name feststeht.
- **Stimme** — getrennt über ElevenLabs. Dort ist auch die Aussprache des
  Markennamens durchsetzbar, was im Videomodell nicht geht.
