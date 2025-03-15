# Simple Expense Tracker
# This program allows users to track their daily expenses

expenses = []  # List to store all expenses

def add_expense():
    """Add a new expense"""
    print("\n=== Add New Expense ===")
    
    # Get expense details from user
    try:
        amount = float(input("Enter amount spent: $"))
        description = input("Enter a brief description: ")
        
        # Simple category selection
        print("\nCategories: 1. Food  2. Transportation  3. Entertainment  4. Other")
        category_num = input("Select category (1-4): ")
        
        # Convert category number to category name
        categories = ["Food", "Transportation", "Entertainment", "Other"]
        if category_num.isdigit() and 1 <= int(category_num) <= 4:
            category = categories[int(category_num) - 1]
        else:
            category = "Other"
        
        # Create and add expense
        expense = {
            "amount": amount,
            "description": description,
            "category": category
        }
        
        expenses.append(expense)
        print("Expense added successfully!")
    
    except ValueError:
        print("Invalid input! Please enter a valid number for amount.")

def view_expenses():
    """View all expenses"""
    print("\n=== Your Expenses ===")
    
    if not expenses:
        print("No expenses recorded yet.")
        return
    
    # Display all expenses
    print(f"{'No.':<4} {'Category':<15} {'Amount':<10} {'Description':<30}")
    print("-" * 59)
    
    for i, expense in enumerate(expenses, 1):
        print(f"{i:<4} {expense['category']:<15} ${expense['amount']:<9.2f} {expense['description']:<30}")
    
    # Calculate and show total
    total = sum(expense['amount'] for expense in expenses)
    print("-" * 59)
    print(f"Total: ${total:.2f}")

def category_summary():
    """Show summary by category"""
    print("\n=== Category Summary ===")
    
    if not expenses:
        print("No expenses recorded yet.")
        return
    
    # Calculate total for each category
    category_totals = {}
    for expense in expenses:
        category = expense['category']
        if category in category_totals:
            category_totals[category] += expense['amount']
        else:
            category_totals[category] = expense['amount']
    
    # Display category summary
    print(f"{'Category':<15} {'Amount':<10}")
    print("-" * 25)
    
    for category, amount in category_totals.items():
        print(f"{category:<15} ${amount:.2f}")
    
    # Calculate and show total
    total = sum(category_totals.values())
    print("-" * 25)
    print(f"Total: ${total:.2f}")

def main_menu():
    """Display main menu and get user choice"""
    print("\n=== Expense Tracker Menu ===")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Category Summary")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    return choice

# Main program
print("Welcome to Simple Expense Tracker!")

while True:
    choice = main_menu()
    
    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        category_summary()
    elif choice == '4':
        print("Thank you for using Expense Tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
