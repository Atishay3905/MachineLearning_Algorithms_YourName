# Rock Paper Scissors Game ✊✋✌️

import random

print("Welcome to Rock-Paper-Scissors!")

choices = ["rock", "paper", "scissors"]

while True:
    user = input("Choose rock, paper, or scissors (or type 'quit' to exit): ").lower()

    if user == "quit":
        print("Thanks for playing!")
        break

    if user not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue

    computer = random.choice(choices)
    print(f"Computer chose: {computer}")

    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You win!")
    else:
        print("You lose!")
