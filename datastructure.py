def add_three_copies(my_list, data):
    # Add three copies of data to the list
    my_list.append(data)
    my_list.append(data)
    my_list.append(data)

def main():
    # Ask the user for some data to copy
    user_input = input("Enter a message to copy: ")

    # Create an empty list
    my_list = []

    # Print the list before modification
    print("List before:", my_list)

    # Call the add_three_copies function to modify the list
    add_three_copies(my_list, user_input)

    # Print the list after modification
    print("List after:", my_list)

if __name__ == "__main__":
    main()
