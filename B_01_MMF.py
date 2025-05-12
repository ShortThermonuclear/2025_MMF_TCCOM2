def make_statement(statement, decoration):
    """Makes the heading stand out more by adding decorations."""
    print(f"{decoration * 3} {statement} {decoration * 3}")


def string_check(question, valid_ans_list=('yes', 'no'), num_letters=1):
    """Checks if the user enters the first letter or a full word from a list of words """

    while True:
        response = input(question).lower()

        for item in valid_ans_list:
            if response == item:
                return item
            elif response == item[:num_letters]:
                return item
            # checks if user enters valid item and responds correctly.
        else:
            print(f"Please choose an valid option from {valid_ans_list}.")
        # Prints an error message in the case of invalid input


def instructions():
    # Function for printing out instructions.
    make_statement("Instructions", "ℹ️")

    print('''
    
For each ticket holder enter..
 - Their name
 - Their age
 - Their payment method (cash/credit)
 
 The program will record the ticket sale and calculate the ticket cost and its profit.
 
 Once you have sold all five tickets or entered the exit code (xxx), 
 the program will display the sales information and write the data into a txt.file
 
 it will also choose one lucky ticket winner(their ticket is free)
 
    ''')


def not_blank(question):
    """Makes sure that the user can not enter a blank name."""

    while True:
        response = input(question)

        if response != "":
            return response

        print("This cannot be blank.")
        # Prints error message in the case when the user does not enter a name.


def int_check(question):
    """Checks if the input is an integer or not"""

    error = "Please enter a valid age"

    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print(error)
            # prints an error message if the user does not enter an integer.


# Main routine goes here

# Initializing variables.
payment_method = ('cash', 'credit')

# Initializing tickets
Max_tickets = 5
tickets_sold = 0

make_statement("Mini-Movie Fundraiser", "🍿")

print()
want_instructions = string_check("Do you want to see the instructions? ")

if want_instructions == "yes":
    instructions()

print()

while tickets_sold < Max_tickets:

    # Asks the user for their name.
    print()
    name = not_blank("Name: ")

    if name == "xxx":
        break

    # Asks the user for their age.
    age = int_check("Age: ")

    if age < 12:
        print(f"{name} is too young.")
        continue

    elif age > 120:
        print(f"??That looks like a typo (too old)")
        continue

    else:
        pass

    # Asks the user for their payment method.
    payment = string_check("Payment method: ", payment_method, 2)
    print(f"{name} has bought a ticket! ({payment})")

    tickets_sold += 1

if tickets_sold == Max_tickets:
    print("You have sold all the tickets!")

else:
    print(f'you have sold {tickets_sold}/{Max_tickets} tickets.')
