# https://nsi.xyz/
# Auteurs : Arthur Jacquin, Kevin Fedyna, Vincent Robert.

from math import sqrt

a, b, c = 0, 0, 0


def def_calc_trinome():
 global a, b, c, d, e, nb, x, y, x1, x2
 while a == 0:
  a = optimiser(float(input('a = ')))
 b = optimiser(float(input('b = ')))
 c = optimiser(float(input('c = ')))
 d = optimiser(float(b**2 - 4 * a * c))
 e = optimiser(float(a * (-b / (2 * a))**2 + b * (-b / (2 * a)) + c))
 if d == 0:
  nb = 1
 else:
  nb = 2
 x = optimiser((-b) / (2 * a))
 y = optimiser((sqrt(abs(d))) / (2 * a))
 x1 = optimiser(min(x + y, x - y))
 x2 = optimiser(max(x - y, x + y))


def aff_entete():
 optimiser(9, br=1)
 print("Polynome (equation) de degre 2")
 if a == 0:
  print("P(x)=ax^2+bx+c (=0)")
 else:
  print("P(x)={}{}{} (=0)".format(
   optimiser(a, ap="x^2", r=4),
   optimiser(b, p=1, ap="x", r=4, naf=1), optimiser(c, p=1, r=4, naf=1)))
  print("")


def aff_menu():
 print("1. Changer les valeurs a,b,c")
 if d < 0:
  s = "< 0"
 elif d > 0:
  s = "> 0"
 elif d == 0:
  s = ""
 print("2. Discriminant = {} {} ".format(d, s))
 if d < 0:
  print("3. Racines complexes conjuguees : 2 ")
  print("   z1= {} + {} i".format(x, y))
  print("   z2= {} - {} i".format(x, y))
 elif d > 0:
  print("3. Racines reelles distinctes : 2 ")
  print("   x1= {}".format(x1))
  print("   x2= {}".format(x2))
 elif d == 0:
  print("3. Racine reelle double : 1 ")
  print("   x1=x2= {}".format(x))
 if d < 0:
  if a < 0:
   print("4. Signe : -", end=" ")
  else:
   print("4. Signe : +", end=" ")
 elif d == 0:
  if a < 0:
   print("4. Signe : -0-", end=" ")
  else:
   print("4. Signe : +0+", end=" ")
 else:
  if a < 0:
   print("4. Signe : -+-", end=" ")
  else:
   print("4. Signe : +-+", end=" ")
 if a < 0:
  print(", extremum : M")
 else:
  print(", extremum : m")
 if d < 0:
  print("5. Factorisation dans les complexes")
 elif d >= 0:
  print("5. Factorisation dans les reels")
 print("6. Quitter")


def exec_menu(i):
 global a, b, c, d, x, y
 aff_entete()
 if i == 1:
  a, b, c = 0, 0, 0
  def_calc_trinome()
 if i == 6:
  quit()

def exec_menu_1():
 pass

def exec_menu_2():
 pass

def exec_menu_3():
 pass

def exec_menu_4():
 pass

def exec_menu_5():
 pass

def exec_menu_6():
 pass

def optimiser(v, av="", ap="", p=0, r=8, naf=0, br=0, par=0):
 # valeur, str avant, str apres, afficher signe, arrondi,
 # ne pas afficher un 0 (1, 2 et 3: resultats differents), sauter v ligne
 # parentheses autour de v
 if br != 0:
  for i in range(v):
   print("")
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
  print(warning)
 choix = 0
 while choix == 0:
  try:
   choix = int(input())
  except:
   choix = 0
   menu(">> saisir un entier entre 1 et 6 !")
 eval("aff_menu_{}()".format(choix))
 if choix != 6:
  menu()


optimiser(9, br=1)
exec_menu(1)
menu()
