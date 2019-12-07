"""
# Tupel
t = (2, "FU", 3)
u = (2, "FU", 3) + (4,5)

# Index eines Tupels
print(t[0])
print(t[1])
print(t[2])
print(u)
print(t)
print(t+u)
print(len(u))   # Länge eines Tupels
"""
# t[0] = 5, geht nicht da Tupel unveränderlich sind

"""
s = (1)
print(s)
print(type(s))  # s ist kein ein-elementiges Tupel sondern ein Integer
s1 = (1,)
print(s1)
print("s1 is vom Typ: ", type(s1))      # Jetzt ist es ein ein-elementiges Tupel
"""

# print(t[1:2])   # start 1, stop bei Index 2, exklusive Wert von Index 2

# schlecht, da eine Variable überschrieben wird
x = 5
y = 7
# x = y
# y = x
"""
#besser
print("x ist:", x)
print("y ist:", y)
(x, y) = (y, x)
print("x ist:", x)
print("y ist:", y)
"""
# Rückgabe als Tupel
"""
def quotient_und_rest(x, y):
    q = x // y
    r = x % y
    return (q,r)

(quotient, rest) = quotient_und_rest(17, 11)

print ("Quotient", quotient)
print("Rest", rest)
"""
"""
t = ("Kiril", "Jan", "Hannes", "Jorg")

for i in t:
    print(i)
"""
"""
# Unterschiede zwischen Listen und Tupel
# Listen sind veränderlich
eine_liste = []
L = [2, "a", 4]

print(len(eine_liste))
print(L[0])
L[1] = 5
print(L)

# Elemente an Listen hinzufügen mit: Listenname.append(Element)
L = [1,2,3]
print("Die Liste L enthält die Elemente:",L)
L.append(5)
print("Die Liste L enthält die Elemente:",L)

L1 = [2,1,3]
L2 = [4,5,6]
# L3 = L1.append(L2) , gibt L3 ist None, geht also so nicht
L3 = L1 + L2    # Neues Objekt L3 wird erzeugt, kann man mit id testen
print(L3, id(L3))
print(L1)
L1.extend([0,6])    # Extend erweitert Liste
print(L1)
L1.append(L2)   # Das Letzte das eingefügt wird ist eine Liste
print(L1)
L1.extend(L2)
print(L1)
"""

"""
L1 = [2,1,3]
L2 = [4,5,6]

print(L1)
del(L1[1])
print(L1)
x = L1.pop(1)   # pop() hat return Wert, default Wert 0
print(L1)
print(x)    # Gibt den gepoppten Wert aus
x = L1.pop(0)
print(L1)
"""

"""
s = "Hallo Welt"
l = list(s)     # Teil String in einzelne Chars auf

print(s, len(s))
print(l, len(l))

x = "blau rot gruen"

res = x.split()     # Schneiden bei Standard Trennzeichen -> Leerzeichen wie .split(" ")
print(res)

y = "blau,rot,gruen"
res2 = y.split(',')
print(res)
"""

# Zusammenfassen von Strings mit selbst festgelegten Zeichen
"""
L = ['a', 'b', 'c']

res1 = "".join(L)
print(res1)

res3 = "_".join(L)
print(res3)
"""

# Listen sortieren
""" 
L = [9,6,0,3]
L4 = sorted(L)   # sorted() verändert Liste nicht, deswegen neue Liste
print(L4)
print(L)
L.sort()    # ändert Liste, eine Klassenmethode
# L1 = L.sort() , hat keinen Rückgabewert deswegen None
print(L)
"""

# Liste umdrehen
L = [1,7,8,2]
L.sort(reverse=True)
print(L)