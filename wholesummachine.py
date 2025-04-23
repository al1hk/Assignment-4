# Define the affirmation
affirmation = "I am capable of doing anything I put my mind to."

# Prompt the user to type the affirmation until they get it right
while True:
    user_input = input("Type this affirmation: 'I am capable of doing anything I put my mind to.'\n")
    
    if user_input == affirmation:
        print("Well done! You are capable of doing anything you put your mind to!")
        break
    else:
        print("Oops! That's not quite right. Try again.")
