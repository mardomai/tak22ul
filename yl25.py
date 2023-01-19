päevik = {
"eesnimi": "Mardo",
"perenimi": "Mai",
"elukoht": "Kuressaare",
"lemmik magustoit": "Jäätis"
}

print(päevik.get("elukoht"))
print(päevik["elukoht"])

päevik.update({"lemmik magustoit": "Pannkook" })

print(päevik.keys())

print(päevik.values())

if 'isikukood' in päevik :
    print("On isikukood")
else:
    print("Pole isikukoodi")

print(len(päevik))

päevik.update({"pikkus": len(päevik)})

päevik.pop("sünniaasta")

del päevik
