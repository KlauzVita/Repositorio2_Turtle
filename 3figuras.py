import turtle
import time



def posicion(x, y): 
    turtle.penup() 
    turtle.setx(x)
    turtle.sety(y)
    turtle.pendown()


posicion(-100, 0)
for i in range(3): 
    turtle.forward(60)
    ang =+ 120
    turtle.left(ang)

posicion(0, 0)
for i in range(4): 
    turtle.forward(75)
    ang =+ 90
    turtle.left(ang)

posicion(150, 0)
for i in range(5): 
    turtle.forward(100)
    ang =+ 72
    turtle.left(ang)

time.sleep(3)


