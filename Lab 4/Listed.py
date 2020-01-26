class node:
    def __init__(self,data,next = None):
        self.data = data
        if next == None:
            self.next = None
        else:
            self.next = next

    def __str__(self):
        return str(self.data)

    def getData(self):
        return self.data
    
    def setData(self,data):
        self.data = data

    def getNext(self):
        return self.next

    def setNext(self,next):
        self.next = next

class list:
    def __init__(self,head = None):
        if head == None:
            self.head = None
            self.size = 0
        else:
            self.head = head
            self.size = 1
            t = self.head
            while t.next != None:
                t = t.next
                self.size += 1

    def __str__(self):
        if self.size == 0:
            return "None"
        else:
            t = self.head
            string = str(t.data)
            while t.next != None:
                string = string + " " + str(t.next) + " "
                t = t.next
            return string

    def getSize(self):
        if self.isEmpty():
            self.size = 0
        else:
            self.size = 1
            t = self.head
            while t.next != None:
                t = t.next
                self.size += 1
        return self.size

    def isEmpty(self):
        return self.size == 0

    def append(self,data):
        if self.isEmpty():
            self.head = node(data)
        else:
            n = node(data)
            t = self.head
            while t.next != None:
                t = t.next
            t.setNext(n)
        self.size += 1

    def addHead(self,data):
        if self.isEmpty():
            self.head = node(data)
        else:
            n = node(data)
            n.setNext(self.head)
            self.head = n
        self.size += 1

    def isIn(self,data):
        t = self.head
        while t.next != None:
            if t.data == data:
                break
            else:
                t = t.next
        return t.data == data

    def before(self,data):
        if self.isIn(data) == True:
            t = self.head
            if t.data == data:
                return "No data before"
            else:
                previous = t
                t = t.next
                while t.next != None:
                    if t.data == data:
                        break
                    else:
                        previous = t
                        t = t.next
                return previous
        else:
            return "No data in list"

    def remove(self,data):
        if self.isIn(data) == True:
            if self.size == 1:
                t = self.head
                self.head = None
            else:
                t = self.head
                while t.data != data:
                    t = t.next
                if t == self.head:
                    self.head = self.head.next
                else:
                    self.before(t.data).setNext(t.next)
            self.size -= 1
            return t
        else:
            return "No data in list"

    def removeTail(self):
        if self.size == 1:
            t = self.head
            self.head = None
        else:
            t = self.head
            while t.next != None:
                t = t.next
            tail = t
            t = self.before(t.data)
            t.setNext(None)
        self.size -= 1
        return tail

    def removeHead(self):
        if self.size == 1:
            t = self.head
            self.head = None
        else:
            t = self.head
            self.head = self.head.next
        self.size -= 1
        return t

n10 = node(10)
n9 = node(9,n10)
n8 = node(8,n9)
n7 = node(7,n8)
n6 = node(6,n7)
n5 = node(5,n6)
n4 = node(4,n5)
n3 = node(3,n4)
n2 = node(2,n3)
n1 = node(1,n2)

l = [1,2,3,4]

t = l
while t != None :
    print(t)
    t = t.next
