import time
import random

def bubbleSort(l):
    for i in range(len(l)):
        for j in range(0, len(l) - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
        #print(l)

def selectionSort(l):
    for i in range(len(l)):
        index = 0
        for j in range(0, len(l) - i):
            if l[j] > l[index]:
                index = j
        l[index], l[len(l) - i - 1] = l[len(l) - i - 1], l[index]
        #print(l)

def insertionSort(l):
    for i in range(len(l)):
        for j in range(i, 0, -1):
            if l[j] < l[j - 1]:
                l[j], l[j - 1] = l[j - 1], l[j]
            else:
                break

def mergeSort(l, low, high):
    def merge(l, low, mid, high):
        nl = mid - low + 1
        nr = high - mid
        L = []
        R = []
        for i in range(nl):
            L.append(l[low + i])
        for i in range(nr):
            R.append(l[mid + 1 + i])
        run = low
        while nl > 0 and nr > 0:
            if L[0] < R[0]:
                l[run] = L.pop(0)
                nl -= 1
            else:
                l[run] = R.pop(0)
                nr -= 1
            run += 1
        while nl > 0:
            l[run] = L.pop(0)
            nl -= 1
            run += 1
        while nr > 0:
            l[run] = R.pop(0)
            nr -= 1
            run += 1

    if low < high:
        mid = (low + high)//2
        mergeSort(l, low, mid)
        mergeSort(l, mid + 1, high)
        merge(l, low, mid, high)

def quickSort(l, low, high):
    def partition(l, low, high):
        i = low - 1
        pivot = l[high] 
        for j in range(low , high):
            if l[j] < pivot:
                i += 1
                l[i], l[j] = l[j], l[i]
        l[i + 1], l[high] = l[high], l[i + 1]
        return i + 1

    if low < high:
        pivot = partition(l, low, high)
        quickSort(l, low, pivot - 1)
        quickSort(l, pivot + 1, high)

eiei = []
for i in range(1000):
    eiei.append(random.randint(1,100001))
#print(eiei)
t1 = time.time()
bubbleSort(eiei)
t2 = time.time()
#print(eiei)
print('bubble sort use approximate time :', (t2 - t1)*1000000, 'microsecond')

eiei.clear()
for i in range(1000):
    eiei.append(random.randint(1,100001))
#print(eiei)
t1 = time.time()
selectionSort(eiei)
t2 = time.time()
#print(eiei)
print('selection sort use approximate time :', (t2 - t1)*1000000, 'microsecond')

eiei.clear()
for i in range(1000):
    eiei.append(random.randint(1,100001))
#print(eiei)
t1 = time.time()
insertionSort(eiei)
t2 = time.time()
#print(eiei)
print('insertion sort use approximate time :', (t2 - t1)*1000000, 'microsecond')

eiei.clear()
for i in range(1000):
    eiei.append(random.randint(1,100001))
#print(eiei)
t1 = time.time()
mergeSort(eiei, 0, len(eiei) - 1)
t2 = time.time()
#print(eiei)
print('merge sort use approximate time :', (t2 - t1)*1000000, 'microsecond')

eiei.clear()
for i in range(1000):
    eiei.append(random.randint(1,100001))
#print(eiei)
t1 = time.time()
quickSort(eiei, 0, len(eiei) - 1)
t2 = time.time()
#print(eiei)
print('quick sort use approximate time :', (t2 - t1)*1000000, 'microsecond')