#Initialisation

nb_lignes_console = 12
Va = "a"
Vb = "b"
Vc = "c"
options_menu = ("Redéfinir les variables","Discriminant","Racines","Fluctuations et extremum","Signes","Formes de l'équation")

# Fonction Principale

def menu(erreur):
    if erreur == 1:
        print("Il faut choisir une option !")   
        print("Tapez le chiffre correspondant :")
        print("")
        nb_lignes_entete = 3
    else:
        entete()
        nb_lignes_entete = 3 #//
    for i in range(len(options_menu)): print(" ",i+1,"-",options_menu[i])
    for i in range((nb_lignes_console)-(nb_lignes_entete)-len(options_menu)-1): print("")
    try: choix = int(input())
    except: menu(1)
    if choix >= 1 and choix <= len(options_menu):
        for i in range(12):
            print("")
        if choix == 1:
            trinome_saisie()
        elif choix == 2:
            trinome_discriminant()
        elif choix == 3:
            trinome_racines()
        elif choix == 4:
            trinome_fluctuations_et_extremum()
        elif choix == 5:
            trinome_signes()
        elif choix == 6:
            trinome_formes_de_l_equation()
    else:
        menu(1)

# Fonctions utilitaires

def entete():
    print("Polynôme (équation) de degré 2")
    print("P(x) =",trinome_formule(Va,Vb,Vc))
    print("")

def trinome_formule(a,b,c):
    return "{}x^(2)+{}x+{}".format(a,b,c)

# Fonctions du menu

def trinome_saisie():
    entete()
    global a,b,c,Va,Vb,Vc
    print("Saisie des valeurs :")
    print("a =")
    a = float(input())
    while a == 0:
        print("a doit être différent de 0 !")
        a = float(input())
    if a == int(a): a = int(a)
    if a > 0: Va = str(a)
    else: Va = "({})".format(a)
    print("b =")
    b = float(input())
    if b == int(b): b = int(b)
    if b > 0: Vb = str(b)
    else: Vb = "({})".format(b)
    print("c =")
    c = float(input())
    if c == int(c): c = int(c)
    if c > 0: Vc = str(c)
    else: Vc = "({})".format(c)
    menu(0)

def trinome_discriminant():
    global d,Vd,signea0
    d = b*b-(4*a*c)
    if d > 0: Vd = str(d)
    else: Vd = "({})".format(d)
    if d < 0: signea0 = ["<","inférieur"]
    elif d == 0: signea0 = ["=","égal"]
    else: signea0 = [">","supérieur"]
    entete()
    print("Discriminant")
    print("")
    print("Δ = b^2-4ac =")
    print("  = {b}^2-4.{a}.{c} = {d}".format(a=Va,b=Vb,c=Vc,d=Vd))
    print("Δ",signea0[0],"0")
    print("")
    print("Le discriminant est {}.".format(d))
    print("Il est donc {} à zéro.".format(signea0[1]))
    input()
    menu(0)

#def trinome_racines():
#def trinome_fluctuations_et_extremum():
#def trinome_signes():
#def trinome_formes_de_l_equation():

# Début programme
trinome_saisie()
menu(0)