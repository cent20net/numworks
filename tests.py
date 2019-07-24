from math import sqrt

a,b,c="a","b","c" #ne sert que pour le premier affichage de afficher_menu_0()

def calculer_trinome():
    calculer_discriminant()
    calculer_nb_solutions()
    definir_solutions()

def definir_trinome():
    global a,b,c
    a=0
    while a==0 :
        a=float(input('a = '))
    b=float(input('b = '))
    c=float(input('c = '))
        if a == int(a): a = int(a)
    if b == int(b): b = int(b)
    if c == int(c): c = int(c
    
def calculer_discriminant():
    global d
    d=float(b**2-4*a*c)
    if d == int(d): d = int(d) 

def calculer_nb_solutions():
    global nb
    if d==0:
        nb=1
    else:
        nb=2
        # Spoil Tale S
        
def definir_solutions():
    x=(-b)/(2*a)
    y=(sqrt(abs(d)))/(2*a)
    return x,y    

def afficher_menu_0():
    print("Polynôme (équation) de degré 2")
    # A Améliorer, 2x^2+3x+-2 est une anomalie, l'astuce d'Arthur +(-2) n'est guère meilleure 
    print("P(x)={}x^2+{}x+{} (=0)".format(a,b,c))
    
    print("")  

def afficher_menu_1():
    menu_1 = "1. Changer les valeurs a,b,c"
    print(menu_1)
    # on pourrait réduire ces deux lignes mais on perd un interêt pédagogique

def afficher_menu_2():
    global d
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
        print("3. Racines complexes conjuguées : 2 ")
        print("   z1= {} + {} i".format(x,y))
        print("   z2= {} - {} i".format(x,y))
        # Spoil Tale S
    elif d>0:
        x1=round(x+y,8)
        x2=round(x-y,8)
        if x1 == int(x1): x1 = int(x1)
        if x2 == int(x2): x2 = int(x2)  
        print("3. Racines réelles distinctes : 2 ")
        print("   x1= {}".format(x1))
        print("   x2= {}".format(x2))
    elif d==0:
       if x == int(x): x = int(x)
       print("3. Racine réelle double : 1 ")
       print("   x1=x2= {}".format(x))

def afficher_menu_4():
    menu_4 = "4. Signe et extremum"
    # A Améliorer, afficher "Signe (+-+), extremum (m)" est préférable dans le menu
    # 6 cas possibles : +-+ -+- +0+ -0- + - plus (M) ou (m)
    print(menu_4)

def afficher_menu_5():
    if d<0:
        menu_5="5. Factorisation dans les complexes"
        # Spoil Tale S
    elif d>=0:
        menu_5="5. Factorisation dans les réels"
    print(menu_5)
    
def executer_menu_1():
    afficher_menu_0()
    definir_trinome()   
    # fini ! 
    
def executer_menu_2():
    afficher_menu_0()
    # a faire - Donner les détail du calcul du discriminant

def executer_menu_3():
    afficher_menu_0()
    # a faire - Donner les détail du calcul des racines

def executer_menu_4():
    afficher_menu_0()
    # a faire ... 
    # On peut faire très simple (texte), beau (tableau) + texte , complexe (couche graphique tableau de signe)

def executer_menu_5():
   afficher_menu_0()
    # a faire : Factorisation formelle + formatage avec les valeurs approchées

def afficher_menu_sommaire():
    for i in range(6):
        eval("afficher_menu_{}()".format(i))

afficher_menu_0()
definir_trinome()
calculer_trinome()
afficher_menu_sommaire()

# il manque le menu qui sert les fonctions d'affichage et d'éxécution ... S'inspirer de celui d'arthur
