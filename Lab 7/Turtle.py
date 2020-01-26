from turtle import *
size=800
min=64
pf=0.8660254 # Pythagoras factor: sqrt(3)/2

def S(l,x,y):
    if l>min: # Not done yet?
        l=l/2 # scale down by 2
        S(l,x,y) # bottom left triangle
        S(l,x+l,y) # bottom right triangle
        S(l,x+l/2,y+l*pf) # top triangle
    else: # Done recursing
        goto(x,y); pendown() # start at (x,y)
        begin_fill() # prepare to fill triangle
        forward(l); left(120) # triangle base
        forward(l); left(120) # triangle right
        forward(l) # triangle left
        end_fill()
        setheading(0) # face East
        penup(); goto(x,y) # finish at (x,y)
        
penup()
speed('fastest')
S(size,-size/2,-size*pf/2.0)
done()