## Anforderungen

- **Python 3.13** oder neuer
- **PDM** (Python Development Master) zur Paketverwaltung

## Projektstruktur
Leistungskurve_Aufgabe_1/
├── main.py               # Hauptskript zum Starten der Analyse
├── pyproject.toml        # PDM Projektkonfiguration
├── pdm.lock              # PDM Lockfile (fixierte Abhängigkeiten)
├── data/
│   └── activity.csv      # Die Quelldaten (Leistungswerte)
├── source/
│   ├── __init__.py       # Macht den Ordner zu einem Python-Paket
│   ├── load_data.py      # Modul zum Einlesen der CSV-Daten
│   ├── sort.py           # Eigener Sortier-Algorithmus (Bubble Sort)
│   └── power_curve.py    # Logik für Berechnung und Visualisierung
└── figures/
    └── power_curve.png   # Generierte Leistungskurve




Nutzung und Ausführung
Das Projekt wird über eine zentrale Einstiegsdatei gesteuert.

Hauptprogramm starten
Führen Sie den folgenden Befehl im Terminal aus:

Bash
pdm run python main.py
Ablauf des Programms
Wenn die main.py starten, führt das Programm folgende Schritte automatisch aus:

Laden: Die Daten werden aus data/activity.csv eingelesen.

Berechnung: Die Leistungswerte (Watt) werden in Relation zum Körpergewicht (W/kg) gesetzt.

Sortierung: Die Werte werden mit einem implementierten Bubble-Sort-Algorithmus absteigend sortiert.

Visualisierung: Eine Grafik mit logarithmischer X-Achse (Zeit) wird erstellt und gespeichert.


Gruppe Team: 

Cedric Rissi; Marven Otto
