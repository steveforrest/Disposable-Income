# python code goes here
import gspread
from google.oauth2.service_account import Credentials
import json
from datetime import datetime


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('Creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Disposable-Income')

income = SHEET.worksheet('Income')
expense = SHEET.worksheet('Expense')

income_data = income.get_all_values()
expense_data = expense.get_all_values()

list_of_dicts = income.get_all_records()
#print(list_of_dicts, '\n')
#income1 = income_data.col_values(1)
#print(income1)
#values_list = income.col_values('Income')(1)
#print(values_list)

#print(f'income', income_data)
#print('expense', expense_data)

now = datetime.now()
date = now.month,now.year

def decide_function():
    """
    Choose new entry, output disposable income or output average disposable income
    """
    while True:
        user_choice = input("""    If you would like to enter a new income entry please type 1 and press enter
    If you would like to enter a new expense entry please type 2 and press enter
    If you would like to see the total disposable income press 3 and then enter
    If you would like to see the disposable income for the latest month press 4 and then enter
    If you would like to see the average monthly dispoable income please press 5 and then enter\n"""
        )
        if validate_decide_function(user_choice):
            break
    checks_output_of_userInput(user_choice)

def validate_decide_function(values):
    """
    Validate whether a number is of 1 2 3 or 4 is given only
    """
    try:
        if (int(values) < 1 or int(values) > 5):
            raise ValueError(
                f"Please enter a number between 1 and 5, you entered {values}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    
    return True

def user_inputs():
    """
    user inputs date
    """
    
    now = datetime.now()
    date = now.month,now.year
    when = str(date)
    entry = input('Please enter a name of the entry: \n')
    while True:
        amount = input('Please enter an amount for your entry: \n')
        if validate_user_inputs(amount):
            break
    return [when, entry, amount]

def validate_user_inputs(values):
    """
    Validate whether a float number is given when asked for amount
    """
    try:
        if not(int(values) or float(values)):
            raise ValueError(
        f"Please enter a number, you entered {values}"
        )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False    
    return True

def add_entry_to_income_worksheet(inputs):
    """
    Adds entry to income worksheet
    """
    income.append_row(inputs)
    print('Updating income worksheet...\n')
    print('Worksheet updated...\n')

def add_entry_to_expense_worksheet(inputs):
    """
    Adds entry to expense worksheet
    """
    expense.append_row(inputs)
    print('Updating expense worksheet...\n')
    print('Worksheet updated...\n')



def checks_output_of_userInput(value):
    """
    checks whether income or expense which inputs two new columns to the worksheet
    """
    if value == '1':
        inputs = user_inputs()
        print('updating income')
        return add_entry_to_income_worksheet(inputs)
    elif value == '2':
        inputs = user_inputs()
        print('updating Expenses')
        return add_entry_to_expense_worksheet(inputs)
    elif value == '3':
        print('getting disposable income')
        return total_disposable()
    elif value == '4':
        print('getting disposable income for current month')
        return disposable_for_this_month()


def sum_income():
    """
    Checks all info in colum 1 to se if it matches current fate time, if it does 
    Sums all income entries for this month and returns a total.
    iterate over each entry to compare to current month, year then return value under amount colum and add to others
    get all results returned as a list 
    """
    income_list = income_data
    amount_income = 0
    length = len(income_list)
    for item in range(length):
        amount_income += int(income_list[item][2])
    return amount_income
      


def sum_expense():
    """
    Sums all expense entries for this month
    """
    expense_list = expense_data
    amount_expense = 0
    length = len(expense_list)
    for item in range(length):
        amount_expense += int(expense_list[item][2])
    return amount_expense

def total_disposable():
    """
    finds disposable income by finding the difference for income and expense of comparable date
    """
    disposable = sum_income() - sum_expense()
    print(disposable)

def sum_income_for_date():
    """
    get the income list and pass through the lists where the [0] index is the same as todays date
    """
    income_list = income_data
    amount_income = 0
    length = len(income_list)
    for item in range(length):
        if income_list[item][0] == str(date):
            amount_income += int(income_list[item][2])
    return amount_income

def sum_expense_for_date():
    """
    get the income list and pass through the lists where the [0] index is the same as todays date
    """
    expense_list = expense_data
    amount_expense = 0
    length = len(expense_list)
   
    for item in range(length):
        if expense_list[item][0] == str(date):
            amount_expense += int(expense_list[item][2])
    return amount_expense

def disposable_for_this_month():
    current_dsiposable = sum_income_for_date() - sum_expense_for_date()

   
    print(current_dsiposable)

def get_number_of_months_income():
    """
    returns how many different months there are in the income worksheet
    """
     income_list = income_data
    amount_income = 0
    length = len(income_list)
    for item in range(length):
        if income_list[item][0] == str(date):
            amount_income += int(income_list[item][2])
    return amount_income
    
    
def get_number_of_months_expense():
    """
    returns how many different months there are in the income worksheet
    """

#"""
#finds average disposable income
#"""


#"""
 #   outputs average disposable income
  #  """

def main():
    """
    runs the main code
    """
    decide_function()

#disposable_for_this_month()
#sum_income_for_date()
#sum_expense_for_date()
#main()
#sum_dates_income()
#sum_dates_expense()
#total_disposable()

disposable_for_this_month()