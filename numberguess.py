import random








#================ Main ===================

num = random.randint(1,100)
print(num)

level = input("easy or hard").lower()

if level == "easy":
    guess_cnt = 10
else:
    guess_cnt = 5

while guess_cnt > 0:
    guess = int(input("Guess: "))
    guess_cnt -= 1
    if guess > num:
        print(f"Too High\nGuess again\nYou have {guess_cnt} attempts remaining to guess right answer")
    elif guess < num:
        print(f"Too low\nGuess again\nYou have {guess_cnt} attempts remaining to guess right answer")
    else:
        guess_cnt = 0
        print("You guessed correctly")


