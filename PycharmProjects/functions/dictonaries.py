# Key : Value
# Schlüssel : Wert
# Paare werden durch Kommas getrennt
# Schlüssel müssen einzigartig sein
# Schlüssel müssen unveränderlich sein

# noten = {"Kiril" : 2.0, "Anja" : 1.0, "Hannes" : 1.7}
"""
noten["Sven"] = 1.3     # Element hinzufügen

print(noten["Kiril"])   # Wert auslesen durch Angabe des Schlüssels
print(noten)
print(noten)    # Dictionaries haben keine Reihenfolge
print("Kiril" in noten)     # Boolabfrage ob Element in Wörterbuch vorhanden
print("kiril" in noten)

del(noten["Kiril"])
print("Kiril" in noten)

print(noten.keys())
print(noten.values())

# Name ist der Schlüssel, gehe über alle Schlüssel und gebe Namen mit Note 1.0 aus
for name in noten.keys():
    if noten[name] == 1.0:
        print(name)

# Vergleich zum Tupel
l = [("Kiril", 1), ("Anja", 2), ("Anatoli", 3)]

for (a,b) in l:
    print(a,b)
"""
# a = key
# b = value
"""
for (a,b) in noten.items():
    print(a,b)

l = [1,2,3,4,5]
"""
 # noten = {"Kiril" : 2.0, "Anja" : 1.0, "Hannes" : 1.7}

# Selbstgeschriebene Summe
"""
my_sum = 0
for i in l:
    my_sum += i
"""

# print(sum(l))
"""
mean = sum(noten.values()) / len(noten.values())
print(mean)
"""

# Dictionaries können dictionaries enthalten


ausgabe = {"en" : {"welcome" : "welcome",
                   "file" : "file",
                   "goodbye" : "goodbye",

                   },"de" : {"welcome" : "Willkommen",
                   "file" : "Datei",
                   "goodbye" : "Auf Wiedersehen"}}

sprache = "en"
sprache2 = "de"
# Angabe der Sprache (Schlüseel Ebene 1) und des Schlüssels Ebene 2: Ausgabe des korrekten Wortes
print(ausgabe[sprache]["welcome"])
print(ausgabe[sprache2]["welcome"])
"""
zk = "test Kiril test hallo welt"
woerter = zk.split()
zaehler = {}

for wort in woerter:
    if wort in zaehler:
        zaehler[wort] += 1
    else:
        zaehler[wort] = 1

print(zaehler)
"""

"""
square_of_evens = []

# In drei Zeilen
for i in range(10):
    if i % 2 == 0:
        square_of_evens.append(i*i)

print(square_of_evens)
# In einer Zeile
square_of_evens = [i*i for i in range(10) if i%2 == 0]

print(square_of_evens)
"""
"""
noten = {"Kiril" : 2.0, "Anja" : 1.0, "Hannes" : 1.7}

# Schlüssel von Noten mit besser als 1.7
gute_note = [name for name in noten.keys() if noten[name] < 1.7]
print(gute_note)
"""

# Dictionary comprehension
"""
fruits = ["apple", "mango", "banana", "cherry"]
d = {}

for f in fruits:
    print("Fuege fuer den Schluessel", f, "den Wert", len(f), "ein")
    d[f] = len(f)

print(d)
#Einfacher mit Dictionary comprehension, in einer Zeile
d = {f: len(f) for f in fruits}
print(d)
"""
# d["apple"] = 5
"""
laenge = {f : len(f) for f in fruits}
print(laenge)

# Ähnlich bloß mit Schleife
for f in fruits:
    print(len(f))

# Auf einer Zeile
s = " ".join(fruits)
print(s)
"""

"""
noten_gruppe1 = {"Kiril" : 2.0, "Anja" : 1.0, "Hannes" : 1.7}
noten_gruppe2 = {"Kiril" : 2.0, "Anja" : 1.0, "Hannes" : 1.7}

noten = noten_gruppe1.copy()
noten.update(noten_gruppe2)

print(noten_gruppe1)
"""

"""
l1 = ["apple", "mango", "banana", "cherry"]

l2 = [item for item in l1 if len(item) < 6]
print(l2)
l3 = {f : len(f) for f in l1 if len(f) < 6}     # Geschweifte Klammern wie mathematische Menge
print(l3)

# Als Schleife
l4 = []
for e in l1:
    if len(e) < 6:
        l4.append(e)

print(l4)
"""
# Mengen, veränderlich aber ohne Index und ungeordnet
menge = {1, 2, 3}

leere_Menge = set()     # leeres_dictionary = {}

erste_menge = {1, 2, 3, 4}
zweite_menge = {3, 4, 5}

zweite_menge.add(8)
schnitt_menge = erste_menge & zweite_menge
verneinigung = erste_menge | zweite_menge

print(erste_menge)
print(zweite_menge)
print(schnitt_menge)
print(verneinigung)