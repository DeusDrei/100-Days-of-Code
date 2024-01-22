import random
from replit import clear
from art import logo


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    give_card = random.choice(cards)
    return give_card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(player_score, computer_score):
    if player_score > 21 and computer_score > 21:
        return "You went over, You Lose!"
    elif player_score == computer_score:
        return "It's a draw"
    elif player_score == 0:
        return "You Win with a Blackjack!"
    elif computer_score == 0:
        return "You Lose, Dealer has Blackjack!"
    elif player_score > 21:
        return "You went over, You Lose!"
    elif computer_score > 21:
        return "Opponent went over, You Win!"
    elif player_score > computer_score:
        return "You Win!"
    else:
        return "You Lose!"


def blackjack():
    print(logo)
    player_card = []
    computer_card = []
    for i in range(2):
        player_card.append(deal_card())
        computer_card.append(deal_card())
    while True:
        player_score = calculate_score(player_card)
        computer_score = calculate_score(computer_card)
        print(f"Your cards: {player_card}, current score: {player_score}")
        print(f"Dealer's first card: {computer_card[0]}")
        if player_score == 0 or computer_score == 0 or player_score > 21:
            break
        else:
            hit = input(
                "Type 'y' to get another card, type 'n' to stand: ").lower()
            if hit == "y":
                player_card.append(deal_card())
            else:
                break
    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)
    print(f"Your final hand: {player_card}, Your final score: {player_score}")
    print(f"Dealer's final hand: {computer_card}, Dealer's final score: {computer_score}")
    print(compare(player_score, computer_score))

while True:
    ask = input("Do you want to play a game of Blackjack? (Y/N) ").lower()
    while ask not in ("y", "n"):
        ask = input("Do you want to play a game of Blackjack? (Y/N) ").lower()
    if ask == "y":
        clear()
        blackjack()
    else:
        print("Thank you for playing.")
        break
