# Function goes here
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


def not_blank(question):
    """Makes sure that the user can not enter a blank name."""

    while True:
        response = input(question)

        if response != "":
            return response

        print("This cannot be blank.")
        # Prints error message in the case when the user does not enter a name.


def string_check(question, valid_ans_list=('yes', 'no'), num_letters=1):
    # Checks if the user enters the first letter or a full word from a list of words

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


# Main routine

# Initializing variables.
payment_method = ('cash', 'credit')

# Ticket price list
CHILD_PRICE = 7.50
ADULT_PRICE = 10.50
SENIOR_PRICE = 6.50

# Credit Surcharge
credit_surcharge = 0.05

# Looping for testing purposes.
while True:
    print()

    # Asks the user for their name.
    name = not_blank("Name: ")

    # Asks the user for their age. and checks if their age is in the selected gap.
    age = int_check("Age: ")

    if age < 12:
        print(f"{name} is too young.")
        continue

    elif 12 <= age < 16:
        ticket_price = CHILD_PRICE

    elif 16 <= age < 65:
        ticket_price = ADULT_PRICE

    elif 65 <= age < 120:
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

    # Total price
    total_price = ticket_price + surcharge

    print(f"{name}'s ticket cost is {ticket_price}, paid by {payment}"
          f", so the surcharge is {surcharge}"
          f", therefore the total cost is {total_price}")
