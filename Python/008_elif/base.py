adam = float(input("Enter a number   "))
alvin = input("Enter an operation (+ - * /)  ")
anthony = float(input("Enter a second number  "))
albert = 0;
albert = float(albert)

if alvin == "+":
    albert = adam + anthony
if alvin == "-":
    albert = adam - anthony
if alvin == "*":
    albert = adam * anthony
if alvin == "/":
    albert = adam / anthony

adam = str(adam)
anthony = str(anthony)
albert = str(albert)

print(adam + " " + alvin + " " + anthony + " = " + albert)