x = input("What is your first and last name? ")
y = ""

for i in range (0,len(x)):
    y = x[i:i+1]
    print(y)
    if y == " ":
        first = x[0:i]
        last = x[i+1: len(x)]
    
print("")
print(first)
print(last)