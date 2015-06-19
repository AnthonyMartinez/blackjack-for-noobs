# first iteration of blackjack game - character based
from random import shuffle



# create the deck
suits = {
        'A': 11,
        'K': 10,
        'Q': 10,
        'J': 10,
        '10': 10,
        '9': 9,
        '8': 8,
        '7': 7,
        '6': 6,
        '5': 5,
        '4': 4,
        '3': 3,
        '2': 2
        }

deck = [i for _ in range(4) for i in suits.keys()]
hand = []
dealer = []

# shuffle the deck
def shuffledeck():
    shuffle(deck)


# create the players hand
    # deal cards
def deal():
    for _ in range(2):
        hand.append(deck.pop())
        dealer.append(deck.pop())



# message module
    # hit, stand, deal
def start():
    print('blackjack!\n')
    shuffledeck()
    deal()
    printDealer()
    printHand()
    menu()

def printHand():
    handmessage = ""
    for i in hand:
        handmessage += i + " "
    # calculate sum here
    print('your hand is ' + handmessage + "(" + str(countHand(hand)) + ")")

def printDealer():
    handmessage = dealer[-1]
    # calculate sum here
    print('dealer shows ' + handmessage)

    

def countHand(cards):
    handcount = 0
    for i in cards:
        handcount += suits[i]
    return handcount

def menu():
    choice = 1
    while choice:
        print('[h]it, [s]tand, or [d]eal?')
        choice = raw_input()
        if choice[0].lower() == 'h':
            pass
            #hit()
        elif choice[0].lower() == 's':
            pass
            #stand()
        elif choice[0].lower() == 'd':
            pass
            #start()
        else:
            print('invalid')
# hit
def hit():
    # add a card to hand
    # check for bust
        #if busted, 
    # check for blackjack
    # return to menu
    pass

# stand
def stand():
    # start the dealer's deal
    pass

def bust_check():
    #if countHand(cards) < 22
    #return False
    #else return True
    pass


# deal - refer to 10

if __name__ == "__main__":
    start()
