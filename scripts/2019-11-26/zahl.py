# 1. Zahl einlesen
# 2. "Gerade" ausgeben wenn die Zahl gerade ist
# 3. "Ungerade" sonst

s = int(input("Bitte geben Sie eine Zahl ein: "))
# print(s)

if s % 2 == 0:
    print("Gerade")
else:
    print("Ungerade")