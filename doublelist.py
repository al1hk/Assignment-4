def double_numbers():
    # Prompt the user to enter numbers and store them in a list
    numbers = []
    while True:
        user_input = input("Enter a number (or type 'done' to finish): ")
        
        if user_input.lower() == 'done':
            break
        
        try:
            # Convert input to a number and add it to the list
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Please enter a valid number or type 'done' to finish.")
    
    # Double each number in the list
    doubled_numbers = [num * 2 for num in numbers]
    
    # Print the doubled numbers
    print("The doubled numbers are:", doubled_numbers)

# Call the function to run the program
double_numbers()
