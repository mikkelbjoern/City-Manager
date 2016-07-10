""" buildingNames contains the names of the buildingtiers in order,
buildingPrices contains the current prices,
buildigIncome contains the current income per day,
buildingOwned contains the amount currently owned"""

buildingNames = ["House", "Manor","Castle", "City Hall","Spaceship"]
buildingPrices = [10, 50, 100, 1000, 956000]
buildingIncome = [1, 10, 25, 275, 4200]
buildingOwned = [0,0,0,0,0]

day = 0 #The current day
wealth = 10 #The players wealth

def statusMessage():#Sends a status message to the player.
    global cityName
    global wealth
    print("The city has a total wealth of: " + str(wealth))
    print(cityName + " has a total income of " + str(income()) +  " and currently consists of:")
    for i in range(len(buildingNames)):
        print("  -     " + buildingNames[i] + ": " + str(buildingOwned[i]))

def income():#Calculates the current income. Returns the income.
    n = 0
    for i in range(len(buildingOwned)):
        n = n + buildingOwned[i] * buildingIncome[i]
    return n

def sureCheck():#Asks if the player is sure about a choice. Returns a bool.
    print("Are you sure you wan't to continue? ")
    answer = input("If you are, write \" Yes \". Any other answer will be considered a no: ")
    if answer == "Yes":
        return True
    else:
        return False

def buyMenu():#The menu for buying new buildings
    global wealth
    print("These buildings can be bought at these prices:")
    for i in range(len(buildingNames)):
        print("  - " + buildingNames[i] + ", price: " + str(buildingPrices[i]) + " - income per day: " + str(buildingIncome[i]))
    decision = input("Which building do you want to buy? ")

    if decision in buildingNames:
        decisionNum = buildingNames.index(decision)
        print("You have " + str(wealth) + " in the bank. After this purchase you will have " + str(wealth - buildingPrices[decisionNum]))
        if buildingPrices[decisionNum] <= wealth:
            if sureCheck():
                wealth -= buildingPrices[decisionNum]
                prevOwned = buildingOwned[decisionNum]
                buildingOwned.pop(decisionNum)
                buildingOwned.insert(decisionNum, prevOwned+1)
                print("You have succesfuly bought a " + str(buildingNames[decisionNum]))
                print("Your new wealth is: " + str(wealth))
        else:
            print("You don't have enough money for that. \n")


    elif decision == "back":
        print("\n")
    else:
        print("That building couldn't be found in the list of buildings. Remember that upper and lower case matters.")
        print("To go back from the buy menu, write \"back\".")
        buyMenu()

def help():#The help menu
    print("These are the commands you can use:")
    print("* buy - used for buying new buildings")
    print("* status - shows the current status of the city")
    print("* end day - ends the days and starts a new one")
    print("* rename city - lets you rename the city")

def choices():#The main list of choices that the player has.
    print("\nWhat do you want to do? (write \"help\" for a list of avaible commands)")
    choice = input(" - ")
    if choice == "status" or choice == "see status":
        statusMessage()
    elif choice == "end day" or choice == "go to bed":
        newDay()
    elif choice == "buy":
        buyMenu()
    elif choice == "rename city":
        cityName = input("What should the new name of the city be? ")
    elif choice == "help":
        help()
    else:
        print("That is not a valid command.")

def newDay():#Starts a new day.
    global day
    global wealth
    wealth += income()
    day = day + 1
    print("\nThis is day " + str(day))
    statusMessage()


print("-------------       City Manager       ------------- \n")
cityName = input("What is the name of your city? ")
print("Welcome to " + cityName)

newDay()
while True:
    choices()
