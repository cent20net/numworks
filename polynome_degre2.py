# En cours de création. livraison mi aout 2018
# Ce script sera expliqué et commenté en détail sur le site internet https://nsi.xyz/ (URL exacte à préciser après publication)
# Transfert automatique vers la NumWorks depuis https://workshop.numworks.com/python/cent20/polynome_degre2
# Auteurs : Arthur Jacquin, Kevin Fedyna, Vincent Robert.

from math import sqrt
import sys

a,b,c="a","b","c"

def def_trinome():
    global a,b,c
    a=0
    while a==0 :
        a=float(input('a = '))
    b=float(input('b = '))
    c=float(input('c = '))
    if a == int(a): a = int(a)
    if b == int(b): b = int(b)
    if c == int(c): c = int(c)
    calc_delta()
    calc_nb_sol()
    def_solutions()
    
def calc_delta():
    global d
    d=float(b**2-4*a*c)
    if d == int(d): d = int(d) 

def calc_nb_sol():
    global nb
    if d==0:
        nb=1
    else:
        nb=2
        # Spoil Tale S
        
def def_solutions():
    x=round((-b)/(2*a),8)
    y=round((sqrt(abs(d)))/(2*a),8)
    return x,y

def aff_menu_0():
    print("Polynôme (équation) de degré 2")
    if a!="a":
        exp_poly = "P(x)={}x^2".format(a)
        if b >= 0:
            exp_poly = exp_poly+"+{}x".format(b)
        if b<0:
            exp_poly = exp_poly+"{}x".format(b)
        if c >= 0:
            exp_poly = exp_poly+"+{}".format(c)
        if c<0:
            exp_poly = exp_poly+"{}".format(c)
        print(exp_poly)
    else:
        print("P(x)={}x^2+{}x+{} (=0)".format(a,b,c))
    print("")  

def aff_menu_1():
    menu_1 = "1. Changer les valeurs a,b,c"
    print(menu_1)
    # on pourrait réduire ces deux lignes mais on perd un interêt pédagogique

def aff_menu_2():
    global d
    if d<0:
        signe = "<0"
    elif d>0:
        signe = ">0"
    elif d==0:
        signe = ""
    menu_2 = "2. Discriminant = {} {} ".format(d,signe)
    print(menu_2)
    
def aff_menu_3():
    x,y = def_solutions()
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

def aff_menu_4():
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
    # On insère pas les coordonnées ? (arthur) > Si à ajouter ! (vincent)
    print(menu_4)

def aff_menu_5():
    if d<0:
        menu_5="5. Factorisation dans les complexes"
        # Spoil Tale S
    elif d>=0:
        menu_5="5. Factorisation dans les réels"
    print(menu_5)
    
def aff_menu_6():
    print("6. Quitter")
    
def exec_menu_1():
    aff_menu_0()
    def_trinome()
    # fini ! 
    
def exec_menu_2():
    aff_menu_0()
    print("Calcul du discriminant:")
    print("Δ = b^2-4ac")
    for i in range(3):
        delta = "Δ = "
        if i==0:
            if b<0:
                delta = delta+"({})^2-4*"
            else:
                delta = delta+"{}^2-4*"
            if a<0:
                delta = delta+"({})*"
            else:
                delta = delta+"{}*"
            if c<0:
                delta = delta+"({})"
            else:
                delta = delta+"{}"
            print(delta.format(b,a,c))
        elif i==1:
            calcDis = 4*a*c
            if b<0:
                delta = delta+"({})^2"
            else:
                delta = delta+"{}^2"
            if calcDis<0:
                delta = delta+"+{}"
            else:
                delta = delta+"{}"
            calcDis = -1*calcDis
            print(delta.format(b,calcDis))
        else:
            calcDis = b**2-4*a*c
            print(delta+str(calcDis))

def exec_menu_3():
    aff_menu_0()
    print("Calcul des racines:")
    x,y = def_solutions()
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

def exec_menu_4():
    aff_menu_0()
    # kevin ?

def exec_menu_5():
    aff_menu_0()
    print("Factorisation:")
    x,y = def_solutions()
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
        fact = "(x-x1) = (x"
        if x1<0:
            fact = fact+"+{})".format(-x1)
        elif x1>0:
            fact = fact+"{})".format(-x1)
        else:
            fact = fact+")"
        print(fact)
        fact = "(x-x2) = (x"
        if x2<0:
            fact = fact+"+{})".format(-x2)
        elif x2>0:
            fact = fact+"{})".format(-x2)
        else:
            fact = fact+")"
        print(fact)
    else:
        print("P(x) = a(z-z1)(z-z2)")
        print("Avec :")
        print("a = {}".format(a))
        fact = "(z-z1) = (z"
        if x<0:
            fact = fact+"+{}".format(-x)
        elif x>0:
            fact = fact+"{}".format(-x)
        if y<0:
            fact = fact+"+{}i)".format(-y)
        elif y>0:
            fact = fact+"{}i)".format(-y)
        print(fact)
        fact = "(z-z2) = (z"
        if x<0:
            fact = fact+"+{}".format(-x)
        elif x>0:
            fact = fact+"{}".format(-x)
        if y<0:
            fact = fact+"{}i)".format(y)
        elif y>0:
            fact = fact+"+{}i)".format(y)
        print(fact)

def menu_input(var_dem,pdif0 = 0,pint = 0,inf = "rien",sup = "rien"):
    global choix
    if var_dem != "rien": print("{} =".format(str(var_dem)))
    try: choix = float(input())
    except:
        print("Entrez un chiffre :")
        menu_input(var_dem,pdif0,pint,inf,sup)    
    if (inf != "rien" and choix < inf) or (sup != "rien" and choix > sup):
        print("La valeur doit être un entier entre {} et {} :".format(inf,sup))
        menu_input(var_dem,pdif0,pint,inf,sup)
    elif (pint == 1 and int(choix) != choix):
        print("La valeur doit être entière :")
        menu_input(var_dem,pdif0,pint,inf,sup)
    
def optimiser(v):
    if v == int(v): v = int(v)
    return v

def menu():
    for i in range(7):
        eval("aff_menu_{}()".format(i))
    menu_input("rien",pint = 1,inf = 1,sup = 6)
    if choix!=6:
        eval("exec_menu_{}()".format(int(choix)))
        if choix!=1: input()
        menu()

aff_menu_0()
def_trinome()
menu()

s=0
for name in dir():
    print("nom var = "+name)
    print(globals()[name])
    print(sys.getsizeof(globals()[name]))
    s=s+sys.getsizeof(globals()[name])
    print(s)
  
    
