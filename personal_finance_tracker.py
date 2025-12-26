balance = 0 
transactions = []

def print_menu():
    print("\n---Personal Finance Tracker ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Transaction History")
    print("5. Exit")

def deposit(balance, transactions):
    amount = float(input("Enter deposit amount: "))
    reason = input("Enter reason: ")

    balance += amount

    transaction = {
        "type": "deposit", 
        "amount": amount, 
        "reason": reason
    }

    transactions.append(transaction)

    print("Deposit successful.")
    return balance


def withdraw(balance, transactions):
    amount = float(input("Enter withdrawal amount: "))

    if amount > balance:
        print("Insufficient balance. Withdrawal denied.")
        return balance
    
    reason = input("Enter reason: ")

    balance -= amount

    transaction = {
        "type": "withdraw", 
        "amount": amount, 
        "reason": reason
    }

    transactions.append(transaction)

    print("Withdrawal successful.")
    return balance

def show_balance(balance):
    print(f"Current Balance: ₹{balance}")

def show_transactions(transactions):
    if not transactions:
        print("No transactions found.")
        return 
    
    for i, t in enumerate(transactions, start=1):
        print(f"{i}. {t['type']} | ₹{t['amount']} | {t['reason']}")

while True:
    print_menu()
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        balance = deposit(balance, transactions)

    elif choice == "2":
        balance = withdraw(balance, transactions)
    
    elif choice == "3":
        show_balance(balance)

    elif choice == "4":
        show_transactions(transactions)

    elif choice == "5":
        print("Exiting .. Thank you!")
        break

    else:
        print("Ivalid choice. Try again.")



















