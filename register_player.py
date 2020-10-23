                                                    #Luke Johnson          


#This is a welcome message and is used to introduce the user to the program
def welcomeMessage():
    print("\t\t============================================")
    print("\t\t============League registration=============")
    print("\t\t============================================")



#This is where the player makes the selection for each field. The purpose of this being placed into a function is to 
def playerDetails():

#This is asking the player to enter their first name into League Registration
    firstName=input("\n\t\tHello and welcome to League registration, \n\t\tto continue please enter your First name: ").title()


#A while loop has been used to identify that the progam needs at minimum 1 character to proceed,
#if not it will generate an infinite loop until the condition has been met
    while len (firstName) <1:
        print("\t\tFirst name must be at least 1 character")
        firstName=input("\t\tplease re enter your First name: ").title()




#A while loop has been used to identify that the progam needs at minimum 1 character to proceed,
#if not it will generate an infinite loop until the condition has been met.
    surName=input("\n\t\tPlease enter your last name: ").title()
    while len (surName) <1:
        print("\t\tSurname must be at least 1 character")
        surName=input("\t\tplease re enter your Surname: ").title()
    
    nickName=input("\n\t\tPlease enter your nickname: ").title()
    


#This is a for loop and is responsible for looking at the length of the input by the user and
#finds an individial character in the string containing "@".
    emailCorrect=False
    while emailCorrect==False:
        emailAddress=input("\n\t\tPlease enter your email address: ")
        for i in range(len(emailAddress)):
            if emailAddress[i] == "@":
                print("\n\t\tthank you for entering the correct email address")
                emailCorrect=True
            
                
                        
                        

#This will ask the user to enter a skill level either being E for Expert or C for Casual.
    skillLevel=input("\n\t\tCan you please enter your skill level using\n\t\t(E) for 'Expert' or (C) for 'Casual': ").upper()
    while skillLevel != "C" and skillLevel != "E":
        print("\t\tSorry but that is the incorrect skill level")
        skillLevel=input("\t\tCan you please re enter your skill level using\n\t\t(E) for 'Expert' or (C) for 'Casual': ").upper()
    print("\n\t\tThank you for entering your skill level")


#This assigns the skill level as an individual character to its true value when it displays Player details.

    if skillLevel == "E":
        skillLevel == "Expert"

    elif skillLevel == "C":
        skillLevel == "Casual"
         
        
#This displays all the player details using .format from {0} - {4} clearly to the user including the type of data, for example email address: {3}.

    print("\n\t\t\tPlayer name: {0}"" ""{1}\n\t\t\tNickname: {2}\n\t\t\tEmail Address: {3}\n\t\t\tSkill Level: {4}".format(firstName,surName,nickName,emailAddress,skillLevel))

    verify=input("\n\n\t\tDoes this information look correct, \n\t\tif so please enter Y for Yes or N for No:").upper()
    while verify != "Y" and verify != "N":
        print("\n\t\tIncorrect selection")
        verify=input("\n\t\tPlease re enter an option either being Y for Yes or N for no:").upper()
    print()
    print("\n\t\tThankyou for entering the correct option")
#If the input is Y for Yes, the program will follow by running the exit() command that allows the user to select enter terminating the program.
    if verify == "Y":
        print("\n\n\t\tGoodbye")
        exit()
        
#If the user has selected N for No, the program will automatically run the welcome message followed by player details repeating the program.
    else:
        welcomeMessage()
        playerDetails()
        





#This shows the order of operation, firstly running the welcome message then by the main body "playerDetails".
welcomeMessage()
playerDetails()
