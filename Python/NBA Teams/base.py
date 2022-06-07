import random
print("Press any key to generate an NBA team. Press q to quit")
nbalist = ["Heat","Bulls","Nets","Bucks","Cavaliers","76ers","Hornets","Raptors","Celtics","Wizards","Knicks","Hawks","Pacers","Pistons","Magic","Suns","Warriors","Grizzlies","Jazz","Mavericks","Nuggets","Clippers","Lakers","Timberwolves","Trail Blazers","Pelicans","Spurs","Kings","Rockets","Thunder"]
while True:
    z = input()
    if z == "q" or z == "Q":
        break
    else:
        x = random.randrange(30)
        print(nbalist[x])