class BST:
    class node:
        def __init__(self,data,left = None,right = None):
            self.data = data
            self.left = None if left is None else left
            self.right = None if right is None else right

        def __str__(self):
            return str(self.data)

        def getData(self):
            return self.data

        def getLeft(self):
            return self.left
    
        def getRight(self):
            return self.right

        def setData(self,data):
            self.data = data
    
        def setLeft(self,left):
            self.left = left

        def setRight(self,right):
            self.right = right

    def __init__(self, root = None):
        self.root = None if root is None else root

    def addI(self,data):
        if self.root is None:
            self.root = self.node(data)
        else:
            fp = None
            p = self.root
            while p:
                fp = p
                p = p.getLeft() if data < p.getData() else p.getRight()

            if fp.getData() > data: 
                fp.setLeft(self.node(data))
            else:
                fp.setRight(self.node(data))
    
    def inOrder(self):
        BST._inOrder(self.root)
        print()

    def _inOrder(root):
        if root:
            BST._inOrder(root.getLeft())
            print(root, end = ' ')
            BST._inOrder(root.getRight())

    def add(self,data):
        self.root = BST._add(self.root,data)

    def _add(root,data):
        if not root:
            return BST.node(data)
        else:
            if data < root.getData():
                root.setLeft(BST._add(root.getLeft(),data))
            else:
                root.setRight(BST._add(root.getRight(),data))
            return root

    def printSideway(self):
        BST._printSideway(self.root,0)
        print()

    def _printSideway(root,level):
        if root:
            BST._printSideway(root.getRight(),level + 1)
            print('   '*level,root)
            BST._printSideway(root.getLeft(),level + 1)

    def preOrder(self):
        BST._preOrder(self.root)
        print()

    def _preOrder(root):
        if root:
            print(root, end = ' ')
            BST._preOrder(root.getLeft())
            BST._preOrder(root.getRight())

    def postOrder(self):
        BST._postOrder(self.root)
        print()

    def _postOrder(root):
        if root:
            BST._postOrder(root.getLeft())
            BST._postOrder(root.getRight())
            print(root, end = ' ')

    def search(self,data):
        return BST._search(self.root,data)

    def _search(root,data):
        if root is None:
            return None
        else:
            if data == root.getData():
                return root
            elif data < root.getData():
                return BST._search(root.getLeft(),data)
            else:
                return BST._search(root.getRight(),data)

    def path(self,data):
        if self.search(data) is None:
            print("No path")
        else:
            BST._path(self.root,data)
            print()

    def _path(root,data):
        if data == root.getData():
            print(root,end = ' ')
            if BST._search(root.getRight(),data) is not None:
                BST._path(root.getRight(),data)
        elif data < root.getData():
            print(root,end = ' ')
            BST._path(root.getLeft(),data)
        else:
            print(root,end = ' ')
            BST._path(root.getRight(),data)
        
    def delete(self,data):
        if self.search(data) is not None:
            self.root = BST._delete(self.root,data)
    
    def _delete(root,data):
        if data == root.getData():
            if root.getLeft() is not None and root.getRight() is not None:
                fp = root
                p = root.getRight()
                while p.getLeft() is not None:
                    fp = p
                    p = p.getLeft()
                root.setData(p.getData())
                if fp == root:
                    fp.setRight(p.getRight())
                else:
                    fp.setLeft(None)
            elif root.getLeft() is None and root.getRight() is None:
                root = None
            elif root.getLeft() is None:
                root.setData(root.getRight().getData())
                p = root.getRight()
                root.setRight(p.getRight())
                root.setLeft(p.getLeft())
            else:
                root.setData(root.getLeft().getData())
                p = root.getLeft()
                root.setLeft(p.getLeft())
                root.setRight(p.getRight())
        elif data < root.getData():
            root.setLeft(BST._delete(root.getLeft(),data))
        else:
            root.setRight(BST._delete(root.getRight(),data))
        return root

l = [14,4,9,7,15,3,18,16,20,5,17,16,15]
print(l)
t = BST()
for ele in l:
    t.addI(ele)
t.inOrder()
t.preOrder()
t.postOrder()
t.printSideway()
s = int(input("Search : "))
print(t.search(s))
p = int(input("Path : "))
t.path(p)
d = int(input("Delete : "))
t.delete(d)
t.printSideway()
t.inOrder()