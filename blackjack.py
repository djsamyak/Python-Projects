from random import *
from math import *

used_cards=['']
global suits
global ranks
global values

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}

def shuffle():
    global card_rank
    global card_suit
    card_suit=suits[randint(0,3)]
    card_rank=ranks[randint(0,12)]

def get_card():
    if(f"{card_suit},{card_rank}" in used_cards):
        shuffle()
        get_card();
    else:
        print(f"The card is {card_rank} of {card_suit}")
        used_cards.append(f"{card_suit},{card_rank}")

player_choice='y'

class Player():
    sum=0
    deck=['']

computer=Player()
human=Player()

while (player_choice=='y'):
    shuffle()
    get_card()
    human.deck.append(f"{card_suit},{card_rank}")
    if(card_rank=='Ace'):
        ace_choice=input("Press '0' for Ace as 1,'1' for Ace as 11 \n")
        if(ace_choice==0):
            human.sum=human.sum + 1
        elif(ace_choice==1):
            human.sum=human.sum + 11
    else:
        human.sum=human.sum + values[card_rank]

    shuffle()
    get_card()
    computer.deck.append(f"{card_suit},{card_rank}")
    if(card_rank=='Ace'):
        ace_choice=randint(0,1)
        if(ace_choice==0):
            computer.sum=computer.sum + 1
        elif(ace_choice==1):
            computer.sum=computer.sum + 11
    else:
        computer.sum=computer.sum + values[card_rank]

    print("Do you want to play another round? (y/n) \n")
    player_choice=input()

print(f"Total sum of the dealer is: {computer.sum} \n")
print(f"Total sum of the player is: {human.sum} \n")

if(abs(human.sum - 21) < abs(computer.sum - 21)):
    print("YAY! You win!\n")
elif(abs(human.sum - 21) > abs(computer.sum - 21)):
    print("OOPSIE! You have lost :( \n")
elif((abs(human.sum - 21) == abs(computer.sum - 21))):
    print("Its a TIE \n")

yolo=input("Press ENTER to exit.")
