from math import sqrt

a,b,c,d="a","b","c","d"

def calculer():
    trinome_discriminant()
    trinome_nb_solutions()
    trinome_solutions()

def definir_variables():
    global a,b,c
    if a == int(a): a = int(a)
    if b == int(b): b = int(b)
    if c == int(c): c = int(c)    

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
    global nb
    if d==0:
        nb=1
    else:
        nb=2
        
def trinome_solutions():
    x=(-b)/(2*a)
    y=(sqrt(abs(d)))/(2*a)
    return x,y    

def afficher_menu_0():
    print("Polynôme (équation) de degré 2")
    print("P(x)={}x^2+{}x+{} (=0)".format(a,b,c))
    print("")  

def afficher_menu_1():
    menu_1 = "1. Changer les valeurs a,b,c"
    print(menu_1)

def afficher_menu_2():
    global d
    if d == int(d): d = int(d) 
    if d<0:
        signe = "<0"
    elif d>0:
        signe = ">0"
    elif d==0:
        signe = "1"
    menu_2 = "2. Discriminant = {} {} ".format(d,signe)
    print(menu_2)
    
def afficher_menu_3():
    x,y = trinome_solutions()
    if d<0:
        print("3. Racines complexes conjuguées : {} ".format(nb))
        print("   z1= {} + {} i".format(x,y))
        print("   z2= {} - {} i".format(x,y))
    elif d>0:
        x1=x+y
        x2=x-y        
        print("3. Racines réelles distinctes : {} ".format(nb))
        print("   x1= {}".format(x1))
        print("   x2= {}".format(x2))
    elif d==0:
       print("3. Racine réelle double : {} ".format(nb))
       print("   x1=x2= {}".format(x))

def afficher_menu_sommaire():
    calculer() 
    for i in range(4):
        eval("afficher_menu_{}()".format(i))

trinome_definir()
calculer()
definir_variables()
afficher_menu_sommaire()
