import random
import turtle
t = turtle.Turtle()

#firework color
'''กำหนดปากกา'''
def pen(color):
    t.color(color)

def rdColor():
    '''กำหนดสีีปากกา'''
    hexadecimal = ["#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])]
    print("A Random color is :",hexadecimal)
    return hexadecimal

def move():
    t.penup()
    x = random.randint(-165,165)
    y = random.randint(-165,165)
    t.goto(x,y)
    t.pendown()

def sky(colour):
     wn = turtle.Screen()
     wn.bgcolor(colour)

sky('black')

def firework(size):
    for num in range (20):
         t.fd(size)
         t.rt(180-(360/20))

def rz():
    '''Random Size'''
    s = random.randint(50,200)
    return s

for i in range(20):
    pen(rdColor())
    firework(rz())
    move()
    pen(rdColor())
    firework(rz())
    move()
    pen(rdColor())
    firework(rz())
    firework(rz())
    move()
