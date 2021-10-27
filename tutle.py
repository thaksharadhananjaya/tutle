from turtle import Turtle

t= Turtle()
t.speed(-100)
b=280

for c in range(1):
    a=1*c
    for i in range(100):
        t.circle(i,a)
        t.right(b)
        t.circle(i,a)
        t.right(b)
        t.circle(i,a)
        t.right(b)
        t.circle(i,a)

input()
