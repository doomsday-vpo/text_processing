# You are given a collection of tickets separated by commas and spaces (one or many). You need to check each ticket to see if it has a winning combination of symbols:
# •	A valid ticket has exactly 20 characters.
# •	A winning ticket is a valid one, containing one of the symbols '@', '#', '$' or '^' uninterruptedly repeated at least 6 times in both halves of the tickets.
# •	In order to win a Jackpot, the ticket should contain the same winning symbol 10 times on both sides
# An example of a valid winning ticket:
# "Cash$$$$$$Ca$$$$$$sh"
# An example of a Jackpot winning valid ticket:
# "$$$$$$$$$$$$$$$$$$$$"
# Input
# The input will be read from the console. The input consists of a single line containing all tickets separated by commas and one or more white spaces in the format:
# •	"{ticket}, {ticket}, … {ticket}"
# Output
# Print the result for every ticket in the order of their appearance, each on a separate line in the format:
# •	If the ticket is invalid: "invalid ticket"
# •	If the ticket is valid, but it is not winning: "ticket "{ticket}" - no match"
# •	If the ticket is valid and winning, but not a Jackpot:
# "ticket "{ticket}" - {uninterrupted_match_length}{match_symbol}"
# •	If the ticket hits the Jackpot:
# "ticket "{ticket}" - {uninterrupted_match_length}{match_symbol} Jackpot!"
# Constraints
# •	Number of tickets will be in range [0 … 100]


def check_ticket(ticket):
    if len(ticket) != 20:
        return "invalid ticket"

    winning_symbols = ['@', '#', '$', '^']
    left_half = ticket[:10]
    right_half = ticket[10:]

    best_length = 0
    winning_symbol = ''

    for symbol in winning_symbols:
        # Check left half
        left_count = 0
        max_left = 0
        for char in left_half:
            if char == symbol:
                left_count += 1
            else:
                max_left = max(max_left, left_count)
                left_count = 0
        max_left = max(max_left, left_count)

        # Check right half
        right_count = 0
        max_right = 0
        for char in right_half:
            if char == symbol:
                right_count += 1
            else:
                max_right = max(max_right, right_count)
                right_count = 0
        max_right = max(max_right, right_count)

        # Update best result
        current_length = min(max_left, max_right)
        if current_length > best_length:
            best_length = current_length
            winning_symbol = symbol

    if best_length < 6:
        return f'ticket "{ticket}" - no match'
    elif best_length == 10:
        return f'ticket "{ticket}" - {best_length}{winning_symbol} Jackpot!'
    else:
        return f'ticket "{ticket}" - {best_length}{winning_symbol}'


# Read input
tickets = [ticket.strip() for ticket in input().split(',')]

# Process each ticket
for ticket in tickets:
    ticket = ticket.strip()
    print(check_ticket(ticket))
