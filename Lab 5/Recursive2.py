def printlistForw(l):
    if len(l) == 0:
        return 0
    else:
        print(l[0], end = ' ')
        printlistForw(l[1:])

def printList(l):
    if l != []:
        print(l[0],end = ' ')
        printList(l[1:])

price = [20,10,5,5,3,2,20,10]
N = len(price)
k = 20

def pick(cart, k, ip):
    global price
    if ip < len(price): 
        if k < price[ip]: 
            pick(cart, k, ip + 1) 
        else: 
            k -= price[ip] 
            cart.append(price[ip]) 
            if k == 0: 
                printList(cart)
                print()
            else: 
                pick(cart, k, ip + 1)
            pick(cart, k + cart.pop(), ip + 1)

pick([],k,0) 