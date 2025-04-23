import random

def hangman():
    print("🎉 Welcome to Hangman!\n")

    # Word list (you can expand this)
    word_list = ["python", "hangman", "coding", "computer", "keyboard", "laptop"]
    word = random.choice(word_list)
    word_letters = set(word)
    guessed_letters = set()
    attempts = 6

    print(f"I'm thinking of a word. It has {len(word)} letters.")

    while attempts > 0 and word_letters:
        print("\nWord: ", " ".join([letter if letter in guessed_letters else "_" for letter in word]))
        print(f"Guessed letters: {' '.join(sorted(guessed_letters))}")
        print(f"❤️ Attempts left: {attempts}")

        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("❌ Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("⚠️ You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word_letters:
            word_letters.remove(guess)
            print("✅ Good guess!")
        else:
            attempts -= 1
            print("❌ Nope, that letter’s not in the word.")

    if not word_letters:
        print(f"\n🎉 Congrats! You guessed the word: {word}")
    else:
        print(f"\n💀 Game Over! The word was: {word}")

# Start the game
hangman()
