from logos import auction_logo

#from replit import clear
#HINT: You can call clear() to clear the output in the console.
import os

import os
cls = lambda: os.system('cls')

# now, to clear the screen
def find_high_bidder(dict1):
    high = -1
    winner = ""
    for key in dict1:
        if dict1[key] > high:
            high = dict1[key]
            winner = key

    print(f"{winner} is the winner with high bid of {high}")


print(auction_logo)
print("Welcome to the secret auction program")

bid_dict = {}

finished = False
while not finished:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))
    bid_dict[name] = bid
    print(bid_dict)
    more = input("Are there other bidders? Type 'yes or 'no'. ").lower()
    if more == "no":
        finished = True

find_high_bidder(bid_dict)






