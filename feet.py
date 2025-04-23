def main():
    # Ask the user to input the number of feet
    feet = float(input("Enter a number of feet: "))
    
    # Calculate the equivalent inches (1 foot = 12 inches)
    inches = feet * 12
    
    # Print the result
    print(f"{feet} feet is equal to {inches} inches.")

# This provided line is required at the end of the Python file to call the main() function.
if __name__ == "__main__":
    main()
