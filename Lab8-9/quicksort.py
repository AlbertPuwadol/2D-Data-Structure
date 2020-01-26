def quickSort1(l, low, high):
    def partition(l, low, high):
        global ohoh1
        i = low - 1
        pivot = l[high] 
        for j in range(low , high):
            if l[j] < pivot:
                i += 1
                l[i], l[j] = l[j], l[i]
                ohoh1 += 1
        l[i + 1], l[high] = l[high], l[i + 1]
        ohoh1 += 1
        return i + 1

    global ohoh1
    if low < high:
        pivot = partition(l, low, high)
        quickSort1(l, low, pivot - 1)
        quickSort1(l, pivot + 1, high)

def quickSort2(l, low, high):
    def partition(l, low, high):
        global ohoh2
        i = low
        pivot = l[low] 
        for j in range(low + 1, high + 1):
            if l[j] < pivot:
                i += 1
                l[i], l[j] = l[j], l[i]
                ohoh2 += 1
        l[i], l[low] = l[low], l[i]
        ohoh2 += 1
        return i

    if low < high:
        pivot = partition(l, low, high)
        quickSort2(l, low, pivot - 1)
        quickSort2(l, pivot + 1, high)

def quickSort3(l, low, high):
    def partition(l, low, high):
        global ohoh3
        i = low
        j = high
        mid = (low + high)//2
        pivot = l[mid] 
        while(j >= i):
            while(l[i] < pivot):
                i += 1
            while(l[j] > pivot):
                j -= 1
            if j >= i:
                l[i], l[j] = l[j], l[i]
                i += 1
                j -= 1
                ohoh3 += 1
        return i

    if low < high:
        pivot = partition(l, low, high)
        quickSort3(l, low, pivot - 1)
        quickSort3(l, pivot + 1, high)

ohoh1 = 0
eiei1 = [i for i in range(1,21)]
print(eiei1)
quickSort1(eiei1, 0, len(eiei1) - 1)
print(eiei1)
print(ohoh1)

ohoh2 = 0
eiei2 = [i for i in range(1,21)]
print(eiei2)
quickSort2(eiei2, 0, len(eiei2) - 1)
print(eiei2)
print(ohoh2)

ohoh3 = 0
eiei3 = [i for i in range(1,21)]
print(eiei3)
quickSort3(eiei3, 0, len(eiei3) - 1)
print(eiei3)
print(ohoh3)