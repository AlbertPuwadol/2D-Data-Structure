from math import log2
from math import floor
def print90(h, i, max_i):
    if i < max_i:
        indent = floor(log2(i+1))
        print90(h, (i*2)+2, max_i)
        print('    ' * indent, h[i])
        print90(h, (i*2)+1, max_i)

def insertMinHeap(l, i):
    l.append(i)
    if l != []:
        index = len(l) - 1
        while index > 0 and l[index] < l[(index - 1)//2]:
            l[index],l[(index - 1)//2] = l[(index - 1)//2],l[index]
            index = (index - 1)//2

def deleteMinHeap(l,last):
    l[0],l[last] = l[last],l[0]
    asc.append(l[last])
    index = 0
    while index*2+2 < last and (l[index*2+1] < l[index] or l[index*2+2] < l[index]):
        if l[index*2+1] < l[index*2+2]:
            l[index],l[index*2+1] = l[index*2+1],l[index]
            index = index*2+1
        else:
            l[index],l[index*2+2] = l[index*2+2],l[index]
            index = index*2+2
    if last == 2:
        if l[1] < l[0]:
            l[0],l[1] = l[1],l[0] 
    

h = [68,65,32,24,26,21,19,13,16,14]
l = []
for i in h:
    insertMinHeap(l,i)
    print(l)
asc = []
for i in range(len(l) - 1,-1,-1):
    deleteMinHeap(l,i)
    print(l)