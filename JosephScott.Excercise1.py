"""
Joseph_ProgrammingExercise_1.py

Programming Exercise 1:
Pre-sell a limited number of cinema tickets.

Rules:
- Each buyer can buy up to 4 tickets.
- No more than 20 tickets can be sold total.
- Prompt the user for the desired number of tickets.
- Display the number of remaining tickets after their purchase.
- Repeat until all tickets have been sold.
- Display the total number of buyers.
"""


def get_valid_ticket_request(tickets_remaining):
    """
    brief description:
        Prompts the user for the number of tickets they wish to purchase and
        validates the input based on program rules.

    parameters (name: type):
        tickets_remaining: int

    variables used (name: type):
        user_input: str
        requested_tickets: int

    logical steps:
        1. Prompt the user for a ticket amount.
        2. Validate the input is a whole number.
        3. Convert the input to an integer.
        4. Ensure the value is between 1 and 4.
        5. Ensure the value does not exceed the remaining tickets.
        6. Repeat until valid input is entered.
        7. Return the valid ticket amount.

    return:
        requested_tickets: int
    """
    while True:
        # We prompt the user for input as a string to validate safely.
        user_input = input("How many tickets would you like to buy? (1 to 4): ")

        # We ensure the input is numeric before conversion.
        if not user_input.isdigit():
            print("Please enter a whole number between 1 and 4.")
            continue

        # We convert the validated input to an integer.
        requested_tickets = int(user_input)

        # We enforce the per-customer ticket limit.
        if requested_tickets < 1 or requested_tickets > 4:
            print("Each buyer may purchase between 1 and 4 tickets.")
            continue

        # We ensure the request does not exceed remaining tickets.
        if requested_tickets > tickets_remaining:
            print(f"Only {tickets_remaining} ticket(s) remain. Please enter a smaller amount.")
            continue

        # We return only when all validation rules are satisfied.
        return requested_tickets


def sell_cinema_tickets():
    """
    brief description:
        Controls the cinema ticket pre-sale process, tracks ticket inventory,
        and counts the number of buyers until all tickets are sold.

    parameters (name: type):
        None

    variables used (name: type):
        total_tickets: int
        tickets_remaining: int
        buyers_total: int
        requested_tickets: int

    logical steps:
        1. Initialize total ticket inventory to 20.
        2. Set remaining tickets equal to total inventory.
        3. Initialize buyer counter to 0.
        4. While tickets remain:
           a. Display tickets remaining.
           b. Prompt user for a valid ticket purchase.
           c. Subtract purchased tickets from remaining inventory.
           d. Increment buyer counter.
           e. Display updated ticket count.
        5. When tickets reach zero, display sold-out message.
        6. Display total number of buyers.

    return:
        None
    """
    # This constant represents the maximum tickets available.
    total_tickets = 20

    # This accumulator tracks remaining tickets.
    tickets_remaining = total_tickets

    # This accumulator tracks the number of buyers.
    buyers_total = 0

    # We continue selling tickets until none remain.
    while tickets_remaining > 0:
        # We inform the user of current availability.
        print(f"Tickets remaining: {tickets_remaining}")

        # We collect a validated ticket purchase amount.
        requested_tickets = get_valid_ticket_request(tickets_remaining)

        # We update the remaining ticket count.
        tickets_remaining -= requested_tickets

        # We increment the buyer count after a successful purchase.
        buyers_total += 1

        # We display the updated number of tickets remaining.
        print(f"Tickets remaining after purchase: {tickets_remaining}\n")

    # We notify the user that tickets are sold out.
    print("All tickets have been sold.")

    # We display the total number of buyers.
    print(f"Total number of buyers: {buyers_total}")


if __name__ == "__main__":
    # You would update these functions to be your functions in your assignment:
    sell_cinema_tickets()
