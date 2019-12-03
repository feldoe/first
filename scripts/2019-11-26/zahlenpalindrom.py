# https://de.wikipedia.org/wiki/Zahlenpalindrom

# Ist x ein Zahlenpalindrom?
# 0. Zahl einlesen
# 1. Die Zahl umdrehen
# 1a. Ganzzahlige Division durch 10 (löscht letzte Stelle)
# 1b. Letze Zahl holen x % 10
# 1c. Ziffern anhängen
# 2. Ist die Zahl umgedreht == Zahl?

x = int(input("Bitte geben Sie eine Zahl ein: "))

kopie = x   # damit der ursprüngliche Wert nicht überschrieben wird
umgekehrt = 0

# Wiederhole solange kopie Ziffern hat
while kopie > 0:
    umgekehrt = umgekehrt * 10 + kopie % 10
    kopie = kopie // 10
    
if x == umgekehrt:
    print("Die Zahl",x, "ist eine Palindromzahl")
else:
    print("Die Zahl", x, "ist keine Palindromzahl")