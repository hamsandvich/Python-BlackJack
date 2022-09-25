

from glob import glob
import random



userMoney= 0
name = ""

def main():

    global name
    global userMoney

    name, userMoney = loadGameState()

    if name == "":
        print("\n\nWelcome To Black Jack\n")
        name = input("Please type in your name:")
    else:
        print("\n\nWelcome Back {0}! \nYour Current balance is {1}$\n\n".format(name,str(userMoney)))
    
    print("Main Menu\n---------\n\n1) Start Game  \n2) Quit \n")
    choice = getIntInput(2)
    menu(choice)


    

# this Tries loads the players state if the file doesn't exest when it trys to load it the exception will create the file and return a balance of 100$ and a black name
def loadGameState():
    try:
        file = open("save.txt", "r")
        l = file.readlines()
        file.close()
        if l[0] == "" or l[1] == "":
            if l[0] == "" and len(l[1]) >= 1:
                return "No Name", int(l[1])
            if len(l[0]) >= 1 and l[1] == "":
                return l[1],100
        return l[0].strip("\n"),int(l[1])

    except:
        file = open("save.txt", "x")
        file.close()
        return "" , 100

# fix the order of name / money
def saveGameStat(name, userMoney):
    lines = [str(name),str(userMoney)]
    file = open("save.txt", "w")
    file.write('\n'.join(lines))
    file.close


def getIntInput(number):
    while True:
        try:
            integer = int(input("Please input your choice: "))
        except ValueError:
            print("Not an integer, please try again")
            continue
        
        if integer > number or integer <= 0:
            print("Please, enter a valid input")
        
        else:
            return integer

def getchar(str1, str2):
    while True:
        userStr = input("Please, enter a input")
        if userStr.capitalize() == str1 or userStr.capitalize() == str2:
            return userStr

def menu(case):
    match case:
        case 1:
            print("\n\nWhat Type of bets would you want?\n---------------------------------\n")
            print("1) Normal Bets (1,5,10,50,100)\n2) HighRoller (1000,2500,5000,10000)\n")
            choice = getIntInput(2)
            if choice == 1:
                lowBetting()
            else:
                if userMoney < 10000:
                    highBetting()
                else:
                    print("You Don't have enought money for this mode :(")
                    lowBetting()
        case 2:
            saveGameStat(name, userMoney)
            quit()

def placeBet(betAmount1,betAmount2,betAmount3,betAmount4,betAmount5):
    firstBet = False
    global userMoney
    bet = 0
    while True:
        if firstBet == False:
            print("\nHow much do you want to bet\n--------------------------- \n\n 1) 1\n 2) 5 \n 3) 10 \n 4) 50 \n 5) 100\n")
            choice = getIntInput(6)
            if choice == 1 and userMoney >= betAmount1:
                bet += betAmount1
                userMoney -= betAmount1
            elif  choice == 1 and userMoney < betAmount1:
                print("\nYou don't have enough for this bet. Your balance is {0}".format(userMoney))
            if choice == 2 and userMoney >= betAmount2:
                bet += betAmount2
                userMoney -= betAmount2
            elif  choice == 2 and userMoney < betAmount2:
                print("\nYou don't have enough for this bet. Your balance is {0}".format(userMoney))
            if choice == 3 and userMoney >= betAmount3:
                bet += betAmount3
                userMoney -= betAmount3
            elif  choice == 3 and userMoney < betAmount1:
                print("\nYou don't have enough for this bet. Your balance is {0}".format(userMoney))
            if choice == 4 and userMoney >= betAmount4:
                bet += betAmount4
                userMoney -= betAmount4
            elif  choice == 4 and userMoney < betAmount4:
                print("\nYou don't have enough for this bet. Your balance is {0}".format(userMoney))
            if choice == 5 and userMoney >= betAmount5:
                bet += betAmount5
                userMoney -= betAmount5
            elif  choice == 5 and userMoney < betAmount5:
                print("\nYou don't have enough for this bet. Your balance is {0}".format(userMoney))
            firstBet = True
        print("\nYour current bet is {0}$\n-----------------------\n\n 1) Deal \n 2) Increase Bet\n".format(bet))
        choice = getIntInput(2)
        if choice == 1:
            return bet

        elif choice == 2:
            print("\nHow much do you want to add to your bet?\n---------------------------------------- \n\n 1) 1$\n 2) 5$ \n 3) 10$ \n 4) 50$ \n 5) 100$\n")
            choice = getIntInput(6)
            if choice == 1 and userMoney >= betAmount1:
                bet += betAmount1
                userMoney -= betAmount1
            elif  choice == 1 and userMoney < betAmount1:
                print("\nYou don't have enough for this bet. Your balance is {0}".format(userMoney))
            if choice == 2 and userMoney >= betAmount2:
                bet += betAmount2
                userMoney -= betAmount2
            elif  choice == 2 and userMoney < betAmount2:
                print("\nYou don't have enough for this bet. Your balance is {0}".format(userMoney))
            if choice == 3 and userMoney >= betAmount3:
                bet += betAmount3
                userMoney -= betAmount3
            elif  choice == 3 and userMoney < betAmount1:
                print("\nYou don't have enough for this bet. Your balance is {0}".format(userMoney))
            if choice == 4 and userMoney >= betAmount4:
                bet += betAmount4
                userMoney -= betAmount4
            elif  choice == 4 and userMoney < betAmount4:
                print("\nYou don't have enough for this bet. Your balance is {0}".format(userMoney))
            if choice == 5 and userMoney >= betAmount5:
                bet += betAmount5
                userMoney -= betAmount5
            elif  choice == 5 and userMoney < betAmount5:
                print("\nYou don't have enough for this bet. Your balance is {0}".format(userMoney))
  
def score(deckList, splt):

    score = 0
    for i in range(deckList):
        if i[1] == "K":
            score += 10
        if i[1] == "J":
            score += 10
        if i[1] == "Q":
            score += 10
        else:
            score += int(i[1:])
    return score



def deal(deck):
    stand = 17
    blackJack = 21
    playerScore = 0
    playHand = []
    dealerScore = 0
    dealerHand = []
    split = False
    
    playHand.append(deck.pop())
    dealerHand.append(deck.pop())
    playHand.append(deck.pop())
    dealerHand.append(deck.pop())
    playerScore = score(playHand)
    dealerHand = score(dealerHand[1])
    print("Dealer hand is {0}, {1}\n \n \n \n",(dealerHand[1], dealerScore))

    print("Player hand is {0}, {1}", (playHand.join(" "), playerScore) )





def game(bet):
    deck = ["D1","D2","D3","D4","D5","D6","D7","D8","D9","D10","DJ","DQ","DK","DA","C1","C2","C3","C4","C5","C6","C7","C8","C9","C10","CJ","CQ","CK","CA","H1","H2","H3","H4","H5","H6","H7","H8","H9","H10","HJ","HQ","HK","HA","S1","S2","S3","S4","S5","S6","S7","S8","S9","S10","SJ","SQ","SK","SA"]
    # possible a better way to make the deck in case of simplicity i just used the above method 
    #deck = [i + j for i in ['D', 'C', 'H', 'S'] for j in ['1', '2', '3' 'J', 'Q', 'K']]
    playWon = False
    playerDoubleDown = False
    
    suffleDeck = random.shuffle(deck)
    playerWon, playerDoubleDown = deal(suffleDeck)

    




    



def lowBetting():
    while True:
        bet = placeBet(1,5,10,50,100)
        game(bet)
        print("Your balance is {0}$ \n")
        print("Play again Y or N")
        choice = getchar("Y" , "N")
        if  choice == "N":
            print("1) Start Game  \n2) Quit ")
            choice = getIntInput(2)
            menu(choice)


def highBetting():
    while True:
        bet = placeBet(250,500,1000,5000,10000)
        game(bet)
        print("Your balance is {0}$ \n")
        print("Play again Y or N")
        choice = getchar("Y" , "N")
        if  choice == "N":
            print("1) Start Game  \n2) Quit ")
            choice = getIntInput(2)
            menu(choice)

main()