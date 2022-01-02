
import random

from hangman_words import word_list


logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']



attempts = 6

chosen_word = random.choice(word_list)

word_len = len(chosen_word)

display = list("_" * word_len)

print(f"{chosen_word} {word_len}")

attempts_cnt = 6
print(stages[6])

while attempts_cnt > 0:

    guess = input("Guess a letter ").lower()

    found = False

    for i in range(word_len):
        if chosen_word[i] == guess:
            display[i] = guess
            found = True

    if found:
        print(display)
    else:
        attempts_cnt -= 1
        print(stages[attempts_cnt])
        print(f"Bad guess: {attempts_cnt} tries left")
        if attempts_cnt == 0:
            print("You lose")
            break

        #if display.count("_") == 0:
    if "_" not in display:

        print("You win")
        break





