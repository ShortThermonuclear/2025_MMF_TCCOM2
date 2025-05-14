import pandas
import random


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


def currency(x):
    return "${:.2f}".format(x)


# Main routine goes here

# Initializing variables.
payment_method = ('cash', 'credit')

# Ticket price list
CHILD_PRICE = 7.50
ADULT_PRICE = 10.50
SENIOR_PRICE = 6.50

# Credit Surcharge
credit_surcharge = 0.05

# list to hold details
all_names = []
all_tickets = []
all_surcharges = []

mini_movie_dict = {
    'Name': all_names,
    'Ticket Price': all_tickets,
    'Surcharge': all_surcharges
}

# Initializing tickets
Max_tickets = 5
tickets_sold = 0

# Program main heading
make_statement("Mini-Movie Fundraiser", "🍿")

print()
want_instructions = string_check("Do you want to see the instructions? ")

if want_instructions == "yes":
    instructions()

print()

# Loop to get name, age and payment.
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

    elif age < 16:
        ticket_price = CHILD_PRICE

    elif age < 65:
        ticket_price = ADULT_PRICE

    elif age < 120:
        ticket_price = SENIOR_PRICE

    else:

        print(f"??That looks like a typo (too old)")
        continue

    # Asks the user for their payment method.
    payment = string_check("Payment method: ", payment_method, 2)

    if payment == "cash":
        surcharge = 0

    else:
        surcharge = ticket_price * credit_surcharge

    # Table to hold name, age, price and profit
    all_names.append(name)
    all_tickets.append(ticket_price)
    all_surcharges.append(surcharge)

    tickets_sold += 1

#  End of ticket loop.

mini_movie_frame = pandas.DataFrame(mini_movie_dict)

# Calculate total payable
mini_movie_frame['Total'] = mini_movie_frame['Ticket Price'] + mini_movie_frame['Surcharge']
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

# Working out sum of everything
total_paid = mini_movie_frame['Total'].sum()
total_profit = mini_movie_frame['Profit'].sum()

# Choose a random winner
winner = random.choice(all_names)

# retrieve ticket price and surcharge
winner_index = all_names.index(winner)

# find total won
ticket_won = mini_movie_frame.at[winner_index, 'Total']
profit_won = mini_movie_frame.at[winner_index, 'Profit']

# Currency formatting
add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

print()
print(mini_movie_frame.to_string(index=False))
print()
print()
print(f"Total Paid: ${total_paid:.2f}")
print(f"Total Profit: ${total_profit:.2f}")

# winner announcement
print(f'The lucky winner is {winner}. Their ticket worth ${ticket_won:.2f} is free!')
print(f'Total Paid is now ${total_paid - ticket_won:.2f}')
print(f"Total profit is now ${total_profit - profit_won:.2f}")

if tickets_sold == Max_tickets:
    print("You have sold all the tickets!")

else:
    print(f'you have sold {tickets_sold}/{Max_tickets} tickets.')
