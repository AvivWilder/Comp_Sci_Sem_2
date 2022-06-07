print("You can enter as many numbers as you wish")
numberlist = []
numberlist2 = []
total = 0
y = 0
while True:
    x = input("Enter a number, press q to quit ")
    if (x == 'q'):
        break
    x = int(x)
    numberlist.append(x)
    numberlist2.append(x)
    total = (int(x) + total)
    y = y + 1

q = 0
maxx = 0

for b in range (0,len(numberlist)):
    for c in range (0, len(numberlist)):
        if numberlist[b] >= numberlist2[c]:
            q = q + 1
    if (q == len(numberlist)):
        maxx = numberlist[b]
        break
    q = 0
    
    
b = 0
c = 0
minn = 0
    
for b in range (0,len(numberlist)):
    for c in range (0, len(numberlist)):
        if numberlist[b] <= numberlist2[c]:
            q = q + 1
    if (q == y):
        minn = numberlist[b]
        break
    q = 0
    
    
average = total/len(numberlist)
print("-----------------------------")
print("Max: " + str(maxx))
print("Min: " + str(minn))
print("Average: " + str(average))
