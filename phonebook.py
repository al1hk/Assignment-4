# Create an empty phonebook dictionary
phonebook = {}

# Input loop to add contacts
while True:
    name = input("Enter a name (or press Enter to stop): ")
    if name == "":
        break
    number = input(f"Enter phone number for {name}: ")
    phonebook[name] = number

# Print the phonebook
print("\nPhonebook:")
for name, number in phonebook.items():
    print(f"{name}: {number}")
