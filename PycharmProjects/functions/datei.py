import math
# math.funktionsname()
# Dateien einlesen
"""
f = open("test.txt")    # Datei öffnen
s = f.read()        # Datei einlesen
print(s)        # Datei ausgeben
f.close()       # Datei schliessen
"""
# besser
"""
with open("test2.txt") as f:       # 'w' schreibt Datei, erzeugt sie
    s = f.read()
    print(s)


with open("test3.txt", 'w') as file:      # 'w' schreibt Datei, erzeugt sie
    file.write("Hallo Welt")
"""

n = 17.11
x = math.sqrt(n)        # Wurzel
y = math.ceil(n)        # aufrunden
z = math.floor(n)       # abrunden


print(x, y, z)
print(j)