# Created by IgorCT - Jan_2025
# Program that allows a user to register students for an exam venue.

# Print a header for the program
print("###################### Exam Register ###########################")

# Ask the user for the number of students to register
student_quantity = int(input("How many students will be registering? "))

# Open the file 'reg_from.txt' in append mode to add student IDs
file = open('reg_form.txt', 'w')

# Loop through the number of students to register
for i in range(student_quantity):
    # Ask the user to enter the student ID number
    student_ID = input("Enter student ID number: ")
    
    # Write the student ID to the file, followed by a dotted line.
    file.write(student_ID + " .............................................\n")

# Close the file after writing all student IDs
file.close()
