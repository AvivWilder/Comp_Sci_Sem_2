import random
print("Press any key to generate an NFL team. Press q to quit")
nfllist = ["Rams","Cardinals","Seahawks","49ers","Vikings","Packers","Bears","Lions","Saints","Panthers","Buccaneers","Falcons","Eagles","Cowboys","Football Team","Giants","Patriots","Dolphins","Jets","Bills","Bengals","Steelers","Ravens","Browns","Chargers","Broncos","Chiefs","Raiders","Colts","Texans","Jaguars","Titans"]
while True:
    z = input()
    if z == "q" or z == "Q":
        break
    else:
        x = random.randrange(32)
        print(nfllist[x])