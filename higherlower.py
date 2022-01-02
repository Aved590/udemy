from game_data import data

import random

import os


os.system('clear')

def get_random_account:
    '''Get data from random account'''
    return random.choice(data)

def format_data(account)
    '''Format account into printable format: name, desc, country'''
    return f"{sel_1['name']}, a {sel_1['description']}, from {sel_1['country']}"


def check_answer(guess, followers_1, followers_2):
    if followers_1 > followers_2:
        return guess == "A"
    elif followers_1 < followers_2:
        return guess == "B"


#Find number of dictionary entries in data


def game()
    win_cnt = 0
    game_over = False
    sel_1 = get_random_account()
    sel_2 = get_random_account()

    while not game_over:

        #select 2 random dictionary elements, if same, select until not same
        #print(data)
        #print(random.choice([data.keys()]))
        sel_1 = random.sample(data,1)[0]
        sel_2 = random.sample(data,1)[0]
        while sel_1["name"] == sel_2["name"]:
            sel_2 = random.sample(data, 1)[0]

        print(sel_1["name"])

        # display each, labeled A and B
        print(f"Compare\n A: {sel_1['name']}, a {sel_1['description']}, from {sel_1['country']}\nvs.\n B: {sel_2['name']}, a {sel_2['description']}, from {sel_2['country']}")
        followers_1 = sel_1["follower_count"]
        followers_2 = sel_2["follower_count"]
        print(f"Fol1: {followers_1}, Fol2 {followers_2}")
        if followers_1 > followers_2:
            answer = "A"
        elif followers_1 < followers_2:
            answer = "B"

        choice = input("Who has more followers?  Type 'A' or 'B': ").upper()

        os.system('clear')


        if choice == answer:
            win_cnt += 1
            print(f"You're right! Current score: {win_cnt}")
        else:
            print(f"Sorry, that's wrong.  Final score: {win_cnt}")
            game_over = True






