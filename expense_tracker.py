import csv
from datetime import datetime

# Function to log an expense
def log_expense(amount, category, description):
    # Append a new expense to the CSV file
    with open('expenses.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now(), amount, category, description])  # Write the current date, amount, category, and description

# Function to generate the report
def generate_report():
    # Calculate and print the total expenses
    total = 0
    with open('expenses.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the first row (header, if present)
        for row in reader:
            try:
                total += float(row[1])  # Add the amount (column 2) to the total
            except ValueError:
                continue  # Skip rows with invalid data
    print(f'Total Expenses: ${total:.2f}')  # Print the total

# Example usage
log_expense(50, 'Groceries', 'Bought fruits and vegetables')  # Log a $50 grocery expense
log_expense(20, 'Transport', 'Bus fare')  # Log a $20 transport expense
generate_report()  # Generate and display the total
