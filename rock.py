import random

def rock_paper_scissors():
    print("🎮 Welcome to Rock, Paper, Scissors!")
    options = ["rock", "paper", "scissors"]

    while True:
        # Player input
        user_choice = input("Choose rock, paper, or scissors (or 'quit' to exit): ").lower()

        if user_choice == "quit":
            print("👋 Thanks for playing!")
            break

        if user_choice not in options:
            print("❌ Invalid choice. Please try again.\n")
            continue

        # Computer's random choice
        computer_choice = random.choice(options)
        print(f"💻 Computer chose: {computer_choice}")

        # Decide the winner
        if user_choice == computer_choice:
            print("🤝 It's a tie!\n")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("✅ You win!\n")
        else:
            print("❌ You lose!\n")

# Start the game
rock_paper_scissors()
