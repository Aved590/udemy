
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


def calculate_score(cards):
    # Hint
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    #Hint
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


#=======================================================
#================       Main       =====================
#=======================================================

dealer_bust = False
player_bust = False

game_over = False

player_hand = []
dealer_hand = []

for _ in range(2):
    draw_card(player_hand)
    draw_card(dealer_hand)

player_hand = [11, 11]
print(player_hand)
#print(player_hand, dealer_hand[0])
print(calculate_score(player_hand))
#print(calculate_score(dealer_hand))

player_hand.append(1)
print(player_hand)
print(calculate_score(player_hand))
print(player_hand)
player_hand.append(10)
print(calculate_score(player_hand))
print(player_hand)
player_score = calculate_score(player_hand)
dealer_score = calculate_score(dealer_hand)



if player_score == 0 or dealer_score == 0 or player_score > 21:
    print("End Game")
    game_over = True



quit()

#player_score = calculate_score(player_hand)
#dealer_score = calculate_score(dealer_hand)



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
