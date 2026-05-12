import os
import matplotlib.pyplot as plt

from load_data import load_data
from sort import bubble_sort


def main():
    print("Loading data...")
    data = load_data("activity.csv")
    power_W = data["PowerOriginal"]

    # Die echte Power Curve berechnet für jede Sekunde (t) 
    # den maximalen Durchschnitt, den man über t Sekunden gehalten hat.
    
    mmp = [] # Mean Maximal Power
    durations = [1, 5, 10, 30, 60, 120, 300, 600] # Sekunden (wie im Bild)
    
    # Beispiel für eine einfache Annäherung (da Bubble Sort sehr langsam ist):
    # Wenn du wirklich die sortierte Liste aller Sekundenwerte willst:
    power_list = power_W.tolist()
    sorted_power = bubble_sort(power_list)[::-1]

    # PLOT
    plt.figure(figsize=(10, 6))
    
    # Logarithmische X-Achse ist typisch für Leistungskurven!
    plt.semilogx(range(1, len(sorted_power) + 1), sorted_power) 

    plt.title("Leistungskurve (Sortierte Sekundenwerte)")
    plt.xlabel("Zeit / Rang (logarithmisch)")
    plt.ylabel("Leistung (W)")
    # X-Achsen Beschriftung schöner machen
    plt.xticks([1, 10, 60, 300, 3600], ['1s', '10s', '1min', '5min', '1h'])
    
    plt.grid(True, which="both", ls="-")
    os.makedirs("figures", exist_ok=True)
    plt.savefig("figures/power_curve.png", dpi=300)
    print("Plot gespeichert.")



if __name__ == "__main__":
    main()