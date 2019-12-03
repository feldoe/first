# Test der while-Schleife
"""
n = 0

while (n < 5):
    print(n)
    n = n + 1
    """

"""
Ausgabe:
0
1
2
3
4
"""

# Beliebige Zahlenreihenfolge wird aufsteigend ausgegeben
n = int(input("Bitte geben Sie eine Zahl ein: "))
i = 0

"""
while (i <= n):
    print(i)
    i = i + 
"""

# Geben Sie alle ungeraden Zahlen kleiner als n aus
while (i < n):
    if (i % 2 != 0):
        print(i)
    i = i + 1   # i + 2, verändern der Schrittgröße kann uns das if-Statement sparen