def main():
    # Ask the user for their age
    age = int(input("What is your age? "))

    # Check voting eligibility in each fictional country
    if age >= 16:
        print("You can vote in Peturksbouipo.")
    else:
        print("You cannot vote in Peturksbouipo.")

    if age >= 25:
        print("You can vote in Stanlau.")
    else:
        print("You cannot vote in Stanlau.")

    if age >= 48:
        print("You can vote in Mayengua.")
    else:
        print("You cannot vote in Mayengua.")

if __name__ == "__main__":
    main()
