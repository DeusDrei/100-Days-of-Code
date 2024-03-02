import art
from game_data import data
import random
from replit import clear


def compare(ask, followers):
  global end_game, score
  if ask == 'a':
    if followers[0] > followers[1]:
      clear()
      score += 1
    elif followers[0] == followers[1]:
      clear()
      score += 1
    elif followers[0] < followers[1]:
      clear()
      end_game = True
      print(art.logo)
      print("You Lose.")
      print(f"Final score: {score}")
  elif ask == 'b':
    if followers[0] > followers[1]:
      clear()
      end_game = True
      print(art.logo)
      print("You Lose.")
      print(f"Final score: {score}")
    elif followers[0] == followers[1]:
      clear()
      score += 1
    elif followers[0] < followers[1]:
      clear()
      score += 1


def pick():
  x = random.choice(data)
  name = x["name"]
  desc = x["description"]
  country = x["country"]
  followers.append(x["follower_count"])
  return f"{name}, A {desc}, from {country}."


score = 0
end_game = False
followers = []
x = pick()
y = pick()

while not end_game:
  print(art.logo)
  print(f"Score: {score}")
  print(f"Compare A: {x}")
  print(art.vs)
  print(f"Compare B: {y}")
  ask = input("Who has more followers? Type 'A' or 'B': ").lower()
  while ask not in ("a", "b"):
    ask = input("Who has more followers? Type 'A' or 'B': ").lower()
  compare(ask, followers)
  x = y
  del (followers[0])
  y = pick()

