class node:
    def __init__(self,data,left = None,right = None):
        self.data = data
        self.left = None if left is None else left
        self.right = None if right is None else right
    
    def __str__(self):
        return str(self.data)

def addi(root,data):
    if root is None:
        root = node(data)
    else:
        fp = None
        p = root
        while p:
            fp = p
            p = p.left if data < p.data else p.right    
        if fp.data > data:
            fp.left = node(data)
        else:
            fp.right = node(data)
    return root

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root, end = ' ')
        inOrder(root.right)

def add(root,data):
    if not root:
        return node(data)
    else:
        if data < root.data:
            root.left = add(root.left,data)
        else:
            root.right = add(root.right,data)
        return root

def printSideWay(root,level):
    if root:
        printSideWay(root.right,level + 1)
        print('   '*level,root)
        printSideWay(root.left,level + 1)

def height(root):
    if not root:
        return -1
    else:
        hl = height(root.left)
        hr = height(root.right)
        if hl > hr:
            return hl + 1
        else:
            return hr + 1

def path(root,data):
    if search(root,data) is not None:
        if data != root.data:
            print(root,end = ' ')
            if data < root.data:
                path(root.left,data)
            else:
                path(root.right,data)
        else:
            print(root)
    else:
        print("no path")

def search(root,data):
    if root is None:
        return None
    else:
        if data == root.data:
            return root
        elif data < root.data:
            return search(root.left,data)
        else:
            return search(root.right,data)

def depth(root,data):
    if search(root,data) is not None:
        if data == root.data:
            return 0
        elif data < root.data:
            return depth(root.left,data) + 1
        else:
            return depth(root.right,data) + 1
    else:
        return -1

def smallest(root):
    if root.left:
        return smallest(root.left)
    else:
        return root

l = [14,4,9,7,15,3,18,16,20,5,16,2]
print('intput : ',l)
r = None 
for ele in l:
    r = add(r, ele)
print('inorder :', end = ' ')
inOrder(r)
print()
print('printSideWay :')
printSideWay(r, 0)

print('height of ', r.data, '=', height(r))

d = 5
print('path :', d, '=', end = ' ')
path(r, d)

d = 9
t = search(r, d)
print(t)

d = 18
print('depth of node data ', d, '=', depth(r, d))

print('smallest data : ',smallest(r))