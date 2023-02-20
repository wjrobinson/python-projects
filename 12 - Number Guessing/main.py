import random
from art import logo

# Global variables for difficulty levels.
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
    """Compares player guess to user answer. Returns number of turns remaining."""
    if guess == answer:
        print(f"You guessed the number {answer} correctly. You win!")
    elif guess > answer:
       print("Your guess is too high, try again.")
       return turns - 1
    else:
        print("Your guess is too low, try again.")
        return turns - 1

def set_difficulty():
    difficulty = input("Please choose difficulty level. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        return EASY_LEVEL_TURNS
    elif difficulty == "hard":
        return HARD_LEVEL_TURNS

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1,101)

    turns = set_difficulty()

    # Declaring guess so it can be used in while loop, guess is replaced by user guess immediately.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        # Sets the local variable turns to the return of check answer function.
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses. You lose.")
            return

game()
