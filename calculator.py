
import matplotlib.pyplot as plt
import copy

"""Each function will take amount owed, interest rate, minimum payment, and total amount to be applied monthly to debt.

All should take the above, specifics below:
One function will take the amount of CCs, APR for each, and return a pay off plan (maybe snowball vs avalanche?)
One function will calculate auto loan
One function will calculate mortgage amount

All return a graph of payoff over time, with one line including only minimum payments and one line being extra payment track"""

def mortgage_calculator(
    amount: float,
    rate: float,
    term: int,
    remaining_term_yrs: int,
    remaining_term_months: int,
    extra_payment_amount: int
    ):
    """Mortgage payoff timeline calculator. 
    
    Returns minimum monthly payment timeline and extra payment timeline with graphs, amount saved on interest, time saved
    
    Args: 
    amount: Original mortgage amount
    rate: Interest rate
    term: Mortgage term length (usually 30) 
    remaining_term: Time remaining in term, one var for years and one for months
    extra_payment_amount: Amount extra being put toward the mortgage each month"""

    # Minimum Mortgage Payment = P ( (i(1 + i)^n) / ((1 + i)^n – 1))
    # P=Principle, i=interest/12, n=number of payments

    # First calculate minimum monthly mortgage payment
    i = (rate / 100) / 12 # Monthly interest rate
    n = term * 12
    min_payment = round(amount * ((i * (1 + i) ** n) / ((1 + i) ** n - 1)), 2)
    total_paid_min_payments = min_payment * n # Total amount paid if you pay minimum the entire term
    total_interest_min_payments = total_paid_min_payments - amount # Total interest paid if paying the minimum


    # Get the total remaining months, months/amount paid so far
    # monthly interest = loan balance x monthly interest rate, and monthly principal = total monthly payment - monthly interest

    remaining_term = (remaining_term_yrs * 12) + remaining_term_months
    months_paid = n - remaining_term
    amount_paid = months_paid * min_payment, 2 # Amount paid so far in term

    # Go through full 30 yrs at minimum payments to determine principal, interest
    # Can add each one to a dict if I need to for visualization
    principal_paid = 0
    interest_paid = 0
    amount_paid = 0
    amount_remaining = amount
    monthly_remaining_balances = []
    payments = list(range(1, n+1))

    # Data for min payments
    for month in payments:
        interest = round(amount_remaining * i, 2)
        principal = round(min_payment - interest, 2)
        interest_paid = round(interest_paid + interest, 2)
        principal_paid = round(principal_paid + principal, 2)
        amount_paid = round(amount_paid + min_payment, 2)
        amount_remaining = round(amount_remaining - principal)
        monthly_remaining_balances.append(amount_remaining)
    
    xprincipal_paid = 0
    xinterest_paid = 0
    x_amount_paid = 0
    xamount_remaining = amount
    xmonthly_remaining_balances = []
    amount_remaining = amount
    xpayment = min_payment + extra_payment_amount
    month_count = 0
    
    # Data for extra payments
    while xamount_remaining > 0:
        # Need to account for min payments already made
        if month_count < n - remaining_term:
            interest = round(xamount_remaining * i, 2)
            principal = round(min_payment - interest, 2)
            xinterest_paid = round(xinterest_paid + interest, 2)
            xprincipal_paid = round(xprincipal_paid + principal, 2)
            x_amount_paid = round(x_amount_paid + min_payment, 2)
            xamount_remaining = round(xamount_remaining - principal)
            xmonthly_remaining_balances.append(xamount_remaining)
        else:
            interest = round(xamount_remaining * i, 2)
            if interest + xamount_remaining < xpayment:
                xpayment = interest + xamount_remaining
            principal = round(xpayment - interest)
            xinterest_paid = round(xinterest_paid + interest, 2)
            xprincipal_paid = round(xprincipal_paid + principal, 2)
            x_amount_paid = round(x_amount_paid + xpayment, 2)
            xamount_remaining = round(xamount_remaining - principal)
            xmonthly_remaining_balances.append(xamount_remaining)
        month_count += 1
    
    xpayments = list(range(1, month_count+1))
    
    # Visualize to compare the two lines
    # Print how much money in interest and time was saved
    fig, ax = plt.subplots()
    fig.suptitle("Mortgage Payoff Timeline")
    ax.plot(payments, monthly_remaining_balances, color="Gray") # Making Minimum Payments
    ax.plot(xpayments, xmonthly_remaining_balances, color="Blue") # Making Additional Payments
    ax.set_xlabel("Number of Payments Made")
    ax.set_ylabel("Amount Remaining")
    ax.legend(["Making Minimum Payments", "Making Additional Payments"])
    plt.show()

    print(f"Initial Mortgage Amount:                ${amount}")
    print(f"Minimum Payment:                        ${min_payment:.2f}")
    print(f"Total Interest Paid if Paying Minimum:  ${interest_paid:.2f}")
    print(f"Total Amount Paid if Paying Minimum:    ${amount_paid:.2f}")
    print(f"Time Taken to Pay:                      {n // 12} years, {n % 12} months")
    print("=============================================================================================")
    print(f"Extra Payment Amount:                   ${extra_payment_amount:.2f}")
    print(f"New Payment Amount:                     ${min_payment + extra_payment_amount:.2f}")
    print(f"Total Interest Paid if Paying Extra:    ${xinterest_paid:.2f}")
    print(f"New Total Amount Paid:                  ${x_amount_paid:.2f}")
    print(f"Time Taken to Pay with Extra:           ${month_count // 12} years, {month_count % 12} months")
    print("=============================================================================================")
    print(f"Money Saved with Extra Payments:        ${amount_paid - x_amount_paid:.2f}")
    print(f"Time Saved with Extra Payments:         {(n - month_count) // 12} years, {(n - month_count) % 12} months")


# May end up making the graphing data loops separate functions. Prob gonna reuse them in every func
def cc_calculator(num_of_cards: int):
    """Credit card payoff timeline calculator. 
    
    Returns minimum monthly payment timeline and extra payment timeline with graphs, amount saved on interest, time saved
    Also returns a plan to pay off the cards using the snowball method with the extra payment

    Using 30 days as average month for calculating interest for the purpose of this project
    
    Args: 
    num_of_cards: The number of credit cards the user has"""

    # Gather card data 
    cards = {}
    for card_num in range(1, num_of_cards + 1):
        print(f"Card {card_num}:")
        try:
            amount = float(input("Balance: "))
        except:
            amount = float(input("Enter a valid number: "))
        try:
            apr = float(input("APR: "))
        except:
            apr = float(input("Enter a valid number: "))    
        try:
            min_payment = float(input("Minimum Payment: "))
        except:
            min_payment = float(input("Enter a valid number:"))
        cards[f"card{card_num}"] = [amount, apr, min_payment]
    
    try:
        extra_payment = float(input("How much extra can you afford to pay each month? "))
    except:
        extra_payment = float(input("Enter a valid number: "))
    
    # Calculate how long it would take paying the minimum on each
    cards_copy = copy.deepcopy(cards)
    monthly_remaining_balances = [] # This will be data for graph
    month_count = 0
    total_balance = sum([data[0] for data in cards_copy.values()])
    interest_paid = 0

    while total_balance > 0:
        month_count += 1
        for card in cards_copy.values():
            amount_remaining = card[0]
            if amount_remaining == 0: 
                continue # Move on from this card if it's paid off
            apr = card[1]
            min_payment = card[2]
            interest = round((((apr / 100) / 365) * amount_remaining) * 30, 2)
            if interest + amount_remaining < min_payment:
                min_payment = interest + amount_remaining
            principle = round(min_payment - interest, 2)
            amount_remaining = round(amount_remaining - principle, 2)
            card[0] = amount_remaining
            total_balance = round(total_balance - principle, 2)
            interest_paid = round(interest_paid + interest, 2)
        monthly_remaining_balances.append(total_balance)

    months = list(range(1, month_count + 1))

    # Do the same as above but apply extra payment to smallest card
    xcards_copy = copy.deepcopy(cards)
    sorted_cards = dict(sorted(xcards_copy.items(), key=lambda item: item[1][0]))
    xmonthly_remaining_balances = [] # This will be data for graph
    xmonth_count = 0
    xtotal_balance = sum([data[0] for data in xcards_copy.values()])
    xinterest_paid = 0
    cc_month_counts = {}
    # extra_payment already exists = float(input("How much extra can you afford to pay each month?"))

    first = True
    for val in sorted_cards.values():
        if first: 
            val.append(True)
            first = False
        else: val.append(False)
    
    change_smallest = False

    # Loop through and make payments with snowball method
    while xtotal_balance > 0:
        xmonth_count += 1
        leftover = 0
        for card in sorted_cards.items():
            amount_remaining = card[1][0]
            if amount_remaining == 0: 
                continue # Move on from this card if it's paid off
            if change_smallest: 
                card[1][-1] = True
            if xmonth_count == 1:
                cc_month_counts[card[0]] = 1
            else: cc_month_counts[card[0]] += 1
            apr = card[1][1]
            min_payment = card[1][2]
            if leftover > 1:
                min_payment += leftover
                leftover = 0
            if card[1][-1]:
                if change_smallest:
                    change_smallest = False
                else:
                    min_payment += extra_payment
            interest = round((((apr / 100) / 365) * amount_remaining) * 30, 2)
            if interest + amount_remaining < min_payment:
                leftover = min_payment - (interest + amount_remaining)
                change_smallest = True
                extra_payment = min_payment
                min_payment = interest + amount_remaining
            principle = round(min_payment - interest, 2)
            amount_remaining = round(amount_remaining - principle, 2)
            card[1][0] = amount_remaining
            xtotal_balance = round(xtotal_balance - principle, 2)
            xinterest_paid = round(xinterest_paid + interest, 2)
        
        xmonthly_remaining_balances.append(xtotal_balance)
    
    # Print data, instructions, and results
    for card in cards.items():
        print(f"Card {card[0][-1]}-----")
        print(f"Balance: {card[1][0]}")
        print(f"Minimum Payment: {card[1][2]}")
    if num_of_cards > 1:
        count = 0
        last_month = 0
        for card in cc_month_counts.items():
            count += 1
            name = card[0]
            if count == 1:
                print(f"Month 1 - Month {card[1]}:")
                print(f"Apply your extra payment on Card {card[0][-1]} &")
                print("pay the minimum on any other cards.")
            elif count == num_of_cards:
                print(f"Month {last_month + 1} - Month {card[1]}")
                print(f"Add everything from the previous card(s) to the payment to Card {card[0][-1]}.")
                print(f"You could be credit card debt free and pay off your {num_of_cards} cards in {int(xmonth_count // 12)} year(s) & {xmonth_count % 12} months!")
            else:
                print(f"Month {last_month + 1} - Month {card[1]}")
                print(f"Add everything from the previous card(s) to the payment to Card {card[0][-1]} &")
                print("pay the minimum on any other cards.")
            last_month = card[1]
    else:
        print(f"With your extra payment you can pay off your card amd be credit card debt free in {int(xmonth_count // 12)} year(s) and {xmonth_count % 12} months!")
    
    print(f"That's far better than taking {int(month_count // 12)} year(s) and {month_count % 12} months just paying the minimum.")
    
    xmonths = list(range(1, xmonth_count + 1))

    # Visualize data
    fig, ax = plt.subplots()
    fig.suptitle("Credit Card Payoff Timeline")
    ax.plot(months, monthly_remaining_balances)
    ax.plot(xmonths, xmonthly_remaining_balances)
    ax.set_xlabel("Number of Payments Made")
    ax.set_ylabel("Total Balance Remaining")
    ax.legend(["Making Minimum Payments", "Making Additional Payments"])
    plt.show()
        

def auto_calculator():
    pass


#mortgage_calculator(400000, 5, 30, 22, 6, 500)

#num_cards = input("How many cards? ")
#num_cards = int(num_cards)
#cc_calculator(num_cards)