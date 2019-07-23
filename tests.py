from math import sqrt

a,b,c,d="a","b","c","d"

def calculer():
    trinome_discriminant()
    trinome_nb_solutions()
    trinome_solutions()    

def trinome_definir():
    global a,b,c
    a=0
    while a==0 :
        a=float(input('a = '))
    b=float(input('b = '))
    c=float(input('c = '))
    
def trinome_discriminant():
    global d
    d=float(b**2-4*a*c)

def trinome_nb_solutions():
    if d==0:
        return(1)
    else:
        return(2)
        
def trinome_solutions():
    x=(-b)/(2*a)
    y=(sqrt(abs(d)))/(2*a)
    if d==0:
        return x,x
    elif d>0:
        [x1,x2]=sorted([x+y,x-y])
    else:
        z1=complex(x,-y)
        z2=complex(x,y)
        return z1,z2

def afficher_menu_0():
    print("Polynôme (équation) de degré 2")
    print("P(x)={}x^2+{}x+{} (=0)".format(a,b,c))
    print("")  

def afficher_menu_1():
    menu_1 = "1. Changer les valeurs a,b,c"
    print(menu_1)

def afficher_menu_2():       
    if d<0:
        signe = "<0"
    elif d>0:
        signe = ">0"
        menu_2 = "2. Delta = b^2-4ac ={} {} ".format(d,signe)
    print(menu_2)


def afficher_menu_sommaire():
    calculer() 
    for i in range(3):
        eval("afficher_menu_{}()".format(i))

# il reste la boucle principale à faire, elle gère l'affichage du menu principale et l'éxécution des différents choix du menu
# ça commence par 
afficher_menu_0()
trinome_definir()
calculer()
afficher_menu_sommaire()
