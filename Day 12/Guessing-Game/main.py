logo = """
  ________                            .__                   ________                       
 /  _____/ __ __   ____   ______ _____|__| ____    ____    /  _____/_____    _____   ____  
/   \  ___|  |  \_/ __ \ /  ___//  ___/  |/    \  / ___\  /   \  ___\__  \  /     \_/ __ \ 
\    \_\  \  |  /\  ___/ \___ \ \___ \|  |   |  \/ /_/  > \    \_\  \/ __ \|  Y Y  \  ___/ 
 \______  /____/  \___  >____  >____  >__|___|  /\___  /   \______  (____  /__|_|  /\___  >
        \/            \/     \/     \/        \//_____/           \/     \/      \/     \/ 
"""

import random

lives = 0
random_number = random.randint(1, 100)


def compare(guess):
    if guess > random_number:
        print("Too high")
        return lives - 1
    elif guess < random_number:
        print("Too low")
        return lives - 1


print(logo)
print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
diff = input("Choose a difficulty. ('easy' or 'hard') ").lower()
while diff not in ("easy", "hard"):
    diff = input("Choose a difficulty. ('easy' or 'hard') ").lower()
if diff == "easy":
    lives = 10
else:
    lives = 5

while True:
    print(f"You have {lives} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    lives = compare(guess)
    if guess == random_number:
        print("You Win!")
        break
    elif lives == 0:
        print(f"You Lose, the number was {random_number}")
        break
