# Mad Libs Generator 📚

print("Let's play Mad Libs!")

# Get words from the user
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")
place = input("Enter a place: ")

# Create a story using the inputs
story = f"\nOne day, a {adjective} {noun} decided to {verb} through the streets of {place}."

print("\nHere's your story:")
print(story)
