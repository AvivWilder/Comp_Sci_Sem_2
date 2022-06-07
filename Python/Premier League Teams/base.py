import random
print("Press any key to generate an Premier League team. Press q to quit")
premierleaguelist = ["Manchester City","Liverpool","Manchester United","Chelsea","West Ham","Arsenal","Tottenham","Wolves","Brighton","Leicester City","Aston Villa","Southampton","Crystal Palace","Brentford","Leeds United","Everton","Norwich City","Newcastle","Watford","Burnley"]
while True:
    z = input()
    if z == "q" or z == "Q":
        break
    else:
        x = random.randrange(20)
        print(premierleaguelist[x])