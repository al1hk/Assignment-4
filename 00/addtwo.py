def main():
    print("Welcome to the Sum Calculator!")

    # Prompt user for the first number
    first_number = int(input("Enter the first number: "))

    # Prompt user for the second number
    second_number = int(input("Enter the second number: "))

    # Calculate the sum
    total_sum = first_number + second_number

    # Display the result
    print(f"The sum of {first_number} and {second_number} is: {total_sum}")

# Call the main function
if __name__ == "__main__":
    main()
