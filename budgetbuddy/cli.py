import argparse
from budgetbuddy.models import init_db
from budgetbuddy.utils import add_expense, set_budget, view_analytics

def main():
    parser = argparse.ArgumentParser(description="BudgetBuddy: Manage your expenses effortlessly!")
    subparsers = parser.add_subparsers(dest="command")

    # Add Expense
    parser_add = subparsers.add_parser("add_expense")
    parser_add.add_argument("--category", required=True, help="Category of the expense")
    parser_add.add_argument("--amount", required=True, type=float, help="Amount spent")
    parser_add.add_argument("--date", required=True, help="Date of the expense (YYYY-MM-DD)")

    # Set Budget
    parser_budget = subparsers.add_parser("set_budget")
    parser_budget.add_argument("--amount", required=True, type=float, help="Monthly budget amount")

    # View Analytics
    subparsers.add_parser("view_analytics")

    args = parser.parse_args()

    if args.command == "add_expense":
        add_expense(args.category, args.amount, args.date)
    elif args.command == "set_budget":
        set_budget(args.amount)
    elif args.command == "view_analytics":
        view_analytics()
    else:
        init_db()
