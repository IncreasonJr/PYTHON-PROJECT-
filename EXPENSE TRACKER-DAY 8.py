import csv
class ExpenseTracker:
    def __init__(self):
        self.expenses =[]
        self.filename = "expenses.csv" 
        try:
            with open(self.filename, 'x', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Expense", "Amount"])
        except FileExistsError:
            pass
        self.load_expenses()

    def add_expense(self):
        expense = input('Type of expense(e.g., Food, Transport): ')
        try:
            amount = float(input('Amount spent: '))
            self.expenses.append([expense, amount])
            self.save_expenses()
            print("Expense added successfully!")
        except ValueError:
            print("Invalid amount. Please enter a number.")
            return
        
    def load_expenses(self):
        try:
            with open(self.filename, 'r', newline='') as f:
                reader = csv.reader(f)
                next(reader, None)  # skip header
                self.expenses = [[row[0], float(row[1])] for row in reader if row]
        except Exception as e :
            print(f"Error loading expenses: {type(e).__name__}: {e}")
            self.expenses = []


    def save_expenses(self):
        with open(self.filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Expense", "Amount"])
            for exp, amt in self.expenses:
                writer.writerow([exp, amt])        
    
        
    def view_expense(self):
        if not self.expenses:
            print("No expenses recorded.")
        else:
            print("Here are your recorded expenses:")
            for expense, amount in self.expenses:
                print(f"Expense: {expense}, Amount: {amount:.2f}")

    def main(self):
        while True:
            print("\nExpense Tracker Menu:")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Exit")
            choice = input("Choose an option (1-3): ")
            if choice == '1':
                self.add_expense()
            elif choice == '2':
                self.view_expense()
            elif choice == '3':
                print("Exiting Expense Tracker. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")

main = ExpenseTracker()
main.main()