# Dictionary to store counts
count_dict = {}

# Input loop
while True:
    user_input = input("Enter a number (or press Enter to finish): ")
    if user_input == "":
        break  # Stop input on empty string
    number = int(user_input)
    
    # Count the occurrences
    if number in count_dict:
        count_dict[number] += 1
    else:
        count_dict[number] = 1

# Display the results
for number, count in count_dict.items():
    print(f"{number} appears {count} times.")
