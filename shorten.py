MAX_LENGTH = 3  # Define the maximum length of the list

def shorten(lst):
    # Check if the list is already shorter than MAX_LENGTH
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()  # Remove the last item
        print(removed_item)  # Print the removed item

def main():
    # Ask the user to input the list elements one by one
    user_list = []
    while True:
        user_input = input("Enter a value (or press enter to finish): ")
        if user_input == "":  # If the user presses Enter without typing anything, stop.
            break
        user_list.append(user_input)  # Add the input to the list

    print("Before shortening:", user_list)
    shorten(user_list)  # Shorten the list
    print("After shortening:", user_list)

if __name__ == "__main__":
    main()
