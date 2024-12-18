# Created by IgorCT - Dez_2024

# variables
user_input = 0
average_list = []

# while loop 
while user_input != -1:
  # user input
  user_input = int(input("Enter a number different of zero (-1 to exit): "))
  if user_input != 0:
    average_list.append(user_input)
    print(f"Numbers average: {sum(average_list)/len(average_list)}")