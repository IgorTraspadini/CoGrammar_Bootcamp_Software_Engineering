# Created by IgorCT - Dez_2024

print("############## Manipulation string ########################")
str_manip = input("Please, enter a sentence: ")

# print the string size
print(f"The string length is: {len(str_manip)}")

# replace the last character per '@'
print(f"{str_manip.replace(str_manip[-1],'@')}")

# print the last three characters 
print(f"{str_manip[-3:]}")

# create a five letter word made up the first two letters and last three letters
print(f"{str_manip[:2]}{str_manip[-3:]}")