a = float(input("Esimene külg:"))
b = float(input("Teine külg:"))
c = float(input("Kolmas külg:"))

if a == b == c:
    print ("Võrdkülgne")
elif (a <= 0) or (b <=0) or (c <=0):
    print("Pole võimalik")
elif a == b:
    print("Võrdhaarne")
else:
    print("Erikülgne")