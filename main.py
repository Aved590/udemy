rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

game_images[rock,paper,scissors]

my = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
cc = random.randint(0,2)

print(f"Computer: {cc}")
print(f"You: {my}")

print()

if cc == 0 and my == 2:
    print("You win")

elif cc > my:
    print("You lose")
elif my >
elif cc == 0 and my == 2
    print("You lose")

elif cc == my
    print("Draw")
elif my >= 4 or my
    print("You typed invalid number")

#
# if cc == 0 and my == 1
#     print(rock)
#     print(paper)
#     print("You Win!")
# elif cc == 0 and my == 2:
#     print(rock)
#     print(scissors)
#     print("You lose")
# elif cc == 0 and my == 0:
#     print(rock)
#     print(rock)
#     print("Draw")
# elif cc == 1 and my == 0:
#     print(paper)
#     print(rock)
#     print("You lose")
# elif cc == 1 and my == 1:
#     print(paper)
#     print(paper)
#     print("Draw")
# elif cc == 1 and my == 2
#     print(paper)
#     print(scissors)
#     print("You Win")
