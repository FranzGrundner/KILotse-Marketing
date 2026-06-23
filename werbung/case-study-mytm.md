# Case Study — MyTM (Eigenprojekt als Referenz)

> Geeignet für: Posts, Loom-Video, Erstgespräch-Einstieg, Linktree-Showcase

---

## Ausgangssituation (Vorher)

**Wer:** Franz (Einzelperson, mehrere parallele Projekte)  
**Problem:** Arbeitsalltag verteilt auf 4 verschiedene Apps —
Gmail, Google Calendar, MyNote (Android), Claude-Projekte.

**Konkret:**
- Mails ankommen, liegen lassen, vergessen
- Termine und Aufgaben aus Mails manuell übertragen
- Notizen auf dem Handy, Projektschritte im Browser, Aufgaben irgendwo dazwischen
- Kein Überblick — jeden Morgen: welche App zuerst?

**Zeitaufwand:** 30–45 Minuten täglich nur für das Sortieren und Verteilen von Informationen

---

## Lösung (Nachher)

**MyTM** — ein persönliches Kommandozentrum, lokal im Browser, gebaut mit Python und Claude AI.

```
Morgens Browser öffnen → eine Seite, alles auf einen Blick:

Gmail (ungelesen)
  → Claude analysiert jede Mail: Löschen / Verschieben / Antworten / Als Task
  → Antwortentwurf in 10 Sekunden, Franz bestätigt nur noch

Google Calendar
  → Nächste 7 Tage auf einen Blick, direkt neben den Aufgaben

MyNote (Android)
  → Notizen vom Handy automatisch abgeglichen, als Tasks übernehmbar

Aufgaben-Board
  → Alle offenen, laufenden, erledigten Tasks aller Projekte an einem Ort
```

**Zeitaufwand nachher:** 5–10 Minuten täglich für den Morgen-Check

---

## Was das technisch ist

- Lokaler HTTP-Server (Python, keine externe Cloud nötig)
- Google-Anbindung via OAuth (Gmail + Calendar)
- Android-Sync via ADB (MyNote)
- Claude AI für E-Mail-Analyse und Antwortentwürfe
- Alles läuft auf dem eigenen Rechner, keine Drittanbieter

**Aufwand:** ca. 3 Wochen Entwicklung (nebenbei, mit KI-Unterstützung)

---

## Vorher / Nachher

| | Vorher | Nachher |
|---|---|---|
| Morgen-Routine | 30–45 Min, 4 Apps | 5–10 Min, 1 Browser-Tab |
| Mails | Manuell lesen, übertragen | KI-Vorschlag, 1 Klick |
| Notizen | Handy ↔ PC manuell | Automatisch synchron |
| Überblick | Keiner | Alles auf einer Seite |

---

## So nutze ich das im Marketing

### Im Erstgespräch

> "Ich habe mir selbst ein KI-gesteuertes Büro gebaut — meine Mails liest Claude,
> schlägt vor was zu tun ist, und ich klicke nur noch Ja oder Nein.
> Sowas kann ich auch für dein Business bauen."

Dann kurz auf dem Handy oder Laptop zeigen. Kein Pitch nötig — das Bild überzeugt.

### Als Post-Hook

**DE:** „Ich habe meinen eigenen Arbeitsalltag mit KI automatisiert. 30 Minuten täglich
Sortierarbeit auf 5 Minuten reduziert — mit einem Tool das ich selbst gebaut habe.
Sowas kann ich auch für dein Business tun."

**EN:** "I automated my own daily workflow with AI. Built a personal command center
that reads my emails, syncs my phone notes, and shows me what needs doing — one page,
one click. I build the same for businesses."

---

## Hook-Zeilen für Posts

**DE:** „Ich habe mir selbst ein KI-Büro gebaut. 30 Min Sortierarbeit täglich → 5 Minuten."

**EN:** "I built my own AI office assistant. 30 minutes of daily sorting → 5 minutes."

---

## Loom-Video Ablauf (wenn du es aufnimmst)

1. Startseite MyTM öffnen (30 Sek.) — "Das ist mein Morgen-Check"
2. Mails-Bereich: 3 echte Mails, KI-Vorschlag zeigen (1 Min.)
3. Kalender-Ansicht kurz (15 Sek.)
4. Aufgaben-Board mit Projekten (30 Sek.)
5. Abschluss: "Das habe ich für mich gebaut — ich baue sowas auch für dich"

**Kein Ton nötig** — Untertitel oder einfach live erklären.
