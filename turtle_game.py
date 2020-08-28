from turtle import *
from random import randint

screen = Screen()
screen.setup(820,520)
screen.bgcolor('black')


color('white')
speed(0)
penup()  #remove the drawing of the pen
goto(-140, 140)     #the turtle starts at the middle of the screen(0, 0)

for step in range(16):
    write(step, align='center')
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)


#Adding 1st turtle
ada = Turtle()
ada.color('red')
ada.shape('turtle')

ada.penup()
ada.goto(-160, 100)
ada.pendown()


#Adding 2nd turtle
bob = Turtle()
bob.color('blue')
bob.shape('turtle')

bob.penup()
bob.goto(-160, 70)
bob.pendown()


#Adding 3rd turtle
viv = Turtle()
viv.color('green')
viv.shape('turtle')

viv.penup()
viv.goto(-160, 40)
viv.pendown()



#Adding 4th turtle
art = Turtle()
art.color('yellow')
art.shape('turtle')

art.penup()
art.goto(-160, 10)
art.pendown()



for turn in range(100):
    ada.forward(randint(1,5))
    bob.forward(randint(1,5))
    viv.forward(randint(1,5))
    art.forward(randint(1,5))
    
    
    
