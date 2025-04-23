import random

def guess_the_number():
    print("🎮 Welcome to 'Guess the Number' Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?\n")

    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("🔻 Too low! Try again.\n")
            elif guess > number_to_guess:
                print("🔺 Too high! Try again.\n")
            else:
                print(f"✅ Congratulations! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("❌ Invalid input. Please enter a number.\n")

# Start the game
guess_the_number()
