import random
print("Guess the random # from 1-1000. The program will tell you to guess higher or lower")
guess = ""
x = random.randrange(1,1001)
while True:
    guess = int(input(""))
    if guess == x:
        print("CORRECT!")
        break
    if guess > x:
        print("Lower")
    if guess < x:
        print("Higher")
    print("")