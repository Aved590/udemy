############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input
#and returns the score.
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

import random

import time


t = int( time.time() * 1000.0 )
random.seed( ((t & 0xff000000) >> 24) +
             ((t & 0x00ff0000) >>  8) +
             ((t & 0x0000ff00) <<  8) +
             ((t & 0x000000ff) << 24)   )

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#=======================================================
def draw_card(hand):
    '''Draw one random card and add to hand'''
    hand.append(random.choice(cards))
    return hand

#=======================================================
def add_cards(hand):
    '''Add all items in list'''
    if hand.count(11) == 2 and len(hand) == 2:
        hand[0] = 1
        return 12

    sum = 0

    for i in range(0, len(hand)):
        sum += hand[i]
    if sum < 22:
        return sum

    if 11 in hand:
        #ace = True
        print(hand)
        hand[hand.index(11)] = 1
        print(f"ace found and fixed {hand}")
        sum = 0
        for i in range(0, len(hand)):
            sum += hand[i]
        return sum
    else:
        return sum



#=======================================================
#================       Main       =====================
#=======================================================

dealer_bust = False
player_bust = False
player_hand = []
dealer_hand = []

for _ in range(2):
    draw_card(player_hand)
    draw_card(dealer_hand)

# draw_card(player_hand)
# draw_card(player_hand)
# draw_card(dealer_hand)
# draw_card(dealer_hand)
print(player_hand, dealer_hand)


# Player Activity

player_card_sum = add_cards(player_hand)

hit = input (f"Your cards are {player_hand} total of {player_card_sum}, (h)it or (s)tay? ").lower()

while hit == 'h' and not player_bust:
    draw_card(player_hand)
    print(f"Player Hand: {player_hand}")
    player_card_sum = add_cards(player_hand)
    if (player_card_sum > 21):
        print(f"{player_hand} Busted, you lose with {player_card_sum}")
        player_bust = True
    else:
        hit = input(f"Your cards are {player_hand} total of {player_card_sum}, (h)it or (s)tay? ").lower()


print(f"Player stands with {player_card_sum}")

# Dealer activity
dealer_card_sum = add_cards(dealer_hand)
while dealer_card_sum < 17:
    draw_card(dealer_hand)

    dealer_card_sum = add_cards(dealer_hand)
    #print(f"Dealer Hand: {dealer_hand}")
    if (dealer_card_sum > 21):
        dealer_bust = True


print(f"Finding winner: dealer busts: {dealer_bust},  {dealer_card_sum}, {dealer_hand}")
print(f"Finding winner: player busts: {player_bust}, {player_card_sum}, {player_hand}")

if dealer_bust and player_bust:
    print("Everybody loses")
elif (not dealer_bust and player_bust):
    print(f"Dealer wins with {dealer_card_sum}")
elif (dealer_bust and not player_bust):
    print(f"Player wins with {player_card_sum}")
elif  (dealer_card_sum < player_card_sum):
    print(f"Player wins with {player_card_sum}")
elif (dealer_card_sum > player_card_sum):
    print(f"Dealer wins with {dealer_card_sum}")
else:
    print(f"Draw")


#or (dealer_card_sum < player_card_sum)
#if (add_cards(dealer_hand)) == 21 and add_cards
#

# print(dealer_hand)
# print(add_cards(dealer_hand))
# dealer_hand.append(5)
#
# print(dealer_hand)
# print(add_cards(dealer_hand))
#
# player_hand = draw_cards(2)
#
# print(player_hand)
# #if add_cards(player_hand)
