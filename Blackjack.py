
import random


userMoney= 0
name = ""

def main():

    global name
    global userMoney

    name, userMoney = loadGameState()

    if name == "":
        print("\n\nWelcome To Black Jack\n")
        name = input("Please type in your name: ")
        print("\n\nWelcome {}! We will start you with a balance of 100$ \n".format(name))
        saveGameStat(name, userMoney)
    else:
        print("\n\nWelcome Back {0}! \nYour Current balance is {1}$".format(name,str(userMoney)))
    
    print("\n\nMain Menu\n---------\n\n1) Start Game  \n2) Quit \n")
    choice = getIntInput(2)
    menu(choice)


    

# this Tries loads the players state if the file doesn't exest when it trys to load it the exception will create the file and return a balance of 100$ and a black name
def loadGameState():
    try:
        file = open("save.txt", "r")
        l = file.readlines()
        file.close()
        if len(l) == 0:
            return "", 100
        
        if l[0] == "" and len(l[1]) >= 1:
                return "No Name", int(l[1])
           
        elif l[1] == "":
            if len(l[0]) >= 1 and l[1] == "":
                return l[1],100
            else:
                return "", 100

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
        userStr = input("Please, enter a input: ")
        if userStr.upper() == str1 or userStr.upper() == str2:
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
                if userMoney >= 250:
                    highBetting()
                else:
                    print("\nYou Don't have enought money for this mode :(\n")
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
            print("\nHow much do you want to bet\n--------------------------- \n\n 1) {0}$\n 2) {1}$ \n 3) {2}$ \n 4) {3}$ \n 5) {4}$\n".format(betAmount1,betAmount2,betAmount3,betAmount4,betAmount5))
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
            print("\nHow much do you want to add to your bet?\n---------------------------------------- \n\n 1) {0}$\n 2) {1}$ \n 3) {2}$ \n 4) {3}$ \n 5) {4}$\n".format(betAmount1,betAmount2,betAmount3,betAmount4,betAmount5))
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
  
def score(hand):
    hasAce = False
    if type(hand) != list:
        card = hand
        hand = []
        hand.append(card)
    score = 0
    for i in range(len(hand)):
        c = hand[i]
        if c[1] == "K":
            score += 10
        elif c[1] == "J":
            score += 10
        elif c[1] == "Q":
            score += 10
        elif c[1] == "A":
            if score + 10 <= 21:
                score += 10
                hasAce = True
                
            else:
                score += 1
                hasAce = True
                
        else:
            score += int(c[1:])
    if score > 21 and hasAce == True:
        score -= 10 
    return score

def gameplayMenu(split,bet,Pass,hit,firstdeal):
    global userMoney
    choice = 0
    doubleDown = False

    
    
    if firstdeal == True and split == True:
        print("\n\nWhat's your move!\n-----------------\n\n1) Hit  \n2) Pass \n3) Double Down\n4) Split" )
        choice = getIntInput(4)
        firstdeal = False
        split = False
    
    elif firstdeal == True:
        firstdeal = False
        print("\n\nWhat's your move!\n-----------------\n\n1) Hit  \n2) Pass \n3) Double Down\n" )
        choice = getIntInput(3)
    else:
        print("\n\nWhat's your move!\n-----------------\n\n1) Hit  \n2) Pass \n")
        choice = getIntInput(2)
    
    match choice:

        case 1:
            hit = True
        case 2:
            Pass = True
        case 3:
            if userMoney - bet > 0:
                doubleDown = True
            else:
                print("\nYou don't have enough for this bet. Your balance is {0}".format(userMoney))
                hit = True
        case 4:
            split = True
    return Pass,hit,doubleDown,split,firstdeal

def deal(deck, bet):
    firstdeal = True
    split = False
    playerScore = 0
    playHand = []
    splitScore = 0
    splitHand = []
    dealerScore = 0
    dealerHand = []
    playerSplit = False
    doubleDown = False
    
    playHand.append(deck.pop())
    dealerHand.append(deck.pop())
    playHand.append(deck.pop())
    dealerHand.append(deck.pop())
    playerScore = score(playHand)
    dealerScore = score(dealerHand[1])
    print("\n\nDealer hand is {0}, {1}\n".format(dealerHand[1], dealerScore))

    print("Player hand is {0}, {1}".format(' '.join(playHand), playerScore) )
    
    if playHand[0][1:] == playHand[1][1:]:
        split = True

    #player loop
    while True:
        hit = False
        Pass = False
        hit2 = False
        Pass2 = False


        if (playerSplit != True) and (doubleDown != True):
            Pass, hit, doubleDown, playerSplit,firstdeal = gameplayMenu(split,bet,Pass,hit,firstdeal)
        
        if (playerSplit == True) and (split == True):
            splitHand.append(playHand.pop())
            playHand.append(deck.pop())
            splitHand.append(deck.pop())
            playerScore = score(playHand)
            print("Player hand is {0}, {1}".format(' '.join(playHand), playerScore) )
            splitHand = score(splitHand)
            print("Player split hand is {0}, Score: {1}".format(' '.join(splitHand), splitScore) )
            split == False

        elif playerSplit == True:
            if Pass != True:
                Pass, hit, doubleDown, playerSplit = gameplayMenu(split,bet,Pass,hit,firstdeal)
            if Pass2 != True:
                Pass2, hit2, doubleDown, playerSplit = gameplayMenu(split,bet,Pass,hit,firstdeal)
            
            if hit == True:
                playHand.append(deck.pop())
            if hit2 == True:
                splitHand.append(deck.pop())
            
            playerScore = score(playHand)
            print("Player hand is {0}, Score: {1}".format(' '.join(playHand), playerScore) )
            if playerScore > 21:
                print("Bust")
                playerScore = -1
                Pass = True

            splitHand = score(splitHand)
            print("Player split hand is {0}, Score: {1}".format(' '.join(splitHand), splitScore) )
            if splitScore > 21:
                print("Bust")
                splitScore = -1
                Pass2 = True
            
            if (Pass == True) and (Pass2 == True):
                split == True
                break
            
        elif doubleDown == True:
            playHand.append(deck.pop())
            playerScore = score(playHand)
            print("Player hand is {0}, Score: {1}".format(' '.join(playHand), playerScore) )
            if playerScore > 21:
                print("Bust")
                playerScore = -1
                
            break
        elif hit == True:
            playHand.append(deck.pop())
            playerScore = score(playHand)
            print("Player hand is {0}, Score: {1}".format(' '.join(playHand), playerScore) )
            if playerScore > 21:
                print("Bust")
                playerScore = -1
                break
        elif Pass == True:
            break
    dealerScore = score(dealerHand)
    print("\n\nDealer hand is {0}, Score: {1}\n".format(' '.join(dealerHand), dealerScore))

    if (playerScore == 21) or (playerScore == -1):
        dealerScore = random.randint(10,20)
        return playerScore, dealerScore, doubleDown, doubleDown, split

    #Computer Deal
    while True:

        if dealerScore < 17:
            dealerHand.append(deck.pop())
            dealerScore = score(dealerHand)
            print("\n\nDealer hand is {0}, Score: {1}\n".format(dealerHand, dealerScore))                
            if dealerScore > 21:
                print("Bust")
                dealerScore = -1
                break
        if (dealerScore >= 17) and (dealerScore < 21):
            break

    return playerScore, splitScore, dealerScore, doubleDown, split     



def game(bet):
    deck = ["\u26662","\u26663","\u26664","\u26665","\u26666","\u26667","\u26668","\u26669","\u266610","\u2666J","\u2666Q","\u2666K","\u2666A",
    "\u26672","\u26673","\u26674","\u26675","\u26676","\u26677","\u26678","\u26679","\u266710","\u2667J","\u2667Q","\u2667K","\u2667A",
    "\u26652","\u26653","\u26654","\u26655","\u26656","\u26657","\u26658","\u26659","\u266510","\u2665J","\u2665Q","\u2665K","\u2665A",
    "\u26642","\u26643","\u26644","\u26645","\u26646","\u26647","\u26648","\u26649","\u266410","\u2664J","\u2664Q","\u2664K","\u2664A"]
    # possible a better way to make the deck in case of simplicity i just used the above method 
    #deck = [i + j for i in ['D', 'C', 'H', 'S'] for j in ['1', '2', '3' 'J', 'Q', 'K']]
    global userMoney
    playerDoubleDown = False
    split = False
    playerScore = 0
    ComputerScore = 0
    SplitScore = 0
    
    random.shuffle(deck)
    playerScore, splitScore, dealerScore, playerDoubleDown, split = deal(deck,bet)

    if playerDoubleDown == True:
        userMoney -= bet
        if playerScore > dealerScore:
            if dealerScore == -1:
                print("\n\n\nDealer has bust Player wins {0}".format((bet *4)))
            print("\n\n\nPlayer score: {0}\nDealer score: {1}\n \nPlayer Wins {2}".format(playerScore,dealerScore,(bet *4)))
            userMoney += (bet *4)
        elif playerScore < dealerScore:
            if playerScore == -1:
                print("\n\n\nDealer has bust Player loses {0}".format((bet *2)))
            print("\n\n\nPlayer score: {0}\nDealer score: {1}\n \nPlayer looses {2}".format(playerScore,dealerScore,(bet *2)))
        elif playerScore == dealerScore:
            print("\n\n\nPlayer score: {0}\nDealer score: {1}\n \nDealer Push".format(playerScore,dealerScore))
            userMoney += (bet *2)

    elif split == True:
        userMoney -= bet
        if playerScore > dealerScore:
            if dealerScore == -1:
                print("\n\n\nDealer has bust Player wins {0}".format((bet *2)))
            print("\n\n\nPlayer score: {0}\nDealer score: {1}\n \nPlayer Wins {2}".format(playerScore,dealerScore,(bet *2)))
            userMoney += (bet *2)
        elif playerScore < dealerScore:
            if playerScore == -1:
                print("\n\n\nDealer has bust Player loses {0}".format((bet)))
            print("\n\n\nPlayer score: {0}\nDealer score: {1}\n \nPlayer looses {2}".format(playerScore,dealerScore,(bet)))
        elif playerScore == dealerScore:
            print("\n\n\nPlayer score: {0}\nDealer score: {1}\n \nDealer Push".format(playerScore,dealerScore))
            userMoney += (bet)
        if splitScore > dealerScore:
            if dealerScore == -1:
                print("\n\n\nDealer has bust Player wins {0}".format((bet *2)))
            print("\n\n\nPlayer split hand score: {0}\nDealer score: {1}\n \nPlayer Wins {2}".format(playerScore,dealerScore,(bet *2)))
            userMoney += (bet *2)
        elif splitScore < dealerScore:
            if playerScore == -1:
                print("\n\n\nDealer has bust Player loses {0}".format((bet)))
            print("\n\n\nPlayer split hand score: {0}\nDealer score: {1}\n \nPlayer looses {2}".format(playerScore,dealerScore,(bet)))
        elif splitScore == dealerScore:
            print("\n\n\nPlayer split hand score: {0}\nDealer score: {1}\n \nDealer Push".format(playerScore,dealerScore))
            userMoney += (bet)
    elif (split != True) and (playerDoubleDown != True):
        if playerScore > dealerScore:
            if dealerScore == -1:
                print("\n\n\nDealer has bust Player wins {0}".format((bet *2)))
            print("\n\n\nPlayer score: {0}\nDealer score: {1}\n \nPlayer Wins {2}".format(playerScore,dealerScore,(bet *2)))
            userMoney += (bet *2)
        elif playerScore < dealerScore:
            if playerScore == -1:
                print("\n\n\nDealer has bust Player loses {0}".format((bet)))
            print("\n\n\nPlayer score: {0}\nDealer score: {1}\n \nPlayer looses {2}".format(playerScore,dealerScore,(bet)))
        elif playerScore == dealerScore:
            print("\n\n\nPlayer score: {0}\nDealer score: {1}\n \nDealer Push".format(playerScore,dealerScore))
            userMoney += (bet)   
    
    return


def lowBetting():
    global userMoney


    while True:
        bet = placeBet(1,5,10,50,100)
        game(bet)
        saveGameStat(name, userMoney)
        print("\nYour balance is {0}$ \n".format(userMoney))
        if userMoney == 0:
            userMoney = 100
            print("\n\nyour in Luck here 100$ on the house!\n")
        print("\nPlay again Y or N")
        choice = getchar("Y" , "N")
        if  choice == "N":
            print("\n1) Start Game  \n2) Quit ")
            choice = getIntInput(2)
            menu(choice)


def highBetting():
    global userMoney
    while True:
        bet = placeBet(250,500,1000,5000,10000)
        game(bet)
        saveGameStat(name, userMoney)
        print("Your balance is {0}$ \n".format(userMoney))
        if userMoney < 250:
            lowBetting()
        print("Play again Y or N")
        choice = getchar("Y" , "N")
        if  choice == "N":
            print("1) Start Game  \n2) Quit ")
            choice = getIntInput(2)
            menu(choice)

main()