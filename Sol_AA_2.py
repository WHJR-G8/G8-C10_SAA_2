import turtle
import random

l1=[10,20,30,40,50]
l2=[60,70,80,90,100,110]
l3=[]
colors=["red","green","black","blue","yellow","grey","cyan","orange"]

def draw_circle(l,c):
    for j in l:
        turtle.pencolor(random.choice(c))
        turtle.stamp()
        turtle.left(j)
        turtle.forward(60)
    
draw_circle(l1,colors)
draw_circle(l2,colors)

turtle.clear()

for i in range(len(l1)-1):
    l3.append(l1[i]+l2[i])
    
draw_circle(l3,colors)