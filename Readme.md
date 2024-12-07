# BudgetBuddy: Personalized Expense Tracker and Optimizer

BudgetBuddy is a lightweight MicroSaaS application designed to help individuals and students manage their expenses effortlessly. It provides a simple interface for logging expenses, setting budgets, and viewing analytics.

---

## Features
- **Daily Expense Logging:** Track expenses by category, amount, and date.
- **Budget Tracking:** Set a monthly budget and get alerted on overspending.
- **Analytics Dashboard:** View total spent, category-wise distribution, and trends.

---

## Setup Instructions
### Prerequisites
- Python 3.8 or higher
- `pip` (Python package manager)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/AdityaSrivastavDS/budgetbuddy-microsaas
   cd budgetbuddy-microsaas
   ```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Initialize the database:
```bash
python app.py
```

# Usage
## Commands

1. Add an Expense:
```bash
python app.py add_expense --category="Food" --amount=200 --date=2024-12-07
```

2. Set a Monthly Budget:
```bash
python app.py set_budget --amount=5000
```

3. View Analytics:
```bash
python app.py view_analytics
```

## Example Output

### Analytics:

```bash
Expense Analytics:
Total Spent: ₹2000
Budget: ₹5000
Category-wise Spending:
  Food: ₹1500
  Transport: ₹500
```

## View
![Project Demo Image](assets/demo.png)