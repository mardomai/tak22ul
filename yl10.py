name = input("Mis su nimi on?: ")

print("Tere",name,)

elukoht = input("Kus sa elad?: ")

if elukoht == "Saaremaa":
    print("Ah norm, mis chillid!")

age = int(input("Kui vana sa oled?: "))

if age < 18:
    print("Liiga noor, et autot juhtida.")
elif age == 18:
    print("Sa võid legaalselt Karli käppida nüüd!")
elif age > 18:
    print("Võid autot juhtida.")