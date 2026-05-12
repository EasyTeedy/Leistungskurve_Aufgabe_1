def bubble_sort(data):
    # Kopie erstellen, um die Originaldaten nicht zu verändern
    arr = list(data)
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Sortiere absteigend (für die Power-Curve)
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr