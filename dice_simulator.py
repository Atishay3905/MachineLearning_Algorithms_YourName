# Dice Rolling Simulator 🎲

import random

print("Welcome to the Dice Simulator!")

while True:
    roll = input("Press Enter to roll the dice or type 'quit' to exit: ")

    if roll.lower() == "quit":
        print("Goodbye!")
        break

    dice = random.randint(1, 6)
    print("🎲 You rolled a", dice)
