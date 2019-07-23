# Initialisation et saisie
print("Polynôme (équation) de degré 2")
print("P(x) = ax^(2)+bx+c")
print("")
print(" > Saisie des valeurs")
print("")
print("a =")
try: a = float(input())
except: print("Saisie non valide")
while a == 0:
    print("a doit être différent de 0 !")
    a = float(input())
if a == int(a): a = int(a)
if a >= 0: Va = str(a)
else: Va = "({})".format
a = float(a)
print("b =")
b = float(input())
if b == int(b): b = int(b)
if b >= 0: Vb = str(b)
else: Vb = "({})".format(b)
b = float(b)
print("c =")
c = float(input())
if c == int(c): c = int(c)
if c >= 0: Vc = str(c)
else: Vc = "({})".format(c)
c = float(c)

# Calculs
d = b*b-(4*a*c)
if d == int(d): d = int(d)
if d >= 0: Vd = str(d)
else: Vd = "({})".format(d)
d = float(d)
if d > 0:
    x1 = min((-b-d**(0.5))/(2*a),(-b+d**(0.5))/(2*a))
    if x1 == int(x1): x1 = int(x1)
    if x1 >= 0: Vx1 = str(x1)
    else: Vx1 = "({})".format(x1)
    x1 = float(x1)
    x2 = max((-b-d**(0.5))/(2*a),(-b+d**(0.5))/(2*a))
    if x2 == int(x2): x2 = int(x2)
    if x2 >= 0: Vx2 = str(x2)
    else: Vx2 = "({})".format(x2)
    x2 = float(x2)
elif d == 0:
    x0 = -b/(2*a)
    if x0 == int(x0): x0 = int(x0)
    if x0 >= 0: Vx0 = str(x0)
    else: Vx0 = "({})".format(x0)
    x0 = float(x0)
A = (-b)/(2*a)
if A == int(A): A = int(A)
if A >= 0: VA = str(A)
else: VA = "({})".format(A)
A = float(A)
B = c-((b*b)/(4*a))
if B == int(B): B = int(B)
if B >= 0: VB = str(B)
else: VB = "({})".format(B)
B = float(B)

# Tableau
tableau = ["","","","","","","","","","",""]
if d < 0: ligne35 = [" "," "," "]
e = "0"
if d == 0: ligne35 = [" ","|"," "]
else: e = "B"
xx = ["x1","x2"]
if d > 0: ligne35 = ["|"," ","|"]
else: xx = ["  ","  "]
if a > 0: signedea = ["+","-","\>","/>","|",e]
else: signedea = ["-","+","/>","\>",e,"|"]
tableau[0] = "--|-------------------------|"
tableau[1] = "x |-8    {}    A    {}    +8|".format(xx[0],xx[1])
tableau[2] = tableau[0]
tableau[3] = "{} |       {}    {}    {}       |".format("+",ligne35[0],ligne35[1],ligne35[2])
if d > 0: tableau[4] = "0 |   {0}   0    {1}    0   {0}   |".format(signedea[0],signedea[1])
elif d == 0: tableau[4] = "0 |     {0}      0      {0}     |".format(signedea[0])
else: tableau[4] = "0 |            {}            |".format(signedea[0])
tableau[5] = "{} |       {}    {}    {}       |".format("-",ligne35[0],ligne35[1],ligne35[2])
tableau[6] = tableau[0]
tableau[7] = "/ |            {}            |".format(signedea[4])
tableau[8] = "- |     {}     |     {}     |".format(signedea[2],signedea[3])
tableau[9] = "\ |            {}            |".format(signedea[5])
tableau[10] = tableau[0]

# Affichage des résultats
if d > 0:
    print("P(x) = ax^(2)+bx+c")
    print("     = a(x-A)^(2)+B")
    print("     = a(x-x1)(x-x2)")
    print("Δ = b^(2)-4ac = {}".format(Vd))
    print("x1 = (-b{}sqrt(Δ))/2a = {}".format(signedea[1],Vx1))
    print("x2 = (-b{}sqrt(Δ))/2a = {}".format(signedea[0],Vx2))
    print("A = -b/2a = {}".format(VA))
    print("B = c-(b^(2))/4a = {}".format(VB))
    print("a = {}".format(Va))
    print("b = -2aA = {}".format(Vb))
    print("c = A^(2)+B = {}".format(Vc))
elif d == 0:
    print("P(x) = ax^(2)+bx+c")
    print("     = a(x-A)^(2)")
    print("     = a(x-x0)^(2)")
    print("Δ = b^(2)-4ac = {}".format(Vd))
    print("x0 = -b/2a = {}".format(Vx0))
    print("")
    print("A = -b/2a = {}".format(VA))
    print("")
    print("a = {}".format(Va))
    print("b = -2aA = {}".format(Vb))
    print("c = A^(2) = {}".format(Vc))
else:
    print("P(x) = ax^(2)+bx+c")
    print("     = a(x-A)^(2)+B")
    print("")
    print("Δ = b^(2)-4ac = {}".format(Vd))
    print("Racines non réelles")
    print("")
    print("A = -b/2a = {}".format(VA))
    print("B = c-(b^(2))/4a = {}".format(VB))
    print("a = {}".format(Va))
    print("b = -2aA = {}".format(Vb))
    print("c = A^(2)+B = {}".format(Vc))
input()
for i in range(len(tableau)):
    print(tableau[i])
input()
for i in range(12):
    print("")