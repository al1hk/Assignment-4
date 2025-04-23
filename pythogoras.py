import math

def main():
    # Prompt the user for the lengths of the two perpendicular sides
    AB = float(input("Enter the length of AB: "))
    AC = float(input("Enter the length of AC: "))
    
    # Calculate the length of the hypotenuse (BC) using the Pythagorean theorem
    BC = math.sqrt(AB**2 + AC**2)
    
    # Output the result
    print(f"The length of BC (the hypotenuse) is: {BC}")

# This provided line is required at the end of the Python file to call the main() function.
if __name__ == "__main__":
    main()
