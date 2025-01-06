# Created by IgorCT - Jan_2025

# Try block to handle potential file-related errors
try:
    # Open the file "DO.txt" in read mode
    with open("DOB.txt", "r") as f:
        # Print a header for the names section
        print("Name")
        # Loop through each line in the file
        for line in f:
            # Strip whitespace and split the line into a list of words
            line_split = line.strip().split()
            # Join the first two words (assumed to be the name) and print them
            print(' '.join(line_split[:2]))
        
        # Print a newline for spacing
        print("\n")
        
        # Print a header for the birthdate section
        print("Birthdate")
    
    # Open the file "DOB.txt" in read mode
    with open("DOB.txt", "r") as f:    
        # Loop through each line in the file
        for line in f:
            # Strip whitespace and split the line into a list of words
            line_split = line.strip().split()
            # Join the remaining words (assumed to be the birthdate) and print them
            print(' '.join(line_split[2:]))

# Except block to handle file not found or other errors
except:
    # Print an error message if the file is not found or an error occurs
    print("File not found!")  # or any other error message you want to display
    