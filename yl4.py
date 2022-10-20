a = int(input (" Sisesta esimene number : "))
b = int(input ("Sisesta teine number: "))

def minimum(a, b):
      
    if a <= b:
        return a
    else:
        return b
      
print(minimum(a, b))