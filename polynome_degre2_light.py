# computing. ready august 2019
# https://nsi.xyz/ 
# https://workshop.numworks.com/python/cent20/polynome_degre2
# Auteurs : Arthur Jacquin, Kevin Fedyna, Vincent Robert.

from math import sqrt
import sys 

a,b,c=0,0,0

def def_calc_trinome():
    global a,b,c,d,nb,x,y
    while a==0 : a=optimiser(float(input('a = ')))
    b=optimiser(float(input('b = ')))
    c=optimiser(float(input('c = ')))
    d=optimiser(float(b**2-4*a*c)) 
    if d==0: nb=1
    else: nb=2
    x=optimiser((-b)/(2*a))
    y=optimiser((sqrt(abs(d)))/(2*a))
    
def aff_entete():
		optimiser(9,br=1)
		print("Polynome (equation) de degre 2")
		if a==0 : print("P(x)=ax^2+bx+c (=0)")
		else :
			print("P(x)={}{}{} (=0)".format(optimiser(a,ap="x^2",r=4),optimiser(b,p=1,ap="x",r=4,af=1),optimiser(c,p=1,r=4,af=1)))
			print("") 

def aff_menu():
    # Choix 1
    print("1. Changer les valeurs a,b,c")
    # Choix 2
    if d<0: s = "< 0"
    elif d>0: s = "> 0"
    elif d==0: s = ""
    print("2. Discriminant = {} {} ".format(d,s))
    # Choix 3
    if d<0:
        print("3. Racines complexes conjuguees : 2 ")
        print("   z1= {} + {} i".format(x,y))
        print("   z2= {} - {} i".format(x,y))
        # Spoil Tale S
    elif d>0:
        x1=optimiser(min(x+y,x-y))
        x2=optimiser(max(x-y,x+y))
        print("3. Racines reelles distinctes : 2 ")
        print("   x1= {}".format(x1))
        print("   x2= {}".format(x2))
    elif d==0:
        print("3. Racine reelle double : 1 ")
        print("   x1=x2= {}".format(x))
    # Choix 4
    if d<0:
        if a<0 : print("4. Signe : -",end =" ")
        else : print("4. Signe : +",end =" ")
    elif d==0:
        if a<0 : print("4. Signe : - 0 -",end =" ")
        else : print("4. Signe : + 0 +",end =" ")
    else:
        if a<0 : print("4. Signe : - + -",end =" ")
        else : print("4. Signe : + - +",end =" ")
    if a<0 : print(", extremum : M")
    else : print(", extremum : m")
    # Choix 5
    if d<0 : print("5. Factorisation dans les complexes")
    elif d>=0 : print("5. Factorisation dans les reels")
    # Choix 6
    print("6. Quitter") 

def exec_menu(i):
	if i==1 :
		global a,b,c
		a,b,c=0,0,0
		aff_entete()
		def_calc_trinome()
	elif i==2 :
		pass #kevin
	elif i==3 :
		pass #kevin
	elif i==4 :
		pass #kevin
	elif i==5 :
		pass #kevin
	elif i==6 :
		pass
		
def optimiser(v,av="",ap="",p=0,r=8,naf=0,br=0):
		# valeur, str avant, str apres, afficher signe, arrondi, ne pas afficher un 0, sauter v ligne
		if br!=0 :
			for i in range(v): print("")
		elif br==0 :
			if v==0 and naf==1 : return ""
			if v == int(v): v = int(v)
			else : v=round(v,r)
			if av=="" and ap=="" and p==0 : return v
			if p==1 and v>0 : v="+"+str(v)
			return str(av)+str(v)+str(ap)


def menu(warning=""):
		aff_entete()
		aff_menu()
		print(warning)
		choix=0
		while choix==0 :
			try:
				choix=int(input())
			except:
				choix=0
				menu(">> saisir un entier entre 1 et 6 !") 
		exec_menu(choix)
		if choix !=6 : menu()

optimiser(9,br=1)
exec_menu(1)
menu()

s=0 # Supprimer 7 lignes pour tester sur la numworks
for name in dir():
    print("nom var = "+name)
    print(globals()[name])
    print(sys.getsizeof(globals()[name]))
    s=s+sys.getsizeof(globals()[name]) 
    print(s)
