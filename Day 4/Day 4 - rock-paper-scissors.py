import random
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
while True:
  choices = [0, 1 ,2]
  computer = random.choice(choices)
  ask = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. "))
  if ask == 0:
    if computer == 0:
        print(rock)
        print("Computer chose:")
        print(rock)
        print("It's a tie")
    elif computer == 1:
        print(rock)
        print("Computer chose:")
        print(paper)
        print("You lose")
    elif computer == 2:
        print(rock)
        print("Computer chose:")
        print(scissors)
        print("You Win!")
  elif ask == 1:
    if computer == 0:
        print(paper)
        print("Computer chose:")
        print(rock)
        print("You Win!")
    elif computer == 1:
        print(paper)
        print("Computer chose:")
        print(paper)
        print("It's a tie")
    elif computer == 2:
        print(paper)
        print("Computer chose:")
        print(scissors)
        print("You lose")
  elif ask == 2:
    if computer == 0:
        print(scissors)
        print("Computer chose:")
        print(rock)
        print("You lose")
    elif computer == 1:
        print(scissors)
        print("Computer chose:")
        print(paper)
        print("You Win!")
    elif computer == 2:
        print(scissors)
        print("Computer chose:")
        print(scissors)
        print("It's a tie")
  else:
    print("Invalid Input. Rerun the code.")
    
  redo = input("Play again? (Y/N) ").lower()
  if redo != "y":
    break
