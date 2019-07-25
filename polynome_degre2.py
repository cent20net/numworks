# En cours de création. livraison mi aout 2018
# Ce script sera expliqué et commenté en détail sur le site internet https://nsi.xyz/ (URL exacte à préciser après publication)
# Transfert automatique vers la NumWorks depuis https://workshop.numworks.com/python/cent20/polynome_degre2
# Auteurs : Arthur Jacquin, Kevin Fedyna, Vincent Robert.

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
    if c == int(c): c = int(c)
    calculer_trinome()
    
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
    x=round((-b)/(2*a),8)
    y=round((sqrt(abs(d)))/(2*a),8)
    return x,y

def afficher_menu_0():
    print("Polynôme (équation) de degré 2")
    if a!="a":
        expressionPolynome = "P(x)={}x^2".format(a)
        if b >= 0:
            expressionPolynome = expressionPolynome+"+{}x".format(b)
        if b<0:
            expressionPolynome = expressionPolynome+"{}x".format(b)
        if c >= 0:
            expressionPolynome = expressionPolynome+"+{}".format(c)
        if c<0:
            expressionPolynome = expressionPolynome+"{}".format(c)
        print(expressionPolynome)
    else:
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
        signe = ""
    menu_2 = "2. Discriminant = {} {} ".format(d,signe)
    print(menu_2)
    
def afficher_menu_3():
    x,y = definir_solutions()
    if d<0:
        print("3. Racines complexes conjuguées : 2 ")
        print("   z1= {} + {} i".format(x,y))
        print("   z2= {} - {} i".format(x,y))
        # Spoil Tale S
    elif d>0:
        x1=min(x+y,x-y)
        x2=max(x-y,x+y)
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
    menu_4 = "4. Signe "
    if d<0:
        if a<0:
            menu_4 = menu_4+"(-)"
        else:
            menu_4 = menu_4+"(+)"
    elif d==0:
        if a<0:
            menu_4 = menu_4+"(-0-)"
        else:
            menu_4 = menu_4+"(+0+)"
    else:
        if a<0:
            menu_4 = menu_4+"(-+-)"
        else:
            menu_4 = menu_4+"(+-+)"
    if a<0:
        menu_4 = menu_4+", extremum (M)"
    else:
        menu_4 = menu_4+", extremum (m)"
    # On insère pas les coordonnées ? (arthur)
    print(menu_4)

def afficher_menu_5():
    if d<0:
        menu_5="5. Factorisation dans les complexes"
        # Spoil Tale S
    elif d>=0:
        menu_5="5. Factorisation dans les réels"
    print(menu_5)
    
def afficher_menu_6():
    print("6. Quitter")
    
def executer_menu_1():
    afficher_menu_0()
    definir_trinome()
    # fini ! 
    
def executer_menu_2():
    afficher_menu_0()
    print("Calcul du discriminant:")
    print("Δ = b^2-4ac")
    for i in range(3):
        formuleDiscriminant = "Δ = "
        if i==0:
            if b<0:
                formuleDiscriminant = formuleDiscriminant+"({})^2-4*"
            else:
                formuleDiscriminant = formuleDiscriminant+"{}^2-4*"
            if a<0:
                formuleDiscriminant = formuleDiscriminant+"({})*"
            else:
                formuleDiscriminant = formuleDiscriminant+"{}*"
            if c<0:
                formuleDiscriminant = formuleDiscriminant+"({})"
            else:
                formuleDiscriminant = formuleDiscriminant+"{}"
            print(formuleDiscriminant.format(b,a,c))
        elif i==1:
            calcDis = 4*a*c
            if b<0:
                formuleDiscriminant = formuleDiscriminant+"({})^2"
            else:
                formuleDiscriminant = formuleDiscriminant+"{}^2"
            if calcDis<0:
                formuleDiscriminant = formuleDiscriminant+"+{}"
            else:
                formuleDiscriminant = formuleDiscriminant+"{}"
            calcDis = -1*calcDis
            print(formuleDiscriminant.format(b,calcDis))
        else:
            calcDis = b**2-4*a*c
            print(formuleDiscriminant+str(calcDis))
    # a faire - Donner les détail du calcul du discriminant

def executer_menu_3():
    afficher_menu_0()
    print("Calcul des racines:")
    x,y = definir_solutions()
    if d<0:
        print("z1 = -b/2a + √|Δ|/2a i")
        print("z1 = {}/2*{} + √{}/2*{} i".format(-b,a,-d,a))
        print("z1 = {}/{} + √{}/{} i".format(-b,2*a,-d,2*a))
        print("z1 = {} + {} i".format(x,y))
        print("z2 = -b/2a - √|Δ|/2a i")
        print("z2 = {}/{} - √{}/{} i".format(-b,2*a,-d,2*a))
        print("z2 = {} - {} i".format(x,y))
    else:
        print("x1 = (-b+√Δ)/2a")
        print("x1 = ({}+√{})/2*{}".format(-b,d,a))
        if d==0:
            print("x1 = {}/{}".format(-b,2*a))
        else:
            print("x1 = ({}+√{})/{}".format(-b,d,2*a))
        print("x1 = {}".format(x+y))
        print("x2 = (-b-√Δ)/2a")
        print("x2 = ({}-√{})/2*{}".format(-b,d,a))
        print("x2 = {}".format(x-y))
        
    # a faire - Donner les détail du calcul des racines

def executer_menu_4():
    afficher_menu_0()
    # a faire ... 
    # On peut faire très simple (texte), beau (tableau) + texte , complexe (couche graphique tableau de signe)

def executer_menu_5():
    afficher_menu_0()
    print("Factorisation:")
    x,y = definir_solutions()
    if x+y==int(x+y):
        x1 = int(x+y)
    else:
        x1 = x+y
    if x-y==int(x-y):
        x2 = int(x-y)
    else:
        x2 = x-y
    if d==0:
        print("P(x) = a(x-(-b/2a))^2")
        print("P(x) = {}(x-({}/2*{}))^2".format(a,-b,a))
        if x1<0:
            print("P(x) = {}(x+{})^2".format(a,-x1))
        elif x1>0:
            print("P(x) = {}(x{})^2".format(a,-x1))
        else:
            print("P(x) = {}x^2".format(a))
    elif d>0:
        print("P(x) = a(x-x1)(x-x2)")
        print("Avec :")
        print("a = {}".format(a))
        formuleFactorisation = "(x-x1) = (x"
        if x1<0:
            formuleFactorisation = formuleFactorisation+"+{})".format(-x1)
        elif x1>0:
            formuleFactorisation = formuleFactorisation+"{})".format(-x1)
        else:
            formuleFactorisation = formuleFactorisation+")"
        print(formuleFactorisation)
        formuleFactorisation = "(x-x2) = (x"
        if x2<0:
            formuleFactorisation = formuleFactorisation+"+{})".format(-x2)
        elif x2>0:
            formuleFactorisation = formuleFactorisation+"{})".format(-x2)
        else:
            formuleFactorisation = formuleFactorisation+")"
        print(formuleFactorisation)
    else:
        print("P(x) = a(z-z1)(z-z2)")
        print("Avec :")
        print("a = {}".format(a))
        formuleFactorisation = "(z-z1) = (z"
        if x<0:
            formuleFactorisation = formuleFactorisation+"+{}".format(-x)
        elif x>0:
            formuleFactorisation = formuleFactorisation+"{}".format(-x)
        if y<0:
            formuleFactorisation = formuleFactorisation+"+{}i)".format(-y)
        elif y>0:
            formuleFactorisation = formuleFactorisation+"{}i)".format(-y)
        print(formuleFactorisation)
        formuleFactorisation = "(z-z2) = (z"
        if x<0:
            formuleFactorisation = formuleFactorisation+"+{}".format(-x)
        elif x>0:
            formuleFactorisation = formuleFactorisation+"{}".format(-x)
        if y<0:
            formuleFactorisation = formuleFactorisation+"{}i)".format(y)
        elif y>0:
            formuleFactorisation = formuleFactorisation+"+{}i)".format(y)
        print(formuleFactorisation)
        
    # a faire : Factorisation formelle + formatage avec les valeurs approchées

def custom_input(variable_demande,pdif0 = 0,pint = 0,pbinf = "none",pbsup = "none"):
    global value
    if variable_demande != "none": print("{} =".format(str(variable_demande)))
    try: value = float(input())
    except:
        print("Entrez un numéro :")
        custom_input(variable_demande,pdif0,pint,pbinf,pbsup)
    if pdif0 == 1 and value == 0:
        print("La valeur doit être différente de zéro :")
        custom_input(variable_demande,pdif0,pint,pbinf,pbsup)
    if (pbinf != "none" and value < pbinf) or (pbsup != "none" and value > pbsup):
        print("La valeur doit être comprise entre {} et {} :".format(pbinf,pbsup))
        custom_input(variable_demande,pdif0,pint,pbinf,pbsup)
    elif (pint == 1 and int(value) != value):
        print("La valeur doit être entière :")
        custom_input(variable_demande,pdif0,pint,pbinf,pbsup)
    return optimiser(value)
    
def optimiser(value):
    global variable
    variable = [0,""]
    if value == int(value): variable[0] = int(value)
    else: variable[0] = value
    if variable[0] >= 0: variable[1] = str(variable[0])
    else: variable[1] = "({})".format(str(variable[0]))
    variable[0] = float(variable[0])
    return variable




# 3 lignes à effacer qd le menu sera fini > ce code devra être intégré dans le menu > Arthur
def menu():
    for i in range(7):
        eval("afficher_menu_{}()".format(i))
    custom_input("none",pint = 1,pbinf = 1,pbsup = 6)
    if variable[0]!=6:
        eval("executer_menu_{}()".format(int(variable[0])))
        if variable[0]!=1: input()
        menu()

# 4 lignes à effacer qd le menu sera fini
afficher_menu_0()
definir_trinome()
menu()


    