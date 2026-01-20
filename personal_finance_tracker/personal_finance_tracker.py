"""
Personal Finance Tracker v3.0 - FINAL VERSION
Developer: Guvvala Venkata Narayana
Date: January 20, 2026
Purpose: Professional personal finance management with complete data persistence
"""

import json
from datetime import datetime

# Configuration Constants
BASE_WIDTH = 120
balance = 0
transactions = [] 
AUTHOR_NAME = "Guvvala Venkata Narayana"
PROJECT_NAME = "Personal Finance Tracker"
VERSION = "v3.0"
YEAR = "2026"

# File paths
BALANCE_FILE = "balance.txt"
TRANSACTIONS_FILE = "transactions.json"
REPORT_FILE = "transaction_report.txt"


# ==================== UTILITY FUNCTIONS ====================

def center_text(text, width):
    """Center text within given width"""
    return text.center(width)


def show_section_title(title, width):
    """Display section title with decorative borders"""
    print("\n" + f" {title} ".center(width, "-"))


def get_valid_amount():
    """Get and validate amount input from user"""
    while True:    
        try:
            amount = float(input("Enter amount: "))
            if amount <= 0:
                print("❌ Amount must be greater than zero.")
                continue
            return amount
        except ValueError:
            print("❌ Invalid input. Please enter a numeric value.")


def can_withdraw(amount):
    """Check if withdrawal amount is available in balance"""
    return balance >= amount


# ==================== FILE OPERATIONS ====================

def save_balance():
    """Save current balance to file"""
    try:
        with open(BALANCE_FILE, "w") as file:
            file.write(str(balance))
        print("✅ Balance saved")
    except Exception as e:
        print(f"❌ Error saving balance: {e}")


def load_balance():
    """Load balance from file at program startup"""
    global balance
    try:
        with open(BALANCE_FILE, "r") as file:
            balance = float(file.read().strip())
        print(f"✅ Loaded balance: ₹{balance:.2f}")
    except FileNotFoundError:
        balance = 0
        print("ℹ️ No previous balance found. Starting fresh!")
    except Exception as e:
        balance = 0
        print(f"❌ Error loading balance: {e}")


def save_transactions():
    """Save all transactions to JSON file"""
    try:
        with open(TRANSACTIONS_FILE, "w") as file:
            json.dump(transactions, file, indent=4)
        print("✅ Transactions saved")
    except Exception as e:
        print(f"❌ Error saving transactions: {e}")


def load_transactions():
    """Load all transactions from JSON file at startup"""
    global transactions
    try:
        with open(TRANSACTIONS_FILE, "r") as file:
            transactions = json.load(file)
        print(f"✅ Loaded {len(transactions)} transactions")
    except FileNotFoundError:
        transactions = []
        print("ℹ️ No previous transactions found. Starting fresh!")
    except Exception as e:
        transactions = []
        print(f"❌ Error loading transactions: {e}")


# ==================== TRANSACTION MANAGEMENT ====================

def create_transaction(transaction_type, amount, reason, balance):
    """Create and save a new transaction"""
    # Use 12-hour format with AM/PM
    timestamp = datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")
    
    transaction = {
        "timestamp": timestamp,
        "type": transaction_type,
        "amount": amount, 
        "reason": reason, 
        "balance_after": balance
    }
    
    transactions.append(transaction)
    print("✅ Transaction added successfully")
    save_transactions()


def deposit_money():
    """Handle deposit transactions"""
    global balance
    
    show_section_title("➕ DEPOSIT MONEY", BASE_WIDTH)
    amount = get_valid_amount()
    
    reason = input("Enter reason for deposit: ").strip()
    if not reason:
        print("❌ Reason required")
        return
    
    balance += amount
    create_transaction("deposit", amount, reason, balance)
    print(f"✅ Deposit successful! Current balance: ₹{balance:.2f}")
    save_balance()


def withdraw_money():
    """Handle withdrawal transactions with validation"""
    global balance
    
    show_section_title("➖ WITHDRAW MONEY", BASE_WIDTH)
    amount = get_valid_amount()
    
    # Check balance BEFORE asking for reason
    if not can_withdraw(amount):
        print(f"❌ Insufficient balance!")
        print(f"   Requested: ₹{amount:.2f}")
        print(f"   Available: ₹{balance:.2f}\n")
        return
    
    # Only ask for reason if withdrawal is possible
    reason = input("Enter reason for withdrawal: ").strip()
    if not reason:
        print("❌ Reason required")
        return
    
    balance -= amount
    create_transaction("withdraw", amount, reason, balance)
    print(f"✅ Withdrawal successful! Current balance: ₹{balance:.2f}")
    save_balance()


# ==================== DISPLAY FUNCTIONS ====================

def show_balance():
    """Display current available balance"""
    show_section_title("💰 CURRENT BALANCE", BASE_WIDTH)
    print(center_text(f"Available Balance: ₹{balance:.2f}", BASE_WIDTH))


def calculate_column_widths(transactions):
    """Calculate optimal column widths for table display"""
    no_width = len("No")
    timestamp_width = len("Date & Time")
    type_width = len("Type")
    amount_width = len("Amount")
    reason_width = len("Reason")
    balance_width = len("Balance After")
    
    for idx, t in enumerate(transactions, start=1):
        no_width = max(no_width, len(str(idx)))
        timestamp_width = max(timestamp_width, len(t.get('timestamp', 'N/A')))
        type_width = max(type_width, len(t['type'].upper()))
        amount_width = max(amount_width, len(f"₹{t['amount']:.2f}"))
        reason_width = max(reason_width, len(t['reason']))
        balance_width = max(balance_width, len(f"₹{t['balance_after']:.2f}"))
    
    return no_width, timestamp_width, type_width, amount_width, reason_width, balance_width


def print_table_header(no_width, timestamp_width, type_width, amount_width, reason_width, balance_width):
    """Print formatted table header"""
    total_width = no_width + timestamp_width + type_width + amount_width + reason_width + balance_width + 18
    
    print("-" * total_width)
    
    header = (f"{'No'.ljust(no_width)} | "
              f"{'Date & Time'.ljust(timestamp_width)} | "
              f"{'Type'.ljust(type_width)} | "
              f"{'Amount'.rjust(amount_width)} | " 
              f"{'Reason'.ljust(reason_width)} | "
              f"{'Balance After'.rjust(balance_width)}")
    
    print(header)
    print("-" * total_width)
    
    return total_width


def print_transactions(transactions):
    """Display all transactions in formatted table"""
    if not transactions:
        print("\nℹ️ No transactions found.")
        return
    
    # Calculate column widths
    no_w, timestamp_w, type_w, amount_w, reason_w, balance_w = calculate_column_widths(transactions)
    
    # Print table header
    total_w = print_table_header(no_w, timestamp_w, type_w, amount_w, reason_w, balance_w)
    show_section_title("📊 TRANSACTION HISTORY", total_w)
    
    # Print each transaction row
    for idx, t in enumerate(transactions, start=1):
        timestamp = t.get('timestamp', 'N/A')
        row = (f"{str(idx).ljust(no_w)} | "
               f"{timestamp.ljust(timestamp_w)} | "
               f"{t['type'].upper().ljust(type_w)} | "
               f"{('₹' + format(t['amount'], '.2f')).rjust(amount_w)} | "
               f"{t['reason'].ljust(reason_w)} | "
               f"{('₹' + format(t['balance_after'], '.2f')).rjust(balance_w)}")
        print(row)
    
    # Print footer
    print("-" * total_w)
    
    # Display statistics
    total_deposits = sum(t['amount'] for t in transactions if t['type'] == 'deposit')
    total_withdrawals = sum(t['amount'] for t in transactions if t['type'] == 'withdraw')
    
    print(f"\n📈 Total Deposits: ₹{total_deposits:.2f}")
    print(f"📉 Total Withdrawals: ₹{total_withdrawals:.2f}")
    print(f"💰 Current Balance: ₹{balance:.2f}")


# ==================== SEARCH FUNCTIONALITY ====================

def search_transactions():
    """Search transactions by reason keyword or type"""
    # Check if transactions exist
    if not transactions:
        print("\n❌ No transactions available to search!")
        print("   Please add some transactions first.\n")
        return
    
    show_section_title("🔍 SEARCH TRANSACTIONS", BASE_WIDTH)
    
    print("\nSearch by:")
    print("1. Reason (keyword)")
    print("2. Type (deposit/withdraw)")
    
    choice = input("\nChoose (1-2): ").strip()
    
    if choice == "1":
        keyword = input("Enter keyword to search in reasons: ").strip().lower()
        results = [t for t in transactions if keyword in t['reason'].lower()]
    elif choice == "2":
        trans_type = input("Enter type (deposit/withdraw): ").strip().lower()
        results = [t for t in transactions if t['type'] == trans_type]
    else:
        print("❌ Invalid choice! Please enter only 1 or 2")
        return
    
    if results:
        print(f"\n✅ Found {len(results)} matching transactions:")
        print_transactions(results)
    else:
        print("\nℹ️ No matching transactions found.")


# ==================== EXPORT FUNCTIONALITY ====================

def export_to_text():
    """Export all transactions to a readable text report"""
    try:
        with open(REPORT_FILE, "w") as file:
            file.write("=" * 60 + "\n")
            file.write("PERSONAL FINANCE TRACKER - TRANSACTION REPORT\n")
            file.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')}\n")
            file.write("=" * 60 + "\n\n")
            
            file.write(f"Current Balance: ₹{balance:.2f}\n")
            file.write(f"Total Transactions: {len(transactions)}\n\n")
            
            if transactions:
                for idx, t in enumerate(transactions, start=1):
                    file.write(f"\nTransaction #{idx}\n")
                    file.write(f"  Date/Time: {t.get('timestamp', 'N/A')}\n")
                    file.write(f"  Type: {t['type'].upper()}\n")
                    file.write(f"  Amount: ₹{t['amount']:.2f}\n")
                    file.write(f"  Reason: {t['reason']}\n")
                    file.write(f"  Balance After: ₹{t['balance_after']:.2f}\n")
            else:
                file.write("\nNo transactions to export.\n")
            
            file.write("\n" + "=" * 60 + "\n")
            file.write(f"Report by: {AUTHOR_NAME}\n")
            file.write("=" * 60 + "\n")
        
        print(f"\n✅ Report exported successfully to '{REPORT_FILE}'")
    except Exception as e:
        print(f"\n❌ Error exporting report: {e}")


# ==================== UI FUNCTIONS ====================

def show_menu():
    """Display main menu options"""
    print("".center(BASE_WIDTH, "="))
    print(center_text("💳 PERSONAL FINANCE TRACKER 💳", BASE_WIDTH))
    print("".center(BASE_WIDTH, "="))
    print(center_text("1. ➕ Deposit Money", BASE_WIDTH))
    print(center_text("2. ➖ Withdraw Money", BASE_WIDTH))
    print(center_text("3. 💰 Show Balance", BASE_WIDTH))
    print(center_text("4. 📊 Show Transactions", BASE_WIDTH))
    print(center_text("5. 🔍 Search Transactions", BASE_WIDTH))
    print(center_text("6. 📁 Export Report", BASE_WIDTH))
    print(center_text("7. 🚪 Exit", BASE_WIDTH))
    print("".center(BASE_WIDTH, "="))


def show_app_header(width):
    """Display application header"""
    print("\n" + "=" * width)
    print(center_text("🏦 RGUKT BANK 🏦", width))
    print(center_text(PROJECT_NAME, width))
    print(center_text(f"Version: {VERSION}", width))
    print(center_text("Secure • Simple • Student-Friendly", width))
    print(center_text(f"Developed by {AUTHOR_NAME}", width))
    print("=" * width + "\n")


def show_exit_footer(width):
    """Display exit message"""
    print("\n" + "-" * width)
    print(center_text("✅ All data saved successfully!", width))
    print(center_text("Thank you for using Personal Finance Tracker", width))
    print(center_text("Built with Python • Learning by Building", width))
    print(center_text(f"© {YEAR} {AUTHOR_NAME}", width))
    print("-" * width + "\n")


# ==================== MAIN PROGRAM ====================

def main():
    """Main program control flow"""
    show_app_header(BASE_WIDTH)
    load_balance()
    load_transactions()
    
    while True:
        show_menu()
        choice = input("\nEnter your choice (1-7): ").strip()
        
        if choice == "1":
            deposit_money()
        elif choice == "2":
            withdraw_money()
        elif choice == "3":
            show_balance()
        elif choice == "4":
            print_transactions(transactions)
        elif choice == "5":
            search_transactions()
        elif choice == "6":
            export_to_text()
        elif choice == "7":
            show_exit_footer(BASE_WIDTH)
            break
        else:
            print("\n❌ Invalid choice. Please enter a number between 1 and 7.\n")


if __name__ == "__main__":
    main()