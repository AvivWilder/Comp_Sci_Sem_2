x = 0
t = 0
grocerylist = []
pricelist = []
i = int(input("How many items are you purchasing?  "))
print("---------------------------------------")
for x in range (0, i):
    y = input("What is item # " + str(x + 1) + "?  ")
    grocerylist.append(y)
    z = float(input("How much did item # " + str(x + 1) + " cost?  "))
    pricelist.append(z)
    t = t + pricelist[x]
    print("---------------------------------------")
x = 0;
print("Receipt")
print("---------------------------------------")
print
for x in range (0, i):
    print(str(grocerylist[x]) + " ------ $" + str(pricelist[x]))
print("---------------------------------------")
print("Total ----- $" + str(t))
print("---------------------------------------")