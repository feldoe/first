""""
warm = ['rot', 'gelb', 'schwarz']

#heiss = warm
heiss = warm.copy()

heiss.append('pink')

print(warm)
print(heiss)
"""

"""
# Listen von Listen, z.B. für Matrizen, mehr dimensionale Arrays
l1 = [[1,2], [3,4], "b"]

print(l1[0][1]) # Zeilennummer und Spaltennummer, deshalb wird 2 ausgegeben
"""
"""
# Zwei Listen vergleichen und Duplikate entfernen
# Noch fehlerhaft, da Liste überschrieben wird
L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]

def remove_dups(L1, L2):
    for e in L1:
        if e in L2:
            L1.remove(e)
            
remove_dups(L1, L2)
print(L1)
"""

# Zwei Listen vergleichen und Duplikate entfernen
a = [1, 2, 3, 4]
b = [1, 2, 5, 6]

def remove_dups(L1, L2):
    L1_copy = L1[ : ]
    for e in L1:
        if e in L2:
            L1.remove(e)


remove_dups(a, b)
print(a)