import random
x = 0;
while True:
    x = random.randrange(20) + 1;
    print (str(x) + " * 13");
    z = input()
    if int(z) == x*13:
        print("correct")