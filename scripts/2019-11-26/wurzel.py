x = float(input("Bitte geben Sie eine Zahl ein: ")) #  float einlesen

g = 3 #  Haben wir so festgelegt

while (abs((g * g)-x) > 0.01):
    g = (g + (x/g)) / 2
    
print("sqrt(x) =  ", x)    # Wurzel

# print "round(100.000056, 3) : ", round(100.000056, 3)