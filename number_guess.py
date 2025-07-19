# Number Guessing Game 🎯

import random  # To generate a random number

print("Welcome to the Number Guessing Game!")

# Generate a random number between 1 and 100
number_to_guess = random.randint(1, 100)

# Set the number of tries
max_tries = 7
tries = 0

# Loop for guessing
while tries < max_tries:
    guess = int(input(f"Attempt {tries + 1} of {max_tries}: Guess a number (1 to 100): "))
    tries += 1

    if guess == number_to_guess:
        print("🎉 Correct! You guessed the number!")
        break
    elif guess < number_to_guess:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

if guess != number_to_guess:
    print(f"😢 You're out of tries. The number was {number_to_guess}.")
