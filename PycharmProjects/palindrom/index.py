s = input("Eingabe: ")

"""
for i in range (len(s)):
    print(s[i])
"""

# Man kann einfach über den String iterieren
"""
for c in s:
    print(c)
"""

# Ist ein c oder i enthalten
gefunden = 0
# gefunden = False      # Alternative
for c in s:
    if c == 'i' or c == 'u':
        gefunden += 1
        # gefunden = True
        break

if gefunden > 0:
# if gefunden:      # if Wahr
    print("Es gibt ein i oder ein u")
else:
    print("Es gibt kein i oder kein u")
