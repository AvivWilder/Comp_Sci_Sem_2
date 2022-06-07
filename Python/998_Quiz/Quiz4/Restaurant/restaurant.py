import random
restaurantlist = ["Panda Express","McDonalds","Subway","Pizza Hut","Taco Bell","Wingstop","Starbucks","Dunkin Donuts","IHOP","Wienerschnitzel","Olive Garden","Wetzels Pretzels","Arby's","El Pollo Loco","Outback Steakhouse"]
pandaexpresslist = ["Orange Chicken","Beijing Beef","Kung Pao Chicken","Honey Sesame Chicken","Chicken Teriyaki","Beef and Broccoli"]
mcdonaldslist = ["Big Mac","Quarter Pounder","Filet o Fish","10 pc Chicken McNuggets","Egg McMuffin"]
subwaylist = ["Meatball Marinara","Italian BMT","Turkey Club","Steak & Cheese","Tuna Melt"]
pizzahutlist = ["Cheese Pizza","Pepperoni Pizza","Meat Lovers Pizza","Veggie Pizza","BBQ Chicken Pizza"]
tacobelllist = ["Doritos Locos Taco","Cantina Crispy Chicken Taco","Crunchwrap","Steak Quesadilla","Chicken Quesadilla"]
wingstoplist = ["Original Hot Wings","Lemon Pepper Wings","BBQ Wings","Garlic Parmesan Winga","Cajun Wings","Hawaiian Wings"]
starbuckslist = ["Caramel Frappuccino","Mocha Cookie Crumble Frappuccino","Java Chip Frappuccino","Dark Roast Hot Coffee","Hot Chocolate","Chai Tea","Everything Bagel","Plain Bagel","Cinnamon Raisin Bagel","Iced Lemon Loaf","Ham and Cheese Croissant","Chocolate Croissant","Chocolate Chip Cookie","Birthday Cake Pop"]
dunkindonutslist = ["Hot Coffee","Americano","Cold Brew","Iced Coffee","Latte","Cappuccino","Egg & Cheese Sandwich","Bacon, Egg, & Cheese Sandwich","Sausage, Egg, & Cheese Sandwich","Apple Fritter","Bostom Cream Donut","Chocolate Cream Donut","Cruller","Jelly Donut","Eclair","Maple Cream Donut","Glazed Donut"]
ihoplist = ["Original Pancakes","Strawberry Banana Pancakes","Blueberry Pancakes","Cupcake Pancakes","Chocolate Chip Pancakes","Original French Toast","Strawberry Banana French Toast","Belgian Waffle"]
wienerschnitzellist = ["Chili Cheese Dog","Chicago Dog","Texas BBQ Dog","Corn Dog","Junkyard Dog","Polish Sandwich","Chili Cheese Egg Burrito"]
olivegardenlist = ["Chicken Alfredo","Shrimp Alfredo","Chicken Parmigiana","Fetuccine Alfredo","Cheese Ravioli","Lasagna Classico","Spaghetti with Meatballs","Spaghetti Bolognese"]
wetzelspretzelslist = ["Original Pretzel","Cinnamon Pretzel","Almond Crunch Pretzel","Pretzel Dog","Pretzel Cheese Dog","Pretzel Cheese Jalapeno Dog","Pretzel Bits","Cinnamon Bits","Almond Crunch Bits","Pizza Bits"]
arbyslist = ["Classic Roast Beef Sandwich","Beef and Cheddar Sandwich","Smokehouse Brisket Sandwich","Reuben Sandwich","Roast Beef Slider","Roast Turkey Slider","Chicken Slider","Crispy Chicken Sandwich","Roast Chicken Sandwich","Buffalo Crispy Chicken Sandwich","5 pc Chicken Tenders"]
elpollolocolist = ["10 pc Family Dinner","4pc Meal","Grilled Chicken Leg","Grilled Chicken Wing","Grilled Chicken Breast","Grilled Chicken Thigh","Chicken Tostada Salad","Original Pollo Bowl","Grande Avocado Chicken Bowl","Chicken Taco","Chicken Avocado Taco","Chicken Burrito","Queso Blanco Burrito","Chicken Avocado Burrito","Chicken Tinga Burrito"]
outbacksteakhouselist = ["Fried Shrimp","Mac & Cheese Bites","Special Wings","Filet Mignon Steak","Sirloin Steak","Ribeye Steak","New York Strip Steak","Porterhouse Steak","Fried Chicken","Baby Back Ribs","Grilled Porkchop"]



for x in range (0, len(restaurantlist)):
    print(str(x + 1) + ": " + restaurantlist[x])

y = int(input("Which restaurant would you like to explore? (enter the number) "))

print("")

if y == 1:
    print("Menu Items")
    print("----------")
    for x in range (0, len(pandaexpresslist)):
        print(pandaexpresslist[x])
    q = random.randrange(0, len(pandaexpresslist))
    print("------------------------------")
    print ("Suggested: " + pandaexpresslist[q])
    print("------------------------------")
    
    
    
if y == 2:
    print("Menu Items")
    print("----------")
    for x in range (0, len(mcdonaldslist)):
        print(mcdonaldslist[x])
    q = random.randrange(0, len(mcdonaldslist))
    print("------------------------------")
    print ("Suggested: " + mcdonaldslist[q])
    print("------------------------------")
    
    
    
if y == 3:
    print("Menu Items")
    print("----------")
    for x in range (0, len(subwaylist)):
        print(subwaylist[x])
    q = random.randrange(0, len(subwaylist))
    print("------------------------------")
    print("Suggested: " + subwaylist[q])
    print("------------------------------")
    

if y == 4:
    print("Menu Items")
    print("----------")
    for x in range (0, len(pizzahutlist)):
        print(pizzahutlist[x])
    q = random.randrange(0, len(pizzahutlist))
    print("------------------------------")
    print("Suggested: " + pizzahutlist[q])
    print("------------------------------")
    
    
if y == 5:
    print("Menu Items")
    print("----------")
    for x in range (0, len(tacobelllist)):
        print(tacobelllist[x])
    q = random.randrange(0, len(tacobelllist))
    print("------------------------------")
    print("Suggested: " + tacobelllist[q])
    print("------------------------------")


if y == 6:
    print("Menu Items")
    print("----------")
    for x in range (0, len(wingstoplist)):
        print(wingstoplist[x])
    q = random.randrange(0, len(wingstoplist))
    print("------------------------------")
    print("Suggested: " + wingstoplist[q])
    print("------------------------------")
    
    
if y == 7:
    print("Menu Items")
    print("----------")
    for x in range (0, len(starbuckslist)):
        print(starbuckslist[x])
    q = random.randrange(0, len(starbuckslist))
    print("------------------------------")
    print("Suggested: " + starbuckslist[q])
    print("------------------------------")
    
    
if y == 8:
    print("Menu Items")
    print("----------")
    for x in range (0, len(dunkindonutslist)):
        print(dunkindonutslist[x])
    q = random.randrange(0, len(dunkindonutslist))
    print("------------------------------")
    print("Suggested: " + dunkindonutslist[q])
    print("------------------------------")
    
    
if y == 9:
    print("Menu Items")
    print("----------")
    for x in range (0, len(ihoplist)):
        print(ihoplist[x])
    q = random.randrange(0, len(ihoplist))
    print("------------------------------")
    print("Suggested: " + ihoplist[q])
    print("------------------------------")
    
    
if y == 10:
    print("Menu Items")
    print("----------")
    for x in range (0, len(wienerschnitzellist)):
        print(wienerschnitzellist[x])
    q = random.randrange(0, len(wienerschnitzellist))
    print("------------------------------")
    print("Suggested: " + wienerschnitzellist[q])
    print("------------------------------")
    
    
if y == 11:
    print("Menu Items")
    print("----------")
    for x in range (0, len(olivegardenlist)):
        print(olivegardenlist[x])
    q = random.randrange(0, len(olivegardenlist))
    print("------------------------------")
    print("Suggested: " + olivegardenlist[q])
    print("------------------------------")
    
    
if y == 12:
    print("Menu Items")
    print("----------")
    for x in range (0, len(wetzelspretzelslist)):
        print(wetzelspretzelslist[x])
    q = random.randrange(0, len(wetzelspretzelslist))
    print("------------------------------")
    print("Suggested: " + wetzelspretzelslist[q])
    print("------------------------------")
    

if y == 13:
    print("Menu Items")
    print("----------")
    for x in range (0, len(arbyslist)):
        print(arbyslist[x])
    q = random.randrange(0, len(arbyslist))
    print("------------------------------")
    print("Suggested: " + arbyslist[q])
    print("------------------------------")
    
    
if y == 14:
    print("Menu Items")
    print("----------")
    for x in range (0, len(elpollolocolist)):
        print(elpollolocolist[x])
    q = random.randrange(0, len(elpollolocolist))
    print("------------------------------")
    print("Suggested: " + elpollolocolist[q])
    print("------------------------------")
    
    
if y == 15:
    print("Menu Items")
    print("----------")
    for x in range (0, len(outbacksteakhouselist)):
        print(outbacksteakhouselist[x])
    q = random.randrange(0, len(outbacksteakhouselist))
    print("------------------------------")
    print("Suggested: " + outbacksteakhouselist[q])
    print("------------------------------")