import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "demo_cockpit.db")

CORE_SCHEMA = """
CREATE TABLE owner (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    typ  TEXT,
    farbe TEXT DEFAULT '#6366f1',
    firmenname TEXT, branche TEXT, mitarbeiterzahl TEXT, leistungsstufe INTEGER,
    ausgabesprache TEXT, beschreibung TEXT, erstgespraech_notizen TEXT,
    status TEXT, slug TEXT, ist_vorlage INTEGER, land TEXT, betriebssystem TEXT,
    backup_praeferenz TEXT, app_sprache_kunden TEXT, zeitplan TEXT,
    dialog_modus TEXT, hardware_details TEXT, erstellt_am TEXT, aktualisiert_am TEXT
);

CREATE TABLE projekte (
    id INTEGER PRIMARY KEY,
    owner_id INTEGER NOT NULL REFERENCES owner(id),
    name TEXT NOT NULL,
    farbe TEXT DEFAULT '#6366f1',
    UNIQUE(owner_id, name)
);

CREATE TABLE todos (
    id INTEGER PRIMARY KEY,
    projekt_id INTEGER REFERENCES projekte(id),
    titel TEXT, beschreibung TEXT, prioritaet TEXT, status TEXT,
    erstellt_am TEXT, erledigt_am TEXT, quelle TEXT, ist_test INTEGER
);

CREATE TABLE photos (
    id TEXT PRIMARY KEY,
    todo_id INTEGER REFERENCES todos(id),
    projekt_id INTEGER REFERENCES projekte(id),
    pfad TEXT, zeitstempel TEXT, gps_lat REAL, gps_lon REAL,
    markiert_insta INTEGER, markiert_fb INTEGER,
    verwendet_insta INTEGER, verwendet_fb INTEGER, quelle TEXT
);
"""

if os.path.exists(DB_PATH):
    os.remove(DB_PATH)

conn = sqlite3.connect(DB_PATH)
conn.executescript(CORE_SCHEMA)

owner_id = conn.execute(
    "INSERT INTO owner (name, typ) VALUES ('Franz', 'privat')").lastrowid

projekte = {}
for name in ("Kunde A", "Kunde B", "Marketing"):
    pid = conn.execute(
        "INSERT INTO projekte (owner_id, name) VALUES (?, ?)", (owner_id, name)
    ).lastrowid
    projekte[name] = pid

todos = [
    ("Kunde A", "Angebot erstellen und versenden", "hoch", "offen"),
    ("Kunde A", "Rechnung Juni verschicken", "mittel", "offen"),
    ("Kunde B", "Termin vorbereiten", "hoch", "in_arbeit"),
    ("Marketing", "Blogartikel KI-Trends schreiben", "mittel", "offen"),
    ("Marketing", "Social-Media-Post planen", "niedrig", "offen"),
    ("Kunde B", "Server-Update durchführen", "mittel", "erledigt"),
]

for projekt, titel, prio, status in todos:
    conn.execute(
        "INSERT INTO todos (projekt_id, titel, prioritaet, status, erstellt_am, quelle) "
        "VALUES (?, ?, ?, ?, datetime('now'), 'demo')",
        (projekte[projekt], titel, prio, status),
    )

conn.commit()
conn.close()
print("demo db created at", DB_PATH)
