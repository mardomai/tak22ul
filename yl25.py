dictionary = {
   "ees-nimi=": "Mardo",
   "perekonna-nimi=": "Mai",
   "sünni-aasta=": "2006",
   "elamis-koht=": "Uduvere",
   "lemmik-magustoit=": "Jäätis"
}

dictionary.update({"lemmik-magustoit=": "Ice cream" })

for x, y in dictionary.items():
  print(x, y)

 

if 'ID' in dictionary :
    print("Have ID")
else:
    print("No have ID")

print(len(dictionary))

dictionary.update({"length": len(dictionary)})

dictionary.pop("sünni-aasta=")

del dictionary