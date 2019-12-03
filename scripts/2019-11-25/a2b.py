# Skript vertauscht die Variablen a und b nur mit arithmethischen Ausdrücken

# Also sowas nur mit + -:
"""
x = 3
y = 2
print("x ist: ",x, "y ist :",y)
z = x
x = y
y = z
print("x ist: ",x, "y ist :",y)
"""

a = int(input("Bitte Wert für a eingeben: "))
b = int(input("Bitte Wert für b eingeben: "))

a = a + b
b = -b + a
a = a - b

print("a ist:", a)
print("b ist:", b)