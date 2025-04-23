def get_last_element(lst):
    # Print the last element in the list
    print(lst[-1])

def main():
    # Ask the user how many elements they want to input
    n = int(input("How many elements do you want to enter in the list? "))
    
    # Initialize an empty list
    user_list = []
    
    # Prompt the user to input the elements one at a time
    for i in range(n):
        element = input(f"Enter element {i + 1}: ")
        user_list.append(element)
    
    # Call the function to print the last element in the list
    get_last_element(user_list)

if __name__ == "__main__":
    main()
