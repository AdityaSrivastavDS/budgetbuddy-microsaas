import sqlite3
from budgetbuddy.models import DB_PATH

def add_expense(category, amount, date):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO expenses (category, amount, date) VALUES (?, ?, ?)", 
                       (category, amount, date))
        conn.commit()
    print(f"Expense added: {category} - ₹{amount} on {date}")

def set_budget(amount):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM budget")
        cursor.execute("INSERT INTO budget (amount) VALUES (?)", (amount,))
        conn.commit()
    print(f"Budget set to ₹{amount}")

def view_analytics():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()

        # Fetch total expenses
        cursor.execute("SELECT SUM(amount) FROM expenses")
        total_spent = cursor.fetchone()[0] or 0

        # Fetch category-wise spending
        cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
        categories = cursor.fetchall()

        # Fetch budget
        cursor.execute("SELECT amount FROM budget")
        budget = cursor.fetchone()

    print("\nExpense Analytics:")
    print(f"Total Spent: ₹{total_spent}")
    print(f"Budget: ₹{budget[0] if budget else 'Not Set'}")
    print("Category-wise Spending:")
    for category, amount in categories:
        print(f"  {category}: ₹{amount}")
