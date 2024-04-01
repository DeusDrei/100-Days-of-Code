import random
import hang_words
import hang_art

lives = 6
main_word = random.choice(hang_words.word_list)

print(hang_art.logo)
used = []
display = []
for i in range(len(main_word)):
  display += "_"

while True:
  guess = input("Enter a letter: ").lower()

  if guess in used or guess in display:
    print(f"{guess} is already guessed.")

  for i in range(len(main_word)):
    x = main_word[i]
    if guess == x:
      display[i] = x

  if guess not in main_word and guess not in used:
    lives -= 1

  used.append(guess)
  print(" ".join(display))
  print(hang_art.stages[lives])

  if "_" not in display:
    print("You Win!")
    break

  elif lives == 0:
    print("You Lose!")
    print(f"The word was {main_word}")
    break
