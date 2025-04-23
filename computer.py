def computer_guesses():
    print("🧠 Think of a number between 1 and 100, and I'll try to guess it!")
    print("Tell me if my guess is too high (H), too low (L), or correct (C).\n")

    low = 1
    high = 100
    attempts = 0

    while low <= high:
        guess = (low + high) // 2
        attempts += 1

        print(f"My guess is: {guess}")
        feedback = input("Is it too High (H), too Low (L), or Correct (C)? ").lower()

        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
        elif feedback == "c":
            print(f"\n🎉 Yay! I guessed your number in {attempts} tries!")
            break
        else:
            print("⚠️ Invalid input. Please enter H, L, or C.\n")

# Start the game
computer_guesses()
