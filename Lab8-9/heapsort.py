from math import log2
from math import floor
class BST:
    class node:
        def __init__(self,data,left = None,right = None,father = None):
            self.data = data
            self.left = None if left is None else left
            self.right = None if right is None else right
            self.father = None if father is None else father

        def __str__(self):
            return str(self.data)

    def __init__(self, root = None):
        self.root = None if root is None else root

    def printSideway(self):
        BST._printSideway(self.root,0)

    @staticmethod
    def _printSideway(root,level):
        if root:
            BST._printSideway(root.right,level + 1)
            print('   '*level,root)
            BST._printSideway(root.left,level + 1)

    def insert(self,data):
        if not self.root:
            self.root = BST.node(data,None,None,None)
        else:
            q = []
            q.append(self.root)
            while q:
                n = q.pop(0)
                if not n.left or not n.right:
                    if not n.left:
                        n.left = BST.node(data,None,None,n)
                        m = n.left
                    elif not n.right:
                        n.right = BST.node(data,None,None,n)
                        m = n.right
                    while m.father and m.data < m.father.data :
                        m.data, m.father.data = m.father.data, m.data
                        m = m.father
                    q = []
                else:
                    if n.left:
                        q.append(n.left)
                    if n.right:
                        q.append(n.right)
    
    def deleteMin(self,last):
        tmp = self.findLast(self.root,last)
        print('deleteMin = ',self.root.data,'FindPlaceFor ',tmp.data)
        asc.append(self.root.data)
        self.root.data,tmp.data = tmp.data,self.root.data
        m = self.root
        while m.left or m.right:
            if m.left and m.right  and m.left.data not in asc and m.right.data not in asc:
                if m.left.data < m.data and m.left.data < m.right.data:
                    m.left.data,m.data = m.data,m.left.data
                    m = m.left
                elif m.right.data < m.data and m.right.data < m.left.data:
                    m.right.data,m.data = m.data,m.right.data
                    m = m.right
                else:
                    break
            else:
                if m.left.data < m.data and m.left.data not in asc:
                    m.left.data,m.data = m.data,m.left.data
                    m = m.left
                else:
                    break
        
    @staticmethod
    def findLast(root,last):
        q = []
        q.append(root)
        i = 0
        while i != last:
            n = q.pop(0)
            i += 1
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
        return n
    
    def printLevel(self):
        e = []
        e.append(self.root)
        while e:
            n = e.pop(0)
            print(n,end = ' ')
            if n.left:
                e.append(n.left)
            if n.right:
                e.append(n.right)
        print()

def print90(h, i, max_i):
    if i < max_i:
        indent = floor(log2(i+1))
        print90(h, (i*2)+2, max_i)
        print('   ' * indent, h[i])
        print90(h, (i*2)+1, max_i)

a = [25,15,10,4,12,22,18,24,50,35,31,44,70,66,90]
print(a)
print90(a,0,len(a))
b = BST()
for i in a:
    b.insert(i)
    print("insert", i)
    b.printLevel()
    b.printSideway()
    print('------------------')

asc = []
for i in range(len(a),0,-1):
    b.deleteMin(i)
    b.printLevel()
    b.printSideway()

for i in asc:
    print(i,end = ' ')