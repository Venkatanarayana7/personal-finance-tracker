def calculate_balance(transactions):
    balance = 0

    for transaction in transactions:
        if transaction["type"] == "deposit":
            balance += transaction["amount"]
        elif transaction["type"] == "withdraw":
            balance -= transaction["amount"]

    return balance

def add_transaction(transactions):
    transaction_type = input("Enter transaction type (deposit/withdraw): ").lower()
    amount = float(input("Enter amount: "))
    reason = input("Enter reason: ")

    if transaction_type == "withdraw":
        balance = calculate_balance(transactions)
        if amount > balance:
            print("Insufficient balance. Transaction cancelled.")
            return
        
    transaction = {
        "type": transaction_type,
        "amount": amount,
        "reason": reason
    }

    transactions.append(transaction)
    print("Transaction added successfully.")


def view_transactions(transactions):
    if not transactions:
        print("No transactions available.")
        return
    
    for i, transaction in enumerate(transactions, start=1):
        print(f"{i}.{transaction['type']} | {transaction['amount']} | {transaction['reason']}")


transactions = []

while True:
    print("\n1. Add Transaction")
    print("2. View Transactions")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_transaction(transactions)
    elif choice == "2":
        view_transactions(transactions)
    elif choice == "3":
        balance = calculate_balance(transactions)
        print("Current Balance:", balance)
    elif choice == "4":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Try again.")