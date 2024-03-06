# Prompt what the program do
print("Welcome to contact management system. Type in what you wanna do! ")
print("Type in 'a' to add a contact, type in 'd' to display all your contacts")
print("'r' to remove the contacts and 'w' to write the contacts you .txt  (e to exit)")

# define contact class
class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email
    def get_name(self):
        return self.name
    def get_phone(self):
        return self.phone_number
    def get_email(self):
        return self.email

def add_contact(arr):
    print("Adding the contact: ")
    list = int(input("Please provide how much contacts you wanna add: "))
    for _ in range(list):
        name = str(input("Please provide your contact name: "))
        phone_number = float(input("Please provide contact phone number: "))
        email = str(input("Please provide contact email: "))
        newContact = Contact(name, phone_number, email)
        arr.append(newContact)

def display_contact(arr):
    arr_size = len(arr)
    i = 0
    print("Displaying the contacts:")
    for contact in arr:
        print("Contact number ", i+1)
        print("Name:", contact.get_name())
        print("Phone number:", contact.get_phone())
        print("Email:", contact.get_email())
        print()
        i += 1

def remove_contact(arr):
    print("Removing the contact:")
    c_remove = int(input("Please provide the contact number to remove: "))
    if(c_remove > len(arr)):
        print("The contact number you provided is not on the list!")
    else:
        del arr[c_remove - 1]

def write_contact():
    print("Writing the contacts to")


# define which answers are correct
accepted_answers = ["a", "d", "r", "w"]
contacts = [] # Empty array to store in the objects we create

valid_input = False # see if valid input is true then proceed to function

while True:
    user_input = str(input("Type the answer here: "))
    input_length = len(user_input)
    # Data validating
    if input_length != 1:
        print("You are supposed to type in 1 character!")
        continue
    elif user_input.isnumeric():
        print("You are supposed to type in character!")
        continue
    if user_input.lower() == "e":
        print("Exiting the program!")
        break
    for char in accepted_answers:
        if user_input.lower() == char:
            valid_input = True
            break
    else:
        print("The only characters accepted: a, d, r, w!")
        continue

    if valid_input:
        if user_input.lower() == "a":
            add_contact(contacts)
        elif user_input.lower() == "d":
            display_contact(contacts)
        elif user_input.lower() == "r":
            remove_contact(contacts)
        elif user_input.lower() == "w":
            write_contact()