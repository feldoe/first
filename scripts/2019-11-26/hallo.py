"""
while(True):
	print("Hallo Welt")
"""
"""
print("Hallo Welt")	
s = input("Bitte geben Sie etwas ein: ")
print("Sie haben folgendes eingegeben "+s)
"""
"""
Vergleiche von Gleitkommazahlen durch Genauigkeit beschränkt
>>> a = 0.3
>>> b = 0.1
>>> c = 0.2
>>> d = b + c
>>> a == d
False
>>> d
0.30000000000000004

"""
# Überlegungen zu Wahrheitswerten
# not (A or B) == not A and not B
# not ( A and B) == not A or not B

# Bedingte Anweisungen: if-Statement

x = input("Bitte geben Sie ein Passwort ein: ")

if x == "Swordfish":
    print("Welcome")
else:
    print("Flasches Passwort")