

from pickle import TRUE
from secrets import choice


deck = ["D1","D2","D3","D4","D5","D6","D7","D8","D9","D10","DJ","DQ","DK","DA","C1","C2","C3","C4","C5","C6","C7","C8","C9","C10","CJ","CQ","CK","CA","H1","H2","H3","H4","H5","H6","H7","H8","H9","H10","HJ","HQ","HK","HA","S1","S2","S3","S4","S5","S6","S7","S8","S9","S10","SJ","SQ","SK","SA"]
# possible a better way to make the deck in case of simplicity i just used the above method 
#deck = [i + j for i in ['D', 'C', 'H', 'S'] for j in ['1', '2', '3' 'J', 'Q', 'K']]
stand = 17
blackJack = 21
gameLoaded = False

userMoney= 0

name = ""

def main():

    if gameLoaded == False:
        userMoney,name=loadGameState()
        gameLoaded = True

    if name == "":
        print("Welcome To Black Jack\n")
        Name = input("Please type in your name:")
    else:
        print("wWlcome Back {0}!\n Your Current balance is {1}$".format(name,str(userMoney)))
    
    print("1) Start Game  \n2) Quit ")
    choice = getIntInput(2)
    if choice == 2:
        choice = 3
    menu(choice)


    

# this Tries loads the players state if the file doesn't exest when it trys to load it the exception will create the file and return a balance of 100$ and a black name
def loadGameState():
    try:
        file = open("save.txt", "r")
        l = file.readline()
        file.close()
        return l[0],l[1]

    except:
        file = open("save.txt", "x")
        file.close()
        return 100 , ""

def saveGameStat(name, userMoney):
    lines = [name,userMoney]
    file = open("save.txt", "r")
    file.write('\n'.join(lines))
    file.close


def getIntInput(number):
    while True:
        try:
            integer = int(input("Please input your choice: "))
        except ValueError:
            print("Please, enter a input")
            continue
        
        if integer > number or integer <= 0:
            print("Please, enter a input")
        
        else:
            return integer
            break 
            

def menu(case):
    match case:
        case 1:
            print("1) Normal Bets (1,5,10,50,100)\n 2) HighRoller (1000,2500,5000,10000)")
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
            print("Your Current balance is {0}$", userMoney)
        case 3:
            saveGameStat(name, userMoney)
            quit()

def lowBetting():
    pass

def highBetting():
    pass
