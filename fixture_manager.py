                                #Luke Johnson

#This individual function reads the file. The use of the funciton using 'file,"r"' is to identify that the program is reading from
#a file. Later on throughout the program, it states the file being .txt. The function then reads the individual text file "data = file.read()
#followed by file.close().
#This returns the data as it has only been read and passes this into another function to process the data into an option that
#is selected by the user. "return" only passes back the data out of the function.
import time
def fileRead(file):
    file = open(file,"r")
    data = file.read()
    file.close()

    return(data)



#This displays the welcome message at the start of the program and is used to welcome the user within multiple options. For example,
#in option A it displays a welcome Message followed by taking the user through the option list.
def welcomeMessage():
    print("-"*55)
    print("\t\tFireside Fixtures")
    print("-"*55)
    print("Welcome to the Fireside Fixtures")





#The purpose of the split file function is to identifty to the user the selected pieces of data and to organise them in order by using the "\n".
#This seperates each field making it understandable to identify.
def splitFile(data):
    eachRecord = data.split("\n")

    dataList = []
    for  i in eachRecord:
        record=i.split(",")
        dataList.append(record)

    recordNumber = len(dataList)

    return(dataList,recordNumber)



#This function is very important in the program as this prompts the user with an input to select option A,B,C or Q (being quit). Their selection is
#passed into the variable optionSelect and is used in a while loop. The program will state within this while loop that when the input from the user
#is not equal to "!=" the values being A,B,C or Q, the program will display "That is an invalid option type". If the input by the user is equal to A,
#it will print "you have selected option A. The program will repeat this for all options apart from "q" when the program prints the selection of quitting
#fireside fixtures. If the input is equal to q, it will flow into another function called "quitFixtures()" where the user verifies that they are exiting.



def optionList():
    optionSelect=input("Please enter an option from the list below to continue the fireside fixtures:\n\n\tOption A: (A)\n\tOption B: (B)\n\tOption C: (C)\n\n\tOr (Q) for Quit\n").upper()
    while optionSelect != "A" and optionSelect != "B" and optionSelect != "C" and optionSelect != "Q":
        print("That is an invalid option type")
        optionSelect=input("Please re enter an option being a,b,c or q to continue:").upper()
    print("Thank you for entering the correct option type being {0}".format(optionSelect))

    if optionSelect == "A":
        print("you have selected option A\t")

        optionA()
    elif optionSelect == "B":
        print("you have selected option b\t")
        optionB()
    elif optionSelect == "C":
        print("you have selected option c\t")
        optionC()
    else:
        print("you have selected to quit Fireside Fixtures?")
    
        quitFixtures()

#Option A contains a 'while True' block when the input for a fixture number is entered to identify if the selection made is between 1 and 190. It uses the basic
#operators suchas '<' and '>' to identify to the user what numbers are present within the text file. If the selection made by the user is false, the program will
#ask the user to re-enter the fixture number within the same variable being "fixtureInput". The program then assigns the boolean operator to False within the logic
#of the extraction of data in the file. The program uses a for loop, looking up a fixture value contained in the fixture number selection. Before displaying the data
#to the user, it runs an if statement to identify if the record number withtin the text file meets the fixture input from the user. Once this meets the condition, it assigns
#fixture found to true and displays the data from [0] - [6].        

def optionA():
    while True:
        try:
            fixtureInput=int(input("To start please enter a fixture number to continue:"))
            while fixtureInput <1 and fixtureInput >190:
                print("This is an incorrect fixture number becasue it is not in the file.")
                fixtureInput=int(input("To start please enter a fixture number to continue:"))
            break
        except ValueError:
            print("Please enter a numerical value")
        

    fixtureFound=False
    for i in range(fixtureValue):
        nextRecord=fixtureData[i]
        if int(nextRecord[0])==fixtureInput:
            fixtureFound=True
            fixtureNumber=nextRecord[0]
            fixtureDate=nextRecord[1]
            playerOne=nextRecord[3]
            playerTwo=nextRecord[4]
            fixturePlayed=nextRecord[5]
            playerWin=nextRecord[6]

    if fixtureFound==False:
        print("That fixture has not been found")
        optionList()
    else:
        print("The details for this fixture are:".format(fixtureInput))
        print("-"*150)
        print("Fixture Number\tFixture Date\tPlayer One\tPlayer Two\t Total Fixtures\t\t\tWinning Player")
        print("-"*150)
        print("{0:10}\t{1:12}\t{2:10}\t{3:15}\t\t{4:21}\t{5:16}".format(fixtureNumber,fixtureDate,playerOne,playerTwo,fixturePlayed,playerWin))
        print()

        replayFixture()
        
        

#Option B displays all the upcoming fixtures including "fixture number", "fixture date", "fixture time", player 1, player 2. The function first assigns number of outstanding
#to 0 before the logic starts avoiding the error that it has not been defined. The for loop looks at the length of fixtureValue and for each character it contains is the number
#of times that the data is being validated. The program will assign each variable a unique location from 0 - 4, much like positioning then it will print the data using .format.
#At the end of option B, after the data has been printed it will look up the number of outstanding fixtures by looking at the number of outstanding being 69.




def optionB():
    print("This will display the fixtures upcoming:\n")
    print("==========================================================================================")
    print("Fixture Number\tFixture Date\tFixture Time\tPlayer 1 Nickname\tPlayer 2 Nickname")
    print("==========================================================================================")

    numberofOutStanding=0
    for i in range(fixtureValue):
        nextRecord=fixtureData[i]
        if nextRecord[5] == "":
            outstandingNumber=nextRecord[0]
            outstandingDate=nextRecord[1]
            outstandingTime=nextRecord[2]
            playerOne=nextRecord[3]
            playerTwo=nextRecord[4]
            numberofOutStanding=numberofOutStanding+1
            
            print("{0:9}\t{1:12}\t{2:12}\t{3:16}\t{4}".format(outstandingNumber,outstandingDate,outstandingTime,playerOne,playerTwo))
    print()
    print("\t\t\tThe number of outstanding fixtures are:{0}".format(numberofOutStanding))
    print()
    replayFixture()


#The purpose of option C is to display all the player information and to calculate a score based on the numebr of matches won and the number of matches played. Option C will then
#present all the information in a leaderboard from highest to lowest based on the score from each field of data.

def optionC():
    print("This will calculate the points for each player and display them in a leader board\n")
    print("===========================================================================================================")
    print("Player Nickname\t\tMatches Played\t\tMatches Won\t\tMatches Lost\t\tPoints")
    print("===========================================================================================================")


    scores=[]
    for i in range(resultsQuantity):
        nextRecord=resultsData[i]
        subList = []
        subList.append(int(nextRecord[2])*3)
        subList.append(nextRecord[0])
        subList.append(int(nextRecord[1]))
        subList.append(int(nextRecord[2]))
        subList.append(int(nextRecord[3]))
        scores.append(subList)

    scores.sort(reverse=True)
    topScoreNumber=len(scores)

    for j in range(topScoreNumber):
        eachUser = scores[j]
        if int(eachUser[3])>=3:
            playerName=str(eachUser[1])
            amountPlayed=int(eachUser[2])
            matchesWon=int(eachUser[3])
            matchesLost=int(eachUser[4])
            points=int(eachUser[0])
            print("{0:^13}\t{1:16}\t{2:14}\t{3:23}\t{4:20}".format(playerName,amountPlayed,matchesWon,matchesLost,points))

    print()       
    replayFixture()


#Quit fixtures is a function that asks the user if they would like to quit the fixtures setup. Firslty it asks the user to enter Y for Yes or N for No within a while loop containing
#the conditions that the input must meet either Y or N. I have also included a string method being .upper() allowing the user to enter a lower case character and converts this to upper
#case therefore meeting the condition. The and operator is included because there is more than one condition that can be met. When the input is Y for Yes, the program will return one line
#prinitng goodbye. On the other hand, if the user selects N for No, the program will run optionList() that has access to all fixture options from A - C.


def quitFixtures():
    quitVerification=input("Do you wish to proceed quitting fireside Fixtures, if so please respond either with,\n\t Y for yes or N for no:").upper()
    while quitVerification != "Y" and quitVerification != "N":
        print("Incorrect selection")
        quitVerification=input("Please re enter an option either being Y for Yes or N for no:").upper()
    print()
    print("Thankyou for entering the correct option")

    if quitVerification == "Y":
        print("Goodbye")
        

    else:
        optionList()


def replayFixture():
    replayFixture=input("Would you like to proceed with another fixture, please enter Y for Yes or N for No:").upper()
    while replayFixture != "Y" and replayFixture != "N":
        print("That is an incorrect selection")
        replayFixture=input("please enter Y for Yes or N for No to replay a fixture:").upper()
    print()
    print("Thankyou for entering the correct selection")

    if replayFixture == "Y":
        print("moving selection to option list...")
        time.sleep(3.00)
        
        optionList()
        

    else:
        print("Thankyou for using Fixture Manager")
        quit()

        
        

#This identifies the name and type of file that is being read in file read.

fixtures=fileRead("firesideFixtures.txt")
#outstanding=fileRead("firesideFixtures.txt")
results=fileRead("firesideResults.txt")
fixtureData,fixtureValue=splitFile(fixtures)
#outstandingData,outstandingQuantity=splitFile(outstanding)
resultsData,resultsQuantity=splitFile(results)
welcomeMessage()
optionList()
