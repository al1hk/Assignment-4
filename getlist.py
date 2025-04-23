def main():
    user_list = []  # Initialize an empty list

    while True:
        # Prompt the user for a value
        value = input("Enter a value: " + "if you want to end the program just press enter without writing anything")

        # Check if the user pressed enter without typing anything
        if value == "":
            break  # Exit the loop if the user didn't type anything

        # Add the entered value to the list
        user_list.append(value)

    # Print the list after the user presses enter without typing anything
    print("Here's the list:", user_list)

if __name__ == "__main__":
    main()
