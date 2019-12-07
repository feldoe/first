# Palindrome sind vorwärts wie rückwärts gelesen gleich
s = input("Bitte geben Sie eine Zeichenkette ein: ")

s = s.lower()   # Groß und Kleinschreibung ignorieren, man kann streiten ob noch Palindrom

if s[::-1] == s:
    print(s, "ist ein Palindrom")
else:
    print(s, "ist kein Palindrom")

