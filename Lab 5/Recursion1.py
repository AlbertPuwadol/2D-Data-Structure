def eat(n):
    if n == 1:
        print('eat',n)
    else:
        print('eat',n,end = ' ')
        eat(n-1)

def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n-1)

def sum1ToN(n):
    if n == 1:
        return 1
    else:
        return n + sum1ToN(n-1)

def printNTo1(n):
    if n == 1:
        print(n)
    else:
        print(n,end = ' ')
        printNTo1(n-1)

def print1ToN(n):
    if n == 1:
        print(n,end = ' ')
    else:
        print1ToN(n-1)
        print(n,end = ' ')

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def binarySearch(lo,hi,x,l):
    if hi < lo:
        return None
    mid = ( hi + lo ) // 2
    if x == l[mid]:
        return mid
    elif l[mid] < x:
        return binarySearch(mid + 1,hi,x,l)
    else:
        return binarySearch(lo,mid - 1,x,l)

def move(n,A,C):
    if n == 1:
        print(n, 'from', A, 'to', C)
    else:
        if abs(ord(A) - ord(C)) == 2:
            B = 'B'
        elif A == 'C' or C == 'C':
            B = 'A'
        else:
            B = 'C'
        move(n-1,A,B)
        print(n, 'from', A, 'to', C)
        move(n-1,B,C)

def sum1(n,l):
    if n <= 0:
        return 0
    elif n == 1:
        return l[0]
    else:
        return sum1(n-1,l) + l[n-1]

def sum2(l,start,finish):
    if start > finish:
        return 0
    elif start == finish:
        return l[start]
    else:
        return l[start] + sum2(l,start+1,finish)

def sum3(l):
    if len(l) == 0:
        return 0
    elif len(l) == 1:
        return l[0]
    else:
        return l[0] + sum3(l[1:])

def printlistForw(l):
    if len(l) == 0:
        return 0
    else:
        print(l[0], end = ' ')
        printlistForw(l[1:])

def printlistBkw(l):
    if len(l) == 0:
        return 0
    else:
        printlistBkw(l[1:])
        print(l[0], end = ' ')

def app(l,n):
    if n == 1:
        l.append(n)
    else:
        app(l,n-1)
        l.append(n)

def appB(l,n):
    if n == 1:
        l.append(n)
    else:
        l.append(n)
        appB(l,n-1)

class node():
    def __init__(self, d, nxt = None):
        self.data = d
        if nxt is None:
            self.next = None
        else:
            self.next = nxt

def printList(h):
    if h is not None:
        print(h.data,end = ' ')
        printList(h.next)

def createLLL(l):
    if l == []:
        return None
    else:
        return node(l[0],createLLL(l[1:]))

def createLL(n,s = 1):
    if n == s:
        return node(n)
    else:
        return node(s,createLL(n,s + 1))

l = [14,4,9,7,15,3,18,16,20,5,16,2]
printlistBkw(l)