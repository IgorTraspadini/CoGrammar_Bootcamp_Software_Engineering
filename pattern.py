# Variable to keep track of the number of rows for the reverse pattern
count_rev = 5

# Loop through each row from 1 to 9
for i in range(1, 10):
    # Check if the current row is less than 6
    if i < 6:
        # Print a pattern of asterisks (*) for the current row
        # The number of asterisks increases by 1 for each row
        print(i * "*")
    else:
        # Decrement the count for the reverse pattern
        count_rev -= 1
        # Print a pattern of asterisks (*) for the current row
        # The number of asterisks decreases by 1 for each row
        print(count_rev * "*")
