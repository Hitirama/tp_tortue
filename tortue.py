import turtle
s = turtle.getscreen()
t = turtle.Turtle()
t.speed(0) # maximum speed

#t.forward(100)
#t.left(90)
#t.forward(50)
#t.right(90)
#t.forward(100)

def equilateral(longueur):
    for triangle in range(3):
        t.forward(200)
        t.right (120)

def carre(longueur):
    for carre in range(4):
        t.forward(100)
        t.right(90)
equilateral (100)
carre(100)
turtle.exitonclick()

    