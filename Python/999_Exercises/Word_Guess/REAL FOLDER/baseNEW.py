import random
wordlist = []
with open('allow_words.txt') as f:
    for line in f:
        l = line.strip()
        wordlist.append(l)
y = 6
a = 0
num = random.randrange(0, 12972)
word = wordlist[num]

for x in range (0, 6):
    guess = input("Guess a 5-letter word  ")
    y = y - 1
    if guess == word:
        print("CORRECT!")
        a = 1
        break
    else:
        print("Sorry, that's incorrect. You have " + str(y) + " guesses remaining.")
        
f.close()
if a == 0:
    print("You are out of guesses! The word was " + word)