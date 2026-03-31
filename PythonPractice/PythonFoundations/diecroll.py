# Simulate rolling a dice using random number generation. Allow the user to roll the dice multiple times and display the result each time.

import random

def dice_roll():
    print("Welcome to the dice roller!")
    while True:
        input("Press Enter to roll the dice...")
        result = random.randint(1, 6)
        print(f"You rolled a {result}!")
        play_again = input("Do you want to roll again? (yes/no): ")
        if play_again.lower() != 'yes':
            print("Thanks for playing! Goodbye!")
            break

dice_roll()