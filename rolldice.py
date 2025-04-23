import random

def roll_dice():
    # Simulate rolling two dice
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    
    # Print the results of each roll and the total
    print(f"Dice 1: {die1}, Dice 2: {die2}, Total: {die1 + die2}")

def main():
    # Call the roll_dice function to simulate rolling the dice
    roll_dice()

# This provided line is required at the end of the Python file to call the main() function.
if __name__ == "__main__":
    main()
