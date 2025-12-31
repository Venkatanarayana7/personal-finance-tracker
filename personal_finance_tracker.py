"""

1. Project name: personal finance tracker
2. Version: 2nd version 
3. Purpose : to improve the core logic and to be ensure code with better error hadling and with clear comments to explain and to be ensure code to helps for future file handling

"""
BASE_WIDTH = 80
balance = 0
transactions = [] 
def center_text(text, width):
    return text.center(width)

def show_welcome_banner(width):
    print("\n" + "=" * width)
    print(center_text("🏦 RGUKT BANK 🏦", width))
    print(center_text("Trusted Bank for Every IIIT Student", width))
    print(center_text("Secure • Simple • Student-Friendly", width))
    print("=" * width + "\n")

def show_section_title(title, width):
    print("\n" + f" {title} ".center(width, "-"))


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


def show_balance():
    """
    Displays the current available balance.
    """
    show_section_title("💰 CURRENT BALANCE", BASE_WIDTH)
    print(center_text(f"Available Balance: ₹{balance:.2f}", BASE_WIDTH))

def show_menu():
    """
    Displays the main menu options.
    """
    print("".center(BASE_WIDTH, "="))
    print(center_text("💳 PERSONAL FINANCE TRACKER 💳", BASE_WIDTH))
    print("".center(BASE_WIDTH, "="))
    print(center_text("1. ➕ Deposit Money", BASE_WIDTH))
    print(center_text("2. ➖ Withdraw Money", BASE_WIDTH))
    print(center_text("3. 💰 Show Balance", BASE_WIDTH))
    print(center_text("4. 📊 Show Transactions", BASE_WIDTH))
    print(center_text("5. 🚪 Exit", BASE_WIDTH))
    print("".center(BASE_WIDTH, "="))


def main():
    """
    Main function to control the program flow.
    """
    show_welcome_banner(BASE_WIDTH)
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
            print_transactions(transactions)

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

    show_section_title("➖ WITHDRAW MONEY", BASE_WIDTH)
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

    show_section_title("➕ DEPOSIT MONEY", BASE_WIDTH)
    amount = get_valid_amount()

    reason = input("Enter reason for deposit: ").strip()
    if not reason:
        print("Reason required")
        return
    
    balance += amount

    create_transaction("deposit", amount, reason, balance)
    
    print(f"Deposit successful! Current balance: ₹{balance:.2f}")

def calculate_column_widths(transactions):
    # Initial widths based on column headers
    no_width = len("No")
    type_width = len("Type")
    amount_width = len("Amount")
    reason_width = len("Reason")
    balance_width = len("Balance After")

    for idx, t in enumerate(transactions, start=1):
        no_width  = max(no_width, len(str(idx)))
        type_width = max(type_width, len(t['type'].upper()))
        amount_width = max(amount_width, len(f"₹{t['amount']:.2f}"))
        reason_width = max(reason_width, len(t['reason']))
        balance_width = max(balance_width, len(f"₹{t['balance_after']:.2f}"))

    return no_width, type_width, amount_width, reason_width, balance_width

def print_table_header(no_width, type_width, amount_width, reason_width, balance_width):
    # Total width for separator line
    total_width = no_width + type_width + amount_width + reason_width + balance_width + 13 # 13 acconts for spaces and | separators

    # Print Separator
    print("-" * total_width)

    # Print header row
    header = f"{'No'.ljust(no_width)} | {'Type'.ljust(type_width)} | {'Amount'.rjust(amount_width)} | {'Reason'.ljust(reason_width)} | {'Balance After'.rjust(balance_width)}"
    print(header)

    # Print  Seperator 
    print("-" * total_width)

    return total_width


def print_transactions(transactions):
    if not transactions:
        print("No transactions found.")
        return
    
    # Step 1: calculate colums widths
    no_w, type_w, amount_w, reason_w, balance_w, = calculate_column_widths(transactions)

    
    # Step 2: print table header
    total_w = print_table_header(no_w, type_w, amount_w, reason_w, balance_w)
    show_section_title("📊 TRANSACTION HISTORY", total_w)
    # Step 3: print rows
    for idx, t in enumerate(transactions, start=1):
        row = ( 
            f"{str(idx).ljust(no_w)} | "
            f"{t['type'].upper().ljust(type_w)} | "
            f"{('₹' + format(t['amount'], '.2f')).rjust(amount_w)} | "
            f"{t['reason'].ljust(reason_w)} | "
            f"{('₹' + format(t['balance_after'], '.2f')).rjust(balance_w)}"
        
        
        
        )
        print(row)

    # Step 4: footer line
    print("-" * total_w)

if __name__ == "__main__":
        main()