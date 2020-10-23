                                                                #Luke Johnson    




def welcomeMessage():

    print("\t============================================")
    print("\t===============Fee Calculator================")
    print("\t============================================")
    #This is the main body of the program and contains multiple functions responsible for data flow.


def playerDetails():

    #This asks the user for their email address included in a while loop and must meet the condition. The variable emailCorrect is set to False
    #at the start of the for loop to identify the condition has not been met. Then another variable emailAddress asks the user for the input
    #and this variable has each individual character looked at to see if the '@' symbol is present in the variable.


    emailCorrect=False
    while emailCorrect==False:
        emailAddress=input("\nPlease enter your email address including the '@' symbol: ")
        for i in range(len(emailAddress)):
            if emailAddress[i] == "@":
                print("\nthank you for entering the correct email address\n")
                emailCorrect=True


    #This asks the user to input a skill level, E for expert or C for casual. I then has a condition to meet
    #if the skill level is not equal to the condition, the program will repeat the line until it has been met.


    skillLevel=input("\nCan you please enter your skill level using\n(E) for 'Expert' or (C) for 'Casual': ").upper()
    while skillLevel != "E" and skillLevel != "C":
        print("I'm sorry but that is the incorrect skill level")
        skillLevel=input("\nCan you please re enter your skill level using\n(E) for 'Expert' or (C) for 'Casual': ").upper()
    print("Thank you for entering your skill level as {0}".format(skillLevel))


    #This assigns the skill level to a skill cost, being an expert will result in the skill cost being 35.00. This is later used to calculate an exchange rate
    #Based on the countery and the skill level.


    if skillLevel == "E":
        skillLevel = "Expert"
        skillCost=35.00


    #This assigns the skill level to a skill cost, being a casual will result in the skill cost being 20.00. This is later used to calculate an exchange rate
    #Based on the country and the skill level.


    else:
        skillLevel = "Casual"
        skillCost=20.00

    #This is assigning skillCost to fee that is later passed into feePlayer.

    fee=feePlayer(skillCost)

    #This while loop asks the user to enter their appropriate country from the list and will later pass this into another function to
    #calculate the total fee with the exchange rate of the selected country.


    country=input("\nPlease enter the appropriate country to continue the entry fee\t\n UK (United Kingdom)\t\n US (United States)\t\n AU (Australia)\n").upper()
    while country != "UK" and country != "US" and country != "AU":
        print("\nIm sorry but that does not meet the requirements")
        country=input("\nPlease enter the appropriate country to continue the entry fee,\n either UK (United Kingdom), US (United States), or AU (Australia):\n").upper()
    print("Thank you for entering {0} as a country!".format(country))


    #This if statement will determine the country name and will assign it to the currecy being "GBP" and states that the total cost is exchange_UK.
    if country == "UK":
        print("United Kingdom selected")
        totalCost=exchange_UK(fee)
        currency="GBP"


     #This if statement will determine the country name and will assign it to the currecy being "USD and states that the total cost is exchange_US.
    elif country == "US":
        print("United States Of America selected")
        totalCost=exchange_US(fee)
        currency="USD"


    #This if statement will determine the country name and will assign it to the currecy being "AUD" and states that the total cost is exchange_AU.
    else:
        country = "Australia"
        print("Australia selected")
        totalCost=exchange_AU(fee)
        currency="AUD"
    return(totalCost,currency,country)


    #Sets the player fee to 10.00 and adds this to the skill cost to later be used when displaying.
def feePlayer(skillCost):
    playerFee = 10.00
    totalFee=playerFee+skillCost
    return (totalFee)


    #This calculates the exchange rate (1.00) for United Kingdom using the fee of the player. This will then later be used to pass into another function to display
    #the total fee with the correct exchange rate.

def exchange_UK(feePlayer):
    totalCost=feePlayer*1.00
    
    return (totalCost)
    #This calculates the exchange rate (1.50) for United States using the fee of the player. This will then later be used to pass into another function to display
    #the total fee with the correct exchange rate.    

def exchange_US(feePlayer):
    totalCost=feePlayer*1.50
    return (totalCost)

    #This calculates the exchange rate (2.00) for Australia using the fee of the player. This will then later be used to pass into another function to display
    #the total fee with the correct exchange rate.

def exchange_AU(feePlayer):
    totalCost=feePlayer*2.00
    return (totalCost)

    #This function will display the final cost including the entry fee and the exchange rate for the skill level. 

    




def displayTotal(totalCost,currency,country):
    print("Your total fee based on your country being {0} is {1:.2f} {2}".format(country,totalCost,currency))




def generateNewFee():

    #This asks the user if they would like to generate a new fee, if they select Y it will loop back to the welcome message that then runs the main body of the program
    #If the user selects N it wikll exit the fee calculator.

    newFee=input("\nWould you like to calculate another fee, please enter Y for Yes or N for No:").upper()
    while newFee != "y" and newFee != "Y" and newFee != "n" and newFee != "N":
        print("\nIm sorry but that does not meet the requirements")
        newFee=input("\nplease enter Y for Yes or N for No to continue:").upper()
    print("Thankyou for using Fee Calculator")

    #This if statement will determine if the new fee is equal to "y" or "Y" and if this condition is met it will display the welcome message and player details.

    if newFee == "y" or newFee =="Y":
        welcomeMessage()
        totalCost,currency,country=playerDetails()
        displayTotal(totalCost,currency,country)
        generateNewFee()

    #This else statement will exit the program using exit()terminating the program.
    else:
        print("Goodbye")
        exit()



    #This will run the welcome message firt, then assigns total cost and currency to player details.
welcomeMessage()
totalCost,currency,country=playerDetails()
displayTotal(totalCost,currency,country)
generateNewFee()
