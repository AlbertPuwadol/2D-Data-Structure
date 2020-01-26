class LinkedList:
    class Node:
        def __init__(self,data,next = None):
            self.data = data
            if next == None:
                self.next = None
            else:
                self.next = next

    def __init__(self):
        self.head = None

    def __str__(self):
        if self.head == None:
            return str(self.head)
        else:
            t = self.head
            res = ''
            while t.next != None:
                res = res + str(t.data) + ' ' 
                t = t.next
            res = res + str(t.data) + ' ' 
            return res

    def __len__(self):
        if self.head == None:
            return 0
        else:
            t = self.head
            size = 1
            while t.next != None:
                size += 1
                t = t.next
            return size

    def append(self,data):
        if self.head == None:
            self.head = self.Node(data)
        else:
            t = self.head
            while t.next != None:
                t = t.next
            t.next = self.Node(data)

    def remove(self,data):
        if self.head == None:
            return None
        else:
            t = self.head
            pre = None
            while t.data != data and t.next != None:
                pre = t
                t = t.next
            if data == t.data:
                if pre == None:
                    self.head = t.next
                    return t.data
            else:
                pre.next = t.next
                return t.data
            return None

    def isEmpty(self):
        return self.head == None

    def add(self,data):
        if self.head == None:
            self.append(data)
        else:
            t = self.head
            while data > t.data and t.next != None:
                pre = t
                t = t.next
            if t.next == None and data >= t.data:
                t.next = self.Node(data)
            elif t == self.head:
                self.head = self.Node(data,t)
            else:
                pre.next = self.Node(data,pre.next)

    def mean(self):
        if self.head == None:
            return 0
        else:
            t = self.head
            sum  = 0
            while t.next != None:
                sum += t.data
                t = t.next
            sum += t.data
            if (sum/self.__len__()*100)%10 == 0:
                return sum/self.__len__()
            else:
                return str(round(sum/self.__len__(), 2))

    def mode(self):
        if self.head == None:
            return None
        else:
            t = self.head
            pre = t.data
            count = 0
            most = 0
            m = ''
            while t.next != None:
                if t.data == pre:
                    count += 1
                else:
                    if count > most:
                        m = (str)(pre)
                        most = count
                    elif count == most:
                        m = m + ", " + (str)(pre)
                    count = 1
                    pre = t.data
                t = t.next
            if t.data == pre:
                count += 1
            if count > most:
                m = (str)(pre)
            return m

    def med(self):
        if self.head == None:
            return None
        else:
            mid = self.__len__()//2
            t = self.head
            if self.__len__() % 2 == 0:
                for i in range(1,mid):
                    t = t.next
                if ((t.data + t.next.data)*5) % 10 == 0:
                    return str((t.data + t.next.data)/2)
                else:
                    return str(round((t.data + t.next.data)/2, 1))
            else:
                for i in range(0,mid):
                    t = t.next
            return str(round(t.data, 1))

l = LinkedList()

message = input("Enter 12 Number : ")
i = 0
while i < len(message):
    if message[i] != ' ':
        data = 0
        while i < len(message) and message[i] != ' ':
            data = data*10 + (int)(message[i])
            i += 1
        l.add(data)
    i += 1
print("Output : ")
print("LinkedList data : ",l)
print("Mean = ", l.mean())
print("Mode = ",l.mode())
print("Median = ",l.med())
