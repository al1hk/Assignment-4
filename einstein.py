def main():
    # Define the speed of light constant in meters per second
    C = 299792458  # meters per second (m/s)
    
    while True:
        # Prompt the user to enter mass in kilograms
        mass = float(input("Enter kilos of mass: "))
        
        # Calculate the energy using the formula E = m * C^2
        energy = mass * C**2
        
        # Output the results
        print("\ne = m * C^2...\n")
        print(f"m = {mass} kg")
        print(f"C = {C} m/s")
        print(f"{energy} joules of energy!\n")
        
        # Optionally, break or continue based on user input (for demo purposes we break here)
        # Uncomment the following line to keep asking the user for input
        # if input("Do you want to calculate again? (yes/no): ").lower() != "yes":
        #     break

# This provided line is required at the end of the Python file to call the main() function.
if __name__ == "__main__":
    main()
