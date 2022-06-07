print("Box Maker")
print("---------")
o = input("Enter a character  ")
x = int(input("Enter box width  "))
y = int(input("Enter box height  "))

g = 0;
f = 0;

for g in range (0, y):
    for f in range (0, x):
        print(o, end="")
    print("")
    