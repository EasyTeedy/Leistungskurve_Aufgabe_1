import os
import matplotlib.pyplot as plt

from load_data import load_data
from sort import bubble_sort


def main():
    print("Loading data...")
    data = load_data("activity.csv")

    # Spalte extrahieren
    power_W = data["PowerOriginal"]

    print(f"Power values: {power_W}")

    # in Liste umwandeln für Bubble Sort
    power_list = power_W.tolist()

    # sortieren + für Power Curve absteigend drehen
    sorted_power = bubble_sort(power_list)[::-1]

    print(f"Sorted power values (descending): {sorted_power}")

    # x-Achse = Rang
    x = list(range(len(sorted_power)))
    y = sorted_power

    # Plot
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, linewidth=2)

    plt.title("Power Curve (sorted values)")
    plt.xlabel("Rank")
    plt.ylabel("Power (W)")
    plt.grid(True)

    # figures Ordner erstellen
    os.makedirs("figures", exist_ok=True)

    # speichern
    plt.savefig("figures/power_curve.png", dpi=300, bbox_inches="tight")
    plt.close()

    print("Plot saved in figures/power_curve.png")


if __name__ == "__main__":
    main()