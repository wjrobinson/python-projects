from data import data
from art import logo, vs
import random
import os

def format_data(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}."

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
            
# display art
print(logo)
score = 0
should_continue = True
account_b = random.choice(data)

# make the game repeatable
while should_continue:
    # generate a random account from the game data
    # making account at position B become the next account at position A
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    # format the account data into printable format.
    print(f"Account A: {format_data(account_a)}")
    print(vs)
    print(f"Account B: {format_data(account_b)}")

    # ask user for a guess
    guess = input("Who has more followers? Type 'a' or 'b': ").lower()

    # check if user is correct.
    # get follower count of each account
    # use if statement to check if user is correct
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # clear the screen between rounds
    os.system('clear')
    print(logo)
    # give user feedback on their guess
    # score keeping
    if is_correct:
        score += 1
        print(f"That's right! Current score: {score}")
    else:
        print(f"Sorry, that's not right. Final score: {score}")
        should_continue = False
