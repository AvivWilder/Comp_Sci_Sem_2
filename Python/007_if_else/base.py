print("Aviv's History Quiz")
print("-------------------")
abc = int(input("What year was the war of 1812 fought?    "))
if abc == 1812:
    print("Correct")
elif abc < 1600 or abc > 2000:
    print("You're kidding, right?")
elif abc < 1700 or abc > 1900:
    print("Not even close")
elif abc < 1750 or abc > 1900:
    print("Close, but no")
