import random
import os
from art import logo

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """"Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "It's a draw."
    elif c_score == 21:
        return "The computer got a ⭐ blackjack ⭐. You lose."
    elif u_score == 21:
        return "You got a ⭐ blackjack ⭐. You win!"
    elif u_score > 21:
        return "You went over 21. You lose."
    elif c_score > 21:
        return "The computer went over 21. You win!"
    elif u_score > c_score:
        return "Your score is higher than the computer. You win!"
    else:
        return "The computer has a higher score. You lose."

def play_game():
    # Initial setup
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # While loop for gameplay
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # The computer gets to draw cards to its  limit.
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print("------------------------------------------------------------------------------------")
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"The computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))
    print("------------------------------------------------------------------------------------")


while input("Do you want to play a game of blackjack? Type 'y' for yes or 'n' for no: ") == "y":
    os.system('clear')
    play_game()
