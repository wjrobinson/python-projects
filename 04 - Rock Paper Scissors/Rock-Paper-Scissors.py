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

game_images = [rock, paper, scissors]
game_choices = ["rock", "paper", "scissors"]
game_continue = True

#RPS being decided
while game_continue:
    player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors "))
    if player_choice >= 3 or player_choice < 0:
        print("You typed an invalid number, try again.")
    else:
        print(f"You chose {game_choices[player_choice]}")
        print(game_images[player_choice])

        computer_choice = random.randint(0,2)
        print(f"Computer chose {game_choices[computer_choice]}")
        print(game_images[computer_choice])

        #The logic of RPS
        if player_choice == 0 and computer_choice == 2:
            print("You win!")
            should_continue = input("Want to play again? Type 'yes' or 'no'")
            if should_continue == "no":
                game_continue = False
        elif computer_choice == 2 and player_choice == 0:
            print("You lose.")
            should_continue = input("Want to play again? Type 'yes' or 'no'")
            if should_continue == "no":
                game_continue = False
        elif computer_choice > player_choice:
            print("You lose.")
            should_continue = input("Want to play again? Type 'yes' or 'no'")
            if should_continue == "no":
                game_continue = False
        elif player_choice > computer_choice:
            print("You win!")
            should_continue = input("Want to play again? Type 'yes' or 'no'")
            if should_continue == "no":
                game_continue = False
        elif player_choice == computer_choice:
            print("It's a draw, try again.")
