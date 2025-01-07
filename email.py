# Created by IgorCT - Jan_2025

# Initialize an empty list to store emails
inbox = []
# Variable to store the user's menu option
option = ""

# Define the Email class to represent an email object
class Email():
    def __init__(self, email_address, subject_line, email_content):
        # Initialize email attributes
        self.email_address = email_address  # Sender's email address
        self.subject_line = subject_line    # Subject of the email
        self.email_content = email_content  # Content of the email
        # Mark email as unread by default
        self.has_been_read = False
    
    # Method to mark an email as read
    def mark_as_read(self):
        self.has_been_read = True

# Function to populate the inbox with sample emails
def populate_inbox():
    # Populate the inbox with 3 sample emails
    for x in range(0, 3):
        inbox.append(Email("igorct"+str(x)+"@gmail.com", "Email number " + str(x), "Hi, This is the email number " + str(x) + " created to test the Email class"))

# Function to list all emails in the inbox
def list_emails():
    # Loop through the inbox and print each email's subject line with its index
    for i, email in enumerate(inbox):
        print(f"{i} {email.subject_line}")

# Function to read an email by its index
def read_email(index):
    try:
        # Print the email's details (sender, subject, and content)
        print(f"{index}. {inbox[index].email_address} - {inbox[index].subject_line} - {inbox[index].email_content}")
        # Mark the email as read
        inbox[index].has_been_read = True
        print(f"Email {index} has been marked as read.")
    except:
        # Handle invalid index (e.g., if the index is out of range)
        print(f"Email {index} does not exist.")

# Populate the inbox with sample emails
populate_inbox()

# Function to display the menu options
def print_menu():
    print("\n")
    print("################# Email System ##################")
    print("# Select an option:                             #")
    print("# 1 -> List all emails in the inbox             #")
    print("# 2 -> Read an email by index                   #")
    print("# 3 -> View unread emails                       #")
    print("# 4 -> Exit the email system                    #")
    print("#################################################")  

# Main loop to handle user input
while option != "4":
    # Display the menu
    print_menu()
    # Get the user's option
    option = input("Enter your option: ")
    if option == "1":
        # List all emails in the inbox
        print("#        List all emails in the inbox           #")  
        list_emails()
    elif option == "2":
        # Read an email by its index
        print("#            Read an email by index             #")
        read_email(int(input("Enter the index of the email you want to read: ")))
    elif option == "3":
        # View unread emails
        print("#              View unread emails               #")
        for i, email in enumerate(inbox):
            if email.has_been_read == False:
                print(f"{i}. {email.subject_line}")
    elif option == "4":
        # Exit the email system
        print("Exiting the email system.")
    else:
        # Handle invalid input
        print("Invalid option. Please try again.")
        