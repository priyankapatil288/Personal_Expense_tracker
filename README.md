Personal Expense Tracker 
Overview
This Personal Expense Tracker is a Python-based command-line application designed to help users manage their monthly finances. The program allows users to record daily expenses, categorize them, set a monthly budget, and monitor their spending habits. All expenses are saved in a CSV file for easy access and future reference.
________________________________________
Features
•	Add Expense:
Users can input expenses with details such as date (validated in YYYY-MM-DD format), category, description, and amount (validated to ensure it is a positive number).
•	View Expenses:
Displays all recorded expenses in a readable format, showing the date, category, description, and amount for each entry.
•	Set and Track Monthly Budget:
Users can set a monthly budget. The tracker calculates the total expenses and compares them to the budget, warning if the budget is exceeded or showing the remaining balance.
•	Save Expenses:
All expenses are saved to a CSV file (expenses.csv), ensuring data persistence between sessions.
•	Load Expenses:
On startup, the program loads existing expenses from the CSV file, so users can continue tracking without losing previous data.
________________________________________
Input Validations
•	Date Validation:
Ensures the date is entered in the correct format (YYYY-MM-DD). Invalid dates prompt the user to re-enter.
•	Amount Validation:
Ensures the amount is a valid, non-negative number.
________________________________________
How It Works
1.	Startup:
The program loads any existing expenses from expenses.csv.
2.	Menu:
Users are presented with a menu to add expenses, view expenses, track budget, save expenses, or exit.
3.	Expense Entry:
When adding an expense, the program validates the date and amount before saving.
4.	Budget Tracking:
Users can set a monthly budget and check if their spending is within the limit.
5.	Saving Data:
Expenses can be saved at any time, and are automatically loaded the next time the program runs.
________________________________________
Benefits
•	Simple and User-Friendly:
The command-line interface is straightforward and easy to use.
•	Persistent Storage:
Data is stored in a CSV file, making it easy to view or edit outside the program if needed.
•	Financial Awareness:
By tracking expenses and comparing them to a set budget, users can develop better spending habits and avoid overspending.
________________________________________
Conclusion
This Personal Expense Tracker is a practical tool for anyone looking to manage their finances more effectively. With features like input validation, CSV storage, and budget tracking, it provides a solid foundation for personal financial management.

