import os
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from source.load_data import load_data
from source.sort import bubble_sort

def format_time(x, pos):
    #X-Achse in H:MM:SS Format
    if x < 0: 
        return ""
    hours = int(x // 3600)
    minutes = int((x % 3600) // 60)
    seconds = int(x % 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}"

def generate_power_curve():
    weight_kg = 75  #Annahme Körpergewicht
    path = "data/activity.csv"
    
    if not os.path.exists(path):
        print(f"Datei {path} nicht gefunden!")
        return

    all_data = load_data(path)
    raw_power = all_data["PowerOriginal"]
    
    # Sortieren
    sorted_power = bubble_sort(raw_power)
    
    # Y-Werte: Leistung in W/kg
    w_per_kg = [p / weight_kg for p in sorted_power]
    
    # X-Werte: Zeit in sek
    time_steps = list(range(1, len(sorted_power) + 1))

    plt.figure(figsize=(12, 6))
    
    #X = Zeit, Y = Leistung (W/kg)
    # semilogx für logarithmische X-Achse, damit die Kurve besser lesbar ist
    plt.semilogx(time_steps, w_per_kg, color='red', linewidth=2)

    # X-Achse Zeit formatieren
    plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(format_time))
    
    # Manuelle Ticks für die Zeit-Achse logenormieren
    tick_positions = [1, 10, 60, 300, 600, 1200, 1800, 3600]
    plt.xticks(tick_positions)

    plt.title(f"Leistungskurve (Körpergewicht: {weight_kg} kg)")
    plt.xlabel("Zeit (H:MM:SS)")
    plt.ylabel("Leistung (W/kg)")
    
    plt.grid(True, which="both", linestyle='--', alpha=0.5)
    plt.xlim(1, len(sorted_power)) # damit die X-Achse bei 1 Sekunde beginnt

    os.makedirs("figures", exist_ok=True)
    plt.savefig("figures/power_curve.png", dpi=300)
    print("Grafik erstellt: X=Zeit (H:MM:SS), Y=W/kg")