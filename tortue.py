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
    polygone(longueur,3)

def carre(longueur):
    polygone(longueur,4) 

def polygone(longueur, nb_cotes,color):
    t.color(color)
    for _ in range(nb_cotes):
        t.forward(longueur)
        t.right(360/nb_cotes)
        
def figure_1(longueur,diff,rep,color):
    t.color(color)
    for _ in range(rep):
        for _ in range (4):
            t.forward(longueur)
            t.left(90)
        longueur = longueur + diff
        t.left(10)
def figure_2 (longueur,nb_cotes,rep,diff,color):
    t.color(color)
    for _ in range (rep):
        t.forward (longueur)
        t.left(90)
        longueur = longueur + diff
        t. left (10)
def figure_3 (longueur, nb_cotes, rep, color):
    t.color(color)
    for _ in range (rep):
        t.forward(longueur)
        t.left(360/nb_cotes)
        longueur = longueur + 5
        t.forward(longueur)
        t.left(88)
        
figure_3(10,4,100,"red")
figure_2(5,4,100,2,"blue")      
figure_1(50,10,50,"pink")
polygone(100,12,"green")
turtle.exitonclick()

    