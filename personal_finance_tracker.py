"""

1. Project name: personal finance tracker
2. Version: 2nd version 
3. Purpose : to improve the core logic and to be ensure code with better error hadling and with clear comments to explain and to be ensure code to helps for future file handling

"""
balance = 0
transactions = [] 

def get_valid_amount(): # to ensure to getting valid input of amount from user 
    while True:    
        try:
            amount = float(input("Enter amount: "))

            if amount <= 0: # to ensure to enter the amount correctly
                print("Amount must be greater than zero.")
                continue #skip the remaining code and starts from starting of the loop 
            
            return amount
        
        except ValueError: # print below statement if the user enters incorrect formated input and then runs the while loop from start
            print("Invalid input. Please enter a numeric value.")

def create_transaction(transaction_type):
    """
    Creates a single transaction dictionary and updates balanec.
    transaction_type: 'deposit' or 'withdraw'

    """

    global balance # we are modifying global balance

    amount = get_valid_amount() # validated amount input
    reason = input("Enter reason for transaction: ")

    # logic for deposit
    if transaction_type == "deposit":
        balance += amount

    # logic for withdrawal
    elif transaction_type == "withdraw":
        if amount > balance:
            print("Insufficient balance. Transaction cancelled.")
            return # stop function, no transaction created
        balance -= amount

    # transaction dictionary
    transaction = {
        "type": transaction_type,
        "amount": amount, 
        "reason": reason, 
        "balance_after": balance
    }    

    # store transaction
    transactions.append(transaction)
    
    print("Transactoin added successfully.")