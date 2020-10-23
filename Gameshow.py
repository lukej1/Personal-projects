#Game show simulation

def welcomeMessage():

    print("\t"*3,"="*30)
    print("\t"*3,"="*5,"The Vegas Gameshow","="*5)
    print("\t"*3,"="*30)



#Inc all probabilities for the selection of boxes.
#Import time as a delay.
#Tell the user the new probability of winning when one
#of the selection boxes have been taken.

def mainBody():

    import time
    
    print("\n"*3)
    name=str(input("Welcome to the most competitive gameshow, we require your name to begin:"))
    print()
    print("\t"*3,"Thankyou for entering your name {0}".format(name))
    print()
    print("\t"*1,"Now {0}, you have now been entered into a gameshow and you""\n""\t"" must choose one out of three boxes in order to claim your prize!".format(name))
    time.sleep(3)
    print()
    print("\t"*1,"We are pleased to tell you {0} that the show host has just""\n""\t"" turned over one of the prize boxes and revealed no money, you""\n""\t""\t""\t"" have a greater chance in winning!".format(name))


def selectBox():
    print()
    boxSelection=input("\t""Please either select 'Box 1' by entering '1' or select 'box 2' by \n \t \t entering '2' to complete your chance in winning:")

    if boxSelection == "1":
        boxSelection="Box 1"
    else:
        boxSelection == "2"

    print("\n\t\tThankyou for selecting your box!")
    while boxSelection !="1" and boxSelection !="2":
        boxSelection=input("\n\t\tPlease enter either box 1 or 2 to be in a chance to win:")
        

    if boxSelection == "1":
        print()
        print("\n\t\t\tBox number:1")
    elif boxSelection == "2":

        print("\n\t\t\tBox number:2")
    else:
        print("That is an invalid Box number")


    
        

    
    
welcomeMessage()
mainBody()
selectBox()







