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
    for _ in range(3):
        t.forward(200)
        t.right (120)

def carre(longueur):
    for _ in range(4):
        t.forward(100)
        t.right(90)
        

def polygone(longueur, nb_cotes):
    for _ in range (nb_cotes):
        t.forward(longueur)
        t.right(360/nb_cotes)
    

polygone(100,7)
#equilateral (100)
#carre(100)
turtle.exitonclick()

    