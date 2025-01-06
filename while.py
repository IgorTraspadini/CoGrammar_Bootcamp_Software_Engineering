# Created by IgorCT - Dez_2024

# Variables to store user input and a list of numbers
user_input = 0
number_list = []

# While loop to continuously ask for user input until -1 is entered
while user_input != -1:
    # Ask the user to enter a number different from zero (-1 to exit)
    user_input = int(input("Enter a number different from zero (-1 to exit): "))

    # Check if the user input is not zero and not -1
    if user_input != 0 and user_input != -1:
        # Append the user input to the list of numbers
        number_list.append(user_input)

# Calculate and print the average of the numbers in the list
print(f"Numbers average: {sum(number_list)/len(number_list)}")
