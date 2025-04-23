def sum_of_numbers():
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
    
    # Calculate and return the sum of the numbers
    total_sum = sum(numbers)
    print("The sum of the numbers is:", total_sum)

# Call the function to run the program
sum_of_numbers()
