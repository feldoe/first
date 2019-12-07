# Hello World um die pyCharm IDE kennen zu lernen
# print("Hello World")
"""
for i in range(10):
    print(i)
"""

"""
mysum = 0

for i in range(5,11,2):
    mysum += i # mysum = mysum + 1
    print(i)

print("=====")
print(mysum)
"""

# 1.Eine Zahl n einlesen
# 2. *
#   **
#   ***
#   *** mit n = 3

# n = int(input("Bitte eine Zahl eingeben: "))
"""
for i in range (n+1):
    zeile = "*" * i
    print(zeile)
"""
"""
for i in range (n+1):
    leer = n - i
    leer = " " * leer
    zeile = "*" * i
    zeile = leer + zeile
    print(zeile)
"""
# in kurz
"""
for i n range (1, n + 1):
    print(" "*(n-i) + "*" * i)
"""

"""
for i in range (n, 0, -1):
    zeile = "*" * i
    print(zeile)
"""
"""
mysum = 0

for i in range(5,11,2):
    mysum += 5

    if mysum == 5:
        break   # Alles nach break wird ignoriert, wenn if-Statement erfüllt ist
        # mysum += 1

print(mysum)
"""
"""
s = input("Bitte geben Sie eine Zeichenkette ein: ")

print(len(s))
"""
"""
s = "abc"

print(s[-3])    # Mit negativem Vorzeichen kann man rückwärts zählen
"""

# Scheiben von strings, mit string[start:stop:step]
# [::] Nur Standard Werte, alles wird ausgegeben
"""
s = "abcdefgh"
#    01234567   Indizes
print(s[3:6])   # Ausgabe def
print(s[:6])    # Standard Wert start = 0
print(s[:])     # Standard Wert stop = End of String, bzw länge des Strings
print(s[3:6:2]) # Ausgabe df
print(s[::-1])  # Ausgabe Zeichenkette in umgekehrter Reihenfolge
print(s[-1:-len(s)-1:-1])   # Standard Werte für -1 bei step
"""

# Strings sind unveränderlich, es wird ein neues String Objekt erstellt
s = "hello"
print(id(s))
s = 'y' + s[1:]
print(s)
print(id(s))