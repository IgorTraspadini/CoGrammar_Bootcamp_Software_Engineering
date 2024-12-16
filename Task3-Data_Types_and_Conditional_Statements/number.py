# Created by IgorCT - Dez_2024

# user input
user_number = []
print("Please, enter three different intergers numbers.")
for i in range(3):
  user_number.append(int(input("Enter a intergers numbers: ")))

# Perform operations
print(f"Sum of the numbers: {sum(user_number)}")
print(f"First minus second number: {user_number[0] - user_number[1]}")
print(f"Third number multiplied by the first number: {user_number[2] * user_number[0]}")
print(f"The sum of all three numbers dividide by the third number: {sum(user_number) / user_number[2]}")