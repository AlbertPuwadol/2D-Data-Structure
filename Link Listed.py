import Listed as Aa

def bottomUp(l,percent):
    des = percent * l.getSize()//100
    for i in range(des):
        l.append(l.removeHead())

def deBottomUp(l,percent):
    des = percent * l.getSize()//100
    for i in range(des):
        l.addHead(l.removeTail())

def riffle(l,percent):
    des = percent * l.getSize()//100
    len = l.getSize()
    if des == 0:
        return l
    else:
        len = l.getSize()
        t = l.head
        for i in range(des - 1):
            t = t.next
        l2 = Aa.list(t.next)
        t.setNext(None)
        t = l.removeHead()
        temp = l2.head
        t.setNext(temp)
        li = Aa.list(t)
        while li.getSize() != len:
            if temp.next == None:
                temp.setNext(l.head)
            elif l.isEmpty():
                t.setNext(temp)
            else:
                t = l.removeHead()
                temp = temp.next
                l2.before(temp.data).setNext(t)
                t.setNext(temp)
        return li

def deRiffle(l,percent):
    des = percent * l.getSize()//100
    if des == 0:
        return l
    else:
        t = l.head
        t2 = t.next
        tHead = t2
        t.setNext(t2.next)
        t = t.next
        while l.getSize() != des:
            t2.setNext(t.next)
            t2 = t2.next
            t.setNext(None)
            if l.getSize() != des:
                t.setNext(t2.next)
                t = t.next
                t2.setNext(None)
        li = Aa.list(tHead)
        t = l.head
        while t.next != None:
            t = t.next
        t.setNext(li.head)
        return l

n11 = Aa.node("11")
n10 = Aa.node("10",n11)
n9 = Aa.node("9",n10)
n8 = Aa.node("8",n9)
n7 = Aa.node("7",n8)
n6 = Aa.node("6",n7)
n5 = Aa.node("5",n6)
n4 = Aa.node("4",n5)
n3 = Aa.node("3",n4)
n2 = Aa.node("2",n3)
n1 = Aa.node("1",n2)
l = Aa.list(n1)

print(l)
bottomUp(l,50)
print(l)
l = riffle(l,60)
print(l)
l = deRiffle(l,60)
print(l)
deBottomUp(l,50)
print(l)