import random
print("Press any key to generate an MLB team. Press q to quit")
mlblist = ["Dodgers","Padres","Giants","Rockies","Diamondbacks","Cardinals","Brewers","Cubs","Pirates","Reds","Nationals","Mets","Braves","Marlins","Phillies","Yankees","Blue Jays","Orioles","Rays","Red Sox","Astros","Angels","Athletics","Mariners","Rangers","Tigers","Twins","Guardians","White Sox","Royals"]
while True:
    z = input()
    if z == "q" or z == "Q":
        break
    else:
        x = random.randrange(30)
        print(mlblist[x])