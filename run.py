# python code goes here
import gspread
from google.oauth2.service_account import Credentials

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

# print('income', income_data)
# print('expense', expense_data)

def decide_function():
    """
    Choose new entry, output disposable income or output average disposable income
    """
    while True:
        user_choice = input("""If you would like to enter a new entry please type 1 and press enter
    If you would like to see the disposable income for the latest month press 2 and then enter
    If you would like to see the average monthly dispoable income please press 3 and then enter\n"""
        )
        if validate_decide_function(user_choice):
            print(f'You selected {user_choice}')
            break

def validate_decide_function(values):
    """
    Validate whether a number is of 1 2 opr 3 is given only
    """
    try:
        if (int(values) < 1 or int(values) > 3):
            raise ValueError(
                f"Please enter a number between 1 and 3, you entered {values}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
    
    return True

  
    """
    user inputs date
    """


    """
    checks whether date is already in worksheet or not
    """

    """
    If date is already in worksheet add columns to end of row if not create new row
    """

    """
    checks whether income or expense which inputs two new columns to the worksheet
    """

    """
    Sums all entries for each month
    """

    """
    finds disposable income by finding the difference for income and expense of comparable date
    """

    """
    finds average disposable income
    """

    """
    outputs average disposable income
    """
decide_function()