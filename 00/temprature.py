def main():
    # Prompt the user for temperature in Fahrenheit
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))

    # Convert to Celsius
    celsius = (fahrenheit - 32) * 5.0 / 9.0

    # Display the result
    print(f"Temperature: {fahrenheit}F = {celsius}C")

# Run the program
if __name__ == "__main__":
    main()
