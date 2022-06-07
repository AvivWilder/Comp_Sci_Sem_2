import random
print("Press any key to generate an NHL team. Press q to quit")
nhllist = ["Panthers","Lightning","Maple Leafs","Bruins","Red Wings","Sabres","Senators","Canadiens","Hurricanes","Penguins","Rangers","Capitals","Blue Jackets","Islanders","Devils","Flyers","Avalanche","Predators","Blues","Wild","Stars","Jets","Blackhawks","Coyotes","Golden Knights","Ducks","Kings","Flames","Sharks","Oilers","Canucks","Kraken"]
while True:
    z = input()
    if z == "q" or z == "Q":
        break
    else:
        x = random.randrange(32)
        print(nhllist[x])