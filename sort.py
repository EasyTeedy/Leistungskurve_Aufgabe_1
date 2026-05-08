
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        #print("----------------") # danimt mann besser sieht wann neue Runde beginnt
        # Last i elements are already in place, no need to check them
        for j in range(0, n-i-1):
            # SWap der Elemente
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                #print(arr) nach jedem switch neu ausgeben

    return arr