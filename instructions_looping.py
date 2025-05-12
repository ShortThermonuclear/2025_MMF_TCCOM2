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


# Main routine goes here

make_statement("Mini-Movie Fundraiser", "🍿")

print()
want_instructions = string_check("Do you want to see the instructions")

if want_instructions == "yes":
    instructions()

print()
print()