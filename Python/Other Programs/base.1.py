import random
x = input("Enter a word: ")

y = ""
letterlist = []

for i in range (0, len(x)):
    y=x[i:i+1]
    letterlist.append(y)
    
letterlist2 = []    

q = 0
for i in range (0, len(letterlist)):
    q = random.randrange(0,len(letterlist))
    letterlist2.append(letterlist[q])
    letterlist.remove(letterlist[q])
    
for i in range (0, len(letterlist2)):
    print(letterlist2[i],end = "")