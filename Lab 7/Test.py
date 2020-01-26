class stack:
    def __init__(self,l = None):
        if l is None:
            self.items = []
        else:
            self.items = l
        self.size = len(self.items)
    
    def push(self,data):
        self.items.append(data)
        self.size += 1

    def pop(self):
        self.size -= 1
        return self.items.pop() 
    
    def peek(self):
        return self.items[-1]
    
    def isEmpty(self):
        return self.items == []
    
    def getSize(self):
        return self.size
    
    def __str__(self):
        s = ''
        for ele in self.items:
            s += str(ele) + ' '
        return s

class node:
    def __init__(self,data,left = None,right = None):
        self.data = data
        self.left = None if left is None else left
        self.right = None if right is None else right

    def __str__(self):
        return str(self.data)

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root,end = ' ')
        inOrder(root.right)

def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root,end = ' ')

def preOrder(root):
    if root:
        print(root,end = ' ')
        preOrder(root.left)
        preOrder(root.right)

l = []

s = str(input("Enter postflix : "))
for ele in s:
    if ele is not ' ':
        l.append(ele)
        
print(l)
stck = stack()

while l:
    if l[0] not in '+-*/%':
        stck.push(node(l.pop(0)))
    else:
        tmp = node(l.pop(0))
        tmp.right = stck.pop()
        tmp.left = stck.pop()
        stck.push(tmp)

inOrder(stck.peek())
print()
postOrder(stck.peek())
print()
preOrder(stck.peek())