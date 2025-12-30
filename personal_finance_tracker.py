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

def create_transaction(transaction_type, amount, reason, balance):
    """
    Creates a single transaction dictionary and updates balanec.
    transaction_type: 'deposit' or 'withdraw'

    """
    # transaction dictionary
    transaction = {
        "type": transaction_type,
        "amount": amount, 
        "reason": reason, 
        "balance_after": balance
    }    

    # store transaction
    transactions.append(transaction)
    
    print("Transaction added successfully.")


def show_transactions():
    """
    Displays all transactions in a readable format.
    """
    if not transactions:
        print("No transactions found.")
        return 
    
    print("\n----- TRANSACTION HISTORY -----")

    for index, transaction in enumerate(transactions, start=1):
        print(f"\nTransaction {index}")
        print(f"Type    : {transaction['type']}")
        print(f"Amount  : ₹{transaction['amount']}")
        print(f"Reason  : {transaction['reason']}")
        print(f"Balance : ₹{transaction['balance_after']:.2f}")
        
    print("\n-------------------------------")

def show_balance():
    """
    Displays the current available balance.
    """
    print("\n----- CURRENT BALANCE -----")
    print(f"Available Balance: ₹{balance:.2f}")
    print("\n---------------------------")

def show_menu():
    """
    Displays the main menu options.
    """
    print("\n====== PERSONAL FINANCE TRACKER ======")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Show Balance")
    print("4. Show Transactions")
    print("5. Exit")
    print("\n======================================")
   
def main():
    """
    Main function to control the program flow.
    """
    while True:
        show_menu()

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            deposit_money()

        elif choice == "2":
            withdraw_money()

        elif choice == "3":
            show_balance()
        
        elif choice == "4":
            show_transactions()

        elif choice == "5":
            print("Thank you for using Personal Finance Tracker. Goodbye!")
            break # exit the while loop and program ends

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
        
def withdraw_money():
    """
    Handles withdrawing money from the account.
    Ensures balance safety and logs transaction details.
    """
    global balance

    print("\n--- Withdraw Money ---")

    amount = get_valid_amount()

    if amount > balance:
        print("You can't withdraw more money than available in your account.")
        return # stop this function safely 

    reason = input("Enter reason for withdrawal: ").strip()
    if not reason:
        print("Reason required")
        return

    balance -= amount

    create_transaction("withdraw", amount, reason, balance)

    print(f"Withdrawal successful! Current balance: ₹{balance:.2f}")
        
def deposit_money():
    """
    Handles deposit money into the account.
    Ensures balance safety and logs transaction details.
    """        
    global balance

    print("\n--- Deposit Money  ---")

    amount = get_valid_amount()

    reason = input("Enter reason for deposit: ").strip()
    if not reason:
        print("Reason required")
        return
    
    balance += amount

    create_transaction("deposit", amount, reason, balance)
    
    print(f"Deposit successful! Current balance: ₹{balance:.2f}")
