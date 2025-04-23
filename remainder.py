def main():
    # Ask the user for two numbers
    dividend = int(input("Please enter an integer to be divided: "))
    divisor = int(input("Please enter an integer to divide by: "))
    
    # Perform division and calculate remainder
    quotient = dividend // divisor
    remainder = dividend % divisor
    
    # Output the result
    print(f"The result of this division is {quotient} with a remainder of {remainder}")

# This provided line is required at the end of the Python file to call the main() function.
if __name__ == "__main__":
    main()
