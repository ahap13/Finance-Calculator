
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
    total_paid_min_payments = round(min_payment * n, 2) # Total amount paid if you pay minimum the entire term
    total_interest_min_payments = total_paid_min_payments - amount

    # Get the total remaining months, months/amount paid so far
    # Need to figure out how much principle is remaining specifically
    # monthly interest = (loan balance x monthly interest rate), and monthly principal = total monthly payment - monthly interest
    remaining_term = (remaining_term_yrs * 12) + remaining_term_months
    months_paid = n - remaining_term
    amount_paid = months_paid * min_payment # Amount paid so far in term

    # Loop through term, process minimum payments for paid so far
    # Figure out how much was spent on principle, interest
    # Figure how much principle is remaining
    # For each payment, take remaining principle and recalculate out monthly interest
    # Remaining principle (minimum monthly payment + extra monthly payment - monthly interest)
    # Keep going until remaining principle == 0
    # Keep track of how many total payments (to get time saved), and total interest saved

    print(min_payment)
    print(total_paid_min_payments)
    print(total_interest_min_payments)
    print(remaining_term)
    print(months_paid)
    print(amount_paid)

mortgage_calculator(400000, 4.5, 30, 20, 6, 0)