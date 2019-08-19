# https://nsi.xyz/
# Auteurs : Arthur Jacquin, Kevin Fedyna, Vincent Robert.

from math import sqrt

a, b, c = 0, 0, 0
P = print
I = input


def def_calc_trinome():
 global a, b, c, d, e, nb, x, y, x1, x2
 while a == 0:
  a = Op(float(I('a = ')))
 b = Op(float(I('b = ')))
 c = Op(float(I('c = ')))
 d = Op(float(b**2 - 4 * a * c))
 e = Op(float(a * (-b / (2 * a))**2 + b * (-b / (2 * a)) + c))
 if d == 0:
  nb = 1
 else:
  nb = 2
 x = Op((-b) / (2 * a))
 y = Op((sqrt(abs(d))) / (2 * a))
 x1 = Op(min(x + y, x - y))
 x2 = Op(max(x - y, x + y))


def aff_entete():
 Op(9, br=1)
 P("Polynome (equation) de degre 2")
 if a == 0:
  P("P(x)=ax^2+bx+c (=0)")
 else:
  P("P(x)={}{}{} (=0)".format(
   Op(a, ap="x^2", r=4),
   Op(b, p=1, ap="x", r=4, naf=1), Op(c, p=1, r=4, naf=1)))
  P("")


def aff_menu():
 P("1. Changer les valeurs a,b,c")
 if d < 0:
  s = "< 0"
 elif d > 0:
  s = "> 0"
 elif d == 0:
  s = ""
 P("2. Discriminant = {} {} ".format(d, s))
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
 if d < 0:
  P("5. Factorisation dans les complexes")
 elif d >= 0:
  P("5. Factorisation dans les reels")
 P("6. Quitter")


def exec_menu(i):
 global a, b, c, d, x, y
 aff_entete()
 if i == 1:
  a, b, c = 0, 0, 0
  def_calc_trinome()
 if i == 6:
  quit()

def exec_menu_1():
 global a, b, c, d, x, y
 a, b, c = 0, 0, 0
 def_calc_trinome()

def exec_menu_2():
 P("2. Calcul du discriminant :")
 P("")
 P("d = b^2 + 4*a*c")
 P(f" = {Op(b,par=1)}^2 + 4*{Op(a,par=1)}*{Op(c,par=1)}")
 if b == 0 and c != 0:
  P(Op(4*a*c,av=" = "))
 else:
  P(f" = {Op(b**2)}{Op(4*a*c,p=1,naf=1)}")
  if c != 0:
   P(Op(d,av=" = "))
 P("")
 P(Op(d,av="d = "), end=" ")
 if d == 0:
  P("")
 elif d < 0:
  P("< 0")
 elif d > 0:
  P("> 0")
 if b != 0 and c != 0:
  P("")
  I()

def exec_menu_3():
 P("3. Calcul des racines :")
 P("")
 if d < 0:
  P("d < 0 d Opnc il existe")
  P("2 racines c Opmplexes c Opnjugees")
  P("telles que :")
  P("")
  P("z1 = -b/2a + sqrt(|d|)/2a i")
  P("z2 = -b/2a - sqrt(|d|)/2a i")
 elif d == 0:
  P("d = 0 d Opnc il existe")
  P("1 racine reelle d Opuble")
  P("telle que :")
  P("")
  P("x1 = x2 = -b/2a")
  P("")
 elif d > 0:
  P("d > 0 d Opnc il existe")
  P("2 racines reelles distinctes")
  P("telles que :")
  P("")
  if a > 0:
   P("x1 = (-b-sqrt(d))/(2a)")
   P("x2 = (-b+sqrt(d))/(2a)")
  else:
   P("x1 = (-b+sqrt(d))/(2a)")
   P("x2 = (-b-sqrt(d))/(2a)")
 I()
 aff_entete()
 P("3. Calcul des racines :")
 P("")
 if d < 0:
  P("z1 = -b/2a + sqrt(|d|)/2a i")
  P(f"  = (-{ Op(b,par=1,r=4)})/(2*{ Op(a,par=1,r=4)}) + sqrt(|{ Op(d,r=4)}|)/(2*{ Op(a,par=1,r=4)}) i")
  P(f"  = {x} + { Op(y,par=1)} i")
  P("z2 = -b/2a - sqrt(|d|)/2a i")
  P(f"  = (-{ Op(b,par=1,r=4)})/(2*{ Op(a,par=1,r=4)}) - sqrt(|{ Op(d,r=4)}|)/(2*{ Op(a,par=1,r=4)}) i")
  P(f"  = {x} - { Op(y,par=1)} i")
 elif d == 0:
  P("x1 = x2 = -b/2a")
  P(f"  = (-{ Op(b,par=1,r=5)})/(2*{ Op(a,par=1,r=5)})")
  P( Op(x,av="  = "))
  for i in range(3): P("")
 elif d > 0:
  if a > 0:
   P("x1 = (-b-sqrt(d))/(2a)")
   P(f"  = (-{ Op(b,par=1,r=4)}-sqrt({ Op(d,r=4)}))/(2*{ Op(a,par=1,r=4)})")
   P( Op(x-abs(y),av="  = "))
   P("x2 = (-b+sqrt(d))/(2a)")
   P(f"  = (-{ Op(b,par=1,r=4)}+sqrt({ Op(d,r=4)}))/(2*{ Op(a,par=1,r=4)})")
   P( Op(x+abs(y),av="  = "))
  else:
   P("x1 = (-b+sqrt(d))/(2a)")
   P(f"  = (-{ Op(b,par=1,r=4)}+sqrt({ Op(d,r=4)}))/(2*{ Op(a,par=1,r=4)})")
   P( Op(x+abs(y),av="  = "))
   P("x2 = (-b-sqrt(d))/(2a)")
   P(f"  = (-{ Op(b,par=1,r=4)}-sqrt({ Op(d,r=4)}))/(2*{ Op(a,par=1,r=4)})")
   P( Op(x-abs(y),av="  = "))
 I()

def exec_menu_4():
 pass

def exec_menu_5():
 pass

def exec_menu_6():
 exit()

def Op(v, av="", ap="", p=0, r=8, naf=0, br=0, par=0):
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
   choix = int(I())
  except:
   choix = 0
   menu(">> saisir un entier entre 1 et 6 !")
  aff_entete()
  eval("exec_menu_{}()".format(int(choix)))
 if choix != 6:
  menu()


Op(9, br=1)
aff_entete()
exec_menu_1()
menu()
