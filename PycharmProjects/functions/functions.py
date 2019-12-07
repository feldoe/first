import math
# Funktionen kennenernen

"""

def f():
    print("Hallo Welt")

f()
"""

"""
def begruessen(name):
    print("Hallo " + name + ". Wie geht es dir?")

begruessen("Kiril")
begruessen("Anja")
"""

"""
def quadrat(x):
    a = 0.5
    b = 1.2
    c = 3.0

    ergebnis = a*x**2 + b*x + c
    return ergebnis

y1 = quadrat(1.0)
y2 = quadrat(5.0)
y3 = quadrat(1.2)

print(y1, ",", y2, ",", y3)

print(quadrat(2))
"""

"""
# Testet ob Zahl gerade ist
def is_even(i):
    print("innerhalb der Funktion") # Wir wissen das Funktion aufgerufen wurde
    return i % 2 == 0

y = is_even(5)
x = is_even(6)
print(y)
print(x)
"""

"""
# Unterschied zwischen lokalen und globalen Variablen
def f(x):
    x += 1
    z = 10
    print("in f. x=", x)
    print("in f. z=", z)
    return x


x = 3
z = f(x)
print("Global. x=", x)
print("Global. z=", z)
"""

""""""
# Etwas kompliziertere Funktionen
def factorial_rek(x):
    if x == 0:
        return 1
    elif x == 1:
        return 1
    else:
        return x * factorial_rek(x-1)

print(factorial_rek(0))
print(factorial_rek(1))
print(factorial_rek(3))
print(factorial_rek(5))


def factorial(n):
    ergebnis = 1
    for i in range(1,n+1):
        ergebnis *= i
    return ergebnis

"""
print(factorial(5))
print(factorial(0))
"""

# Beim aufmultiplizieren mit 1 beginnen
# Berechne e hoch x
def exp(x):
    ergebnis = 1

    for i in range(6):
        ergebnis += x**i / factorial(i)
    return ergebnis

#print(exp(2))

def cos(x):
    ergebnis = 0
    for n in range(6):
        ergebnis += (((-1) ** n) * x**(2*n)) / factorial(2*n)
    return ergebnis

"""
print(cos(3.1415926535897932384626433832795))  # math.pi
print(cos(1))
print(cos(0))
print(3.14 / 2)
"""