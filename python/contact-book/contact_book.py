# Import dependencies
from art import logo

print(logo)

# Function manage_contacts() to encapsulate all contact management logic
def manage_contacts():
    # Empty dictionary `contacts` to store contact name and phone as key:value pairs
    contacts = {}

    # `While` loop to allow the user to perform multiple actions (adding, viewing, or quitting) without restarting program
    continue_actions = True

    # Add contact details to a diary.
    def output_to_file():
        with open('diary.csv', 'w', newline='') as file:
            for contact, number in contacts.items():
                file.write('%s:%s\n' % (contact, number))
    
    while continue_actions:
        # Prompt user for choice (a=add contact, v=view contact, q=quit)
        print(f"Options - a=add contacts, v=view contacts, o=output to diary, q=quit application")
        choice = input(f"Please select your choice of action: ").lower() # Convert input to lowercase

        # Adding a contact - user must enter a contact name, and number
        if choice == 'a':
            name = input(f"\nPlease enter the contact name: ") # Prompt user to enter contacts name, and store in `name` variable
            number = input(f"Please enter the contact number: ") # Prompt user to enter contacts number, and store in `number` variable
            contacts[name] = number # Add new contact to `contacts` dictionary with `name` as key
            print(f"\nThe contact was successfully added - {contacts}\n")
        # Viewing a contact - check `contacts` dictionary for any contacts and print existing contacts to user
        elif choice == 'v':
            # If `contacts` dictionary is empty, inform user there are no contacts, otherwise loop through `contacts` dictionary, and print results
            if not contacts:
                print(f"There are no contacts. Please first add a contact name, and number. \n")
            else:
                for name, number in contacts.items():
                    print(f"Contact: {name}, Number: {number}")
        # Output to diary - user can export and save contact details to a contact diary
        elif choice == 'o':
            print(f"Adding contacts to diary...")
            output_to_file()
            print(f"Contacts added.")
        # Quitting program - exits the loop and closes the application
        elif choice == 'q':
            break
        # Manage any invalid input
        else:
            print(f"Please enter a valid choice...\n")
    
    print("Exiting application...")


manage_contacts() # Call the function
