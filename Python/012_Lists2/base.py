import random
x = int(input("How many random numbers would you like?  "))
q = 0;


numlist = []
for q in range (0, x):
    numlist.append(random.randrange(1,11))
    print(numlist[q], end = ", ")





    