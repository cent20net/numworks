# computing. ready august 2019
# https://nsi.xyz/
# https://workshop.numworks.com/python/cent20/polynome_degre2
# Auteurs : Arthur Jacquin, Kevin Fedyna, Vincent Robert.

from math import sqrt
import sys

# O = optimiser
P = print

a, b, c = 0, 0, 0


def def_calc_trinome():
    global a, b, c, d, e, nb, x, y, x1, x2
    while a == 0:
        a = O(float(input('a = ')))
    b = O(float(input('b = ')))
    c = O(float(input('c = ')))
    d = O(float(b**2 - 4 * a * c))
    e = O(float(a * (-b / (2 * a))**2 + b * (-b / (2 * a)) + c))
    if d == 0:
        nb = 1
    else:
        nb = 2
    x = O((-b) / (2 * a))
    y = O((sqrt(abs(d))) / (2 * a))
    x1 = O(min(x + y, x - y))
    x2 = O(max(x - y, x + y))


def aff_entete():
    O(9, br=1)
    P("Polynome (equation) de degre 2")
    if a == 0:
        P("P(x)=ax^2+bx+c (=0)")
    else:
        P("P(x)={}{}{} (=0)".format(O(a, ap="x^2", r=4),O(b, p=1, ap="x", r=4, naf=1),O(c, p=1, r=4, naf=1)))
        P("")


def aff_menu():
    # Choix 1
    P("1. Changer les valeurs a,b,c")
    # Choix 2
    if d < 0:
        s = "< 0"
    elif d > 0:
        s = "> 0"
    elif d == 0:
        s = ""
    P("2. Discriminant = {} {} ".format(d, s))
    # Choix 3
    if d < 0:
        P("3. Racines complexes conjuguees : 2 ")
        P("   z1= {} + {} i".format(x, y))
        P("   z2= {} - {} i".format(x, y))
    elif d > 0:
        P("3. Racines reelles distinctes : 2 ")
        P("   x1= {}".format(x1))
        P("   x2= {}".format(x2))
    elif d == 0:
        P("3. Racine reelle double : 1 ")
        P("   x1=x2= {}".format(x))
    # Choix 4
    if d < 0:
        if a < 0:
            P("4. Signe : -", end=" ")
        else:
            P("4. Signe : +", end=" ")
    elif d == 0:
        if a < 0:
            P("4. Signe : -0-", end=" ")
        else:
            P("4. Signe : +0+", end=" ")
    else:
        if a < 0:
            P("4. Signe : -+-", end=" ")
        else:
            P("4. Signe : +-+", end=" ")
    if a < 0:
        P(", extremum : M")
    else:
        P(", extremum : m")
    # Choix 5
    if d < 0:
        P("5. Factorisation dans les complexes")
    elif d >= 0:
        P("5. Factorisation dans les reels")
        # Choix 6
    P("6. Quitter")


def exec_menu(i):
    global a, b, c, d, x, y
    aff_entete()
    if i == 1:
        a, b, c = 0, 0, 0
        def_calc_trinome()
    elif i == 2:
        # Arthur
        P("2. Calcul du discriminant :")
        P("")
        P("d = b^2 + 4*a*c")
        P("  = {}^2 + 4*{}*{}".format(O(b,par=1),O(a,par=1),O(c,par=1)))
        if b == 0 and c != 0:
            P(O(4*a*c,av="  = "))
        else:
            P("  = {}{}".format(O(b**2),O(4*a*c,p=1,naf=1)))
            if c != 0:
                P(O(d,av="  = "))
        P("")
        P(O(d,av="d = "), end=" ")
        if d == 0:
            P("")
        elif d < 0:
            P("< 0")
        elif d > 0:
            P("> 0")
        if b != 0 and c != 0:
            P("")
    elif i == 3:
        # Arthur
        P("3. Calcul des racines :")
        P("")
        if d < 0:
            P("d < 0 donc il existe")
            P("2 racines complexes conjugees")
            P("telles que :")
            P("")
            P("z1 = -b/2a + sqrt(|d|)/2a i")
            P("z2 = -b/2a - sqrt(|d|)/2a i")
        elif d == 0:
            P("d = 0 donc il existe")
            P("1 racine reelle double")
            P("telle que :")
            P("")
            P("x1 = x2 = -b/2a")
            P("")
        elif d > 0:
            P("d > 0 donc il existe")
            P("2 racines reelles distinctes")
            P("telles que :")
            P("")
            if a > 0:
                P("x1 = (-b-sqrt(d))/(2a)")
                P("x2 = (-b+sqrt(d))/(2a)")
            else:
                P("x1 = (-b+sqrt(d))/(2a)")
                P("x2 = (-b-sqrt(d))/(2a)")
        input()
        aff_entete()
        P("3. Calcul des racines :")
        P("")
        if d < 0:
            P("z1 = -b/2a + sqrt(|d|)/2a i")
            P("   = (-{0})/(2*{1}) + sqrt(|{2}|)/(2*{1}) i".format(O(b,par=1,r=4),O(a,par=1,r=4),O(d,r=4)))
            P("   = {} + {} i".format(x,O(y,par=1)))
            P("z2 = -b/2a - sqrt(|d|)/2a i")
            P("   = (-{0})/(2*{1}) - sqrt(|{2}|)/(2*{1}) i".format(O(b,par=1,r=4),O(a,par=1,r=4),O(d,r=4)))
            P("   = {} - {} i".format(x,O(y,par=1)))
        elif d == 0:
            P("x1 = x2 = -b/2a")
            P("   = (-{})/(2*{})".format(O(b,par=1,r=5),O(a,par=1,r=5)))
            P(O(x,av="   = "))
            for i in range(3): P("")
        elif d > 0:
            if a > 0:
                P("x1 = (-b-sqrt(d))/(2a)")
                P("   = (-{}-sqrt({}))/(2*{})".format(O(b,par=1,r=4),O(d,r=4),O(a,par=1,r=4)))
                P(O(x-abs(y),av="   = "))
                P("x2 = (-b+sqrt(d))/(2a)")
                P("   = (-{}+sqrt({}))/(2*{})".format(O(b,par=1,r=4),O(d,r=4),O(a,par=1,r=4)))
                P(O(x+abs(y),av="   = "))
            else:
                P("x1 = (-b+sqrt(d))/(2a)")
                P("   = (-{}+sqrt({}))/(2*{})".format(O(b,par=1,r=4),O(d,r=4),O(a,par=1,r=4)))
                P(O(x+abs(y),av="   = "))
                P("x2 = (-b-sqrt(d))/(2a)")
                P("   = (-{}-sqrt({}))/(2*{})".format(O(b,par=1,r=4),O(d,r=4),O(a,par=1,r=4)))
                P(O(x-abs(y),av="   = "))
    elif i == 4:
        # Vincent
        P("-----------------------------")
        if d <= 0:
            P("  x |        -b/(2a)        |")
            P("-----------------------------")
            if a > 0:
                P("P(x)|     +     m     +     |")
            else:
                P("P(x)|     -     M     -     |")
        else:
            P("  x |    x1  -b/(2a)  x2    |")
            P("-----------------------------")
            if a > 0:
                P("P(x)|  +  0  -  m  -  0  +  |")
            else:
                P("P(x)|  -  0  +  M  +  0  -  |")
        P("-----------------------------")
        P("Extremum : ")
        P("   (", O(-b / (2 * a), r=4), ";", O(e, r=4), ")")
        P("")
        P("")
    elif i == 5:
        # Kevin
        if d == 0:
            P("P(x) = a(x-(-b/2a))^2")
            if x1 != 0:
                P(O(-x1, "P(x) = {}(x".format(a), ")^2", p=1))
            else:
                P("P(x) = {}x^2".format(a))
        elif d > 0:
            P("P(x) = a(x-x1)(x-x2)")
            P(O(-x2,O(-x1,"P(x) = {}(x".format(a),")(x",p=1,naf=2,r=4),")",p=1,naf=2,r=4))
        else:
            P("P(z) = a(z-z1)(z-z2)\nAvec:")
            P(O(-x,"(z-z1) = (z",O(y,ap="i",r=4,naf=1,p=1)+")",r=4,naf=2,p=1))
            P(O(-x,"(z-z2) = (z",O(-y,ap="i",r=4,naf=1,p=1)+")",r=4,naf=2,p=1))
    elif i == 6:
        pass
    if i != 6 and i != 1:
        input()


def O(v, av="", ap="", p=0, r=8, naf=0, br=0, par=0):
    # valeur, str avant, str apres, afficher signe, arrondi,
    # ne pas afficher un 0 (1, 2 et 3: resultats differents), sauter v ligne
    # parentheses autour de v
    if br != 0:
        for i in range(v):
            P("")
    elif br == 0:
        if v == 0 and naf == 1:
            return ""
        if v == 0 and naf == 2:
            return str(av) + str(ap)
        if v == 0 and naf == 3:
            return str(av)
        if v == int(v):
            v = int(v)
        else:
            v = round(v, r)
        if av == "" and ap == "" and p == 0 and par == 0:
            return v
        if p == 1 and v > 0:
            v = "+" + str(v)
        if par == 1 and v < 0:
            v = "({})".format(v)
    return str(av) + str(v) + str(ap)


def menu(warning=""):
    aff_entete()
    aff_menu()
    if warning != "":
        P(warning)
    choix = 0
    while choix == 0:
        try:
            choix = int(input())
        except:
            choix = 0
            menu(">> saisir un entier entre 1 et 6 !")
    exec_menu(choix)
    if choix != 6:
        menu()


O(9, br=1)
exec_menu(1)
menu()

# Supprimer 7 lignes ci dessous pour tester sur la numworks
s = 0
for name in dir():
    P("nom var = " + name)
    P(globals()[name])
    P(sys.getsizeoformat(globals()[name]))
    s = s + sys.getsizeoformat(globals()[name])
    P(s)