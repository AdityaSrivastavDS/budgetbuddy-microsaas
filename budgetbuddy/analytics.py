import sqlite3
from budgetbuddy.models import DB_PATH

def get_total_expenses():
    """Calculate the total expenses."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT SUM(amount) FROM expenses")
        total_spent = cursor.fetchone()[0] or 0
    return total_spent

def get_category_wise_expenses():
    """Fetch category-wise spending."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
        category_spending = cursor.fetchall()
    return category_spending

def get_budget():
    """Retrieve the set budget."""
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT amount FROM budget")
        budget = cursor.fetchone()
    return budget[0] if budget else None

def display_analytics():
    """Display a summary of expenses and budget."""
    total_spent = get_total_expenses()
    category_spending = get_category_wise_expenses()
    budget = get_budget()

    print("\nExpense Analytics:")
    print(f"Total Spent: ₹{total_spent}")
    print(f"Budget: ₹{budget if budget else 'Not Set'}")
    print("Category-wise Spending:")
    for category, amount in category_spending:
        print(f"  {category}: ₹{amount}")

    if budget and total_spent > budget:
        print("\n⚠️ Warning: You have exceeded your budget!")
