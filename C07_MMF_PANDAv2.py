import pandas

# list to hold details
all_names = ['A', 'B', 'C', 'D', 'E']
all_tickets = [7.50, 7.50, 10.50, 10.50, 6.50]
all_surcharges = [0, 0, 0.53, 0.53, 0]

mini_movie_dict = {
    'Name': all_names,
    'Ticket Price': all_tickets,
    'Surcharge': all_surcharges
}

# Create dataframe / table from dictionary.
mini_movie_frame = pandas.DataFrame(mini_movie_dict)

# Calculate total payable
mini_movie_frame['Total'] = mini_movie_frame['Ticket Price'] + mini_movie_frame['Surcharge']
mini_movie_frame['Total Profit'] = mini_movie_frame['Ticket Price'] - 5

# Working out sum of everything
total_paid = mini_movie_frame['Total'].sum()
total_profit = mini_movie_frame['Total Profit'].sum()

# Main routine

print(mini_movie_frame)
print()
print()
print(f"Total Paid: ${total_paid}")
print(f"Total Profit: ${total_profit}")
