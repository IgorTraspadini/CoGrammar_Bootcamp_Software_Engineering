# Created by IgorCT - Dez_2024

# reads in a string and makes each alternate character into an uppercase character and each other alternate character a lowercase character.

# variable input
user_input = input("Enter a phrase:")

# alternate letter 
alter_letter = [value.upper() if index % 2 == 0 else value.lower() for index, value in enumerate(user_input)]
print("".join(alter_letter))

# alternate word 
alter_word = user_input.split(" ")
alter_word = [value.lower() if index % 2 == 0 else value.upper() for index, value in enumerate(alter_word)]
print(" ".join(alter_word))