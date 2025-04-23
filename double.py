# Ask the user for a number
number = float(input("Enter a number: "))

# Double the number until it's 100 or greater
while number < 100:
    number *= 2
    print(f"The number is now: {number}")

print("The number has reached 100 or greater!")
