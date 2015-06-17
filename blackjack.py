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
    print('blackjack!\nyour hand is ' + printHand())

def printHand():
    handmessage = ""
    for i in hand:
        handmessage += i + " "
    # calculate sum here
    return handmessage + "(" + str(countHand()) + ")"

def countHand():
    handcount = 0
    for i in hand:
        handcount += suits[i]
    return handcount
# hit

# stand

# deal - refer to 10

if __name__ == "__main__":
    shuffledeck()
    deal()
    start()
