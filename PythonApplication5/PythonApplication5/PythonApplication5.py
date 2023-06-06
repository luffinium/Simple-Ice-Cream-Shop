print ("Welcome to The Ice Creamery.")
conePrices={"S":"$1.50","M":"$2.50","L":"$3.50"}
coneSizes={"S":"smallish","M":"more for me","L":"lotta lickin"}
flavorsList = ["Vanlla" , "Chocolate" , "Strawberry" , "Pistachio" , "Butter Pecan" , "Cookie Dough" , "Neapolitan"]
flavorsList [0] = "Fudge"
flavorsList.append("Coconut") 
flavorsList.sort()
flavorTotal = len(flavorsList)
print ("These are the " ,int((len(flavorsList))), " flavors we are serving today at The Ice Creamery ")
for y in range(flavorTotal):
            print(str(y+1)+" "+flavorsList[y])
looping = True
while looping:
    userSize = (input("Please enter the cone size of your choosing: S, M, or L:  ")) 
    validSize = True
    if userSize == "S":
        conePrices = "$1.50"
        coneSizes = "smallish"
    elif userSize == "M":
        conePrices = "$2.50"
        coneSizes ="more for me"
    elif userSize == "L":
        conePrices = "$3.50"
        coneSizes ="lotta lickin"
    else:
        validSize = False
    if validSize:
        userSize = coneSizes
        looping =False
    else:
        print ("Please use a valid size option S, M, or L.")

looping = True
while looping:
    userFlavor = (input("Please enter your flavor number: "))
    validFlavor = True
    if userFlavor == "1":
           flavorsList = "Butter Pecan"
    elif userFlavor == "2":
           flavorsList = "Chocolate"
    elif userFlavor == "3":
           flavorsList = "Coconut"
    elif userFlavor == "4":
           flavorsList = "Cookie Dough"
    elif userFlavor == "5":
           flavorsList = "Fudge"
    elif userFlavor == "6":
           flavorsList = "Neapolitan"
    elif userFlavor == "7":
           flavorsList = "Pistachio"
    elif userFlavor == "8":
           flavorsList = "Strawberry"
    else:
            validFlavor = False
    if validFlavor:
        userFlavor = flavorsList
        print("Your total is: " + conePrices)
        print("Your", userSize, "sized cone of The Ice Creamery's", userFlavor,  "will arrive shortly."
        "\n"
        "Thank you for visiting The Ice Creamery")
        looping = False
    else:
        print("Please choose a valid flavor from number one through eight.")
        
        

               