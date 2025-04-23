import random

def guess_my_number():
    number_to_guess = random.randint(0, 99)
    print("I am thinking of a number between 0 and 99...")

    while True:
        try:
            guess = int(input("Enter a guess: "))
            if guess > number_to_guess:
                print("Your guess is too high\n")
            elif guess < number_to_guess:
                print("Your guess is too low\n")
            else:
                print(f"Congrats! The number was: {number_to_guess}")
                break
        except ValueError:
            print("Please enter a valid number.\n")

# Run the game
guess_my_number()
