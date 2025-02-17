
import matplotlib.pyplot as plt

"""Each function will take amount owed, interest rate, minimum payment, and total amount to be applied monthly to debt.

All should take the above, specifics below:
One function will take the amount of CCs, APR for each, and return a pay off plan (maybe snowball vs avalanche?)
One function will calculate auto loan
One function will calculate mortgage amount

All return a graph of payoff over time, with one line including only minimum payments and one line being extra payment track"""

def mortgage_calculator(amount: int,
                        rate: float,
                        term: int,
                        remaining_term_yrs: int,
                        remaining_term_months: int,
                        extra_payment_amount: int):
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
    # Need to see how much is going to principle and how much is going to interest
    i = (rate / 100) / 12 # Monthly interest rate
    n = term * 12
    min_payment = round(amount * ((i * (1 + i) ** n) / ((1 + i) ** n - 1)), 2)
    total_paid_min_payments = min_payment * n # Total amount paid if you pay minimum the entire term
    total_interest_min_payments = total_paid_min_payments - amount # Total interest paid if paying the minimum


    # Get the total remaining months, months/amount paid so far
    # Need to figure out how much principle is remaining specifically
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
            if xamount_remaining < 0: xamount_remaining = 0
            xmonthly_remaining_balances.append(xamount_remaining)
        else:
            interest = round(xamount_remaining * i, 2)
            principal = round(xpayment - interest)
            xinterest_paid = round(xinterest_paid + interest, 2)
            xprincipal_paid = round(xprincipal_paid + principal, 2)
            x_amount_paid = round(x_amount_paid + xpayment, 2)
            xamount_remaining = round(xamount_remaining - principal)
            if xamount_remaining < 0: xamount_remaining = 0
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


def cc_calculator():
    pass


mortgage_calculator(400000, 5, 30, 22, 6, 500)