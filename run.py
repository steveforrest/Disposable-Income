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

now = datetime.now()
date = now.month, now.year


def decide_function():
    """
    Choose new entry, output disposable income or output average
    disposable income
    """
    print(
        'Ensure you have clicked into the terminal before you try to input.')
    while True:
        user_choice = input("""
        If you would like to enter a new income entry please
        type 1 and press enter
        If you would like to enter a new expense entry please
        type 2 and press enter
        If you would like to see the total disposable income
        press 3 and then enter
        If you would like to see the disposable income for the
        latest month press 4 and then enter
        If you would like to see the average monthly disposable
        income please press 5 and then enter\n
        """)
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
    date = now.month, now.year
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
              f'Please enter a number, you entered {values}'
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
    main()


def add_entry_to_expense_worksheet(inputs):
    """
    Adds entry to expense worksheet
    """
    expense.append_row(inputs)
    print('Updating expense worksheet...\n')
    print('Worksheet updated...\n')
    main()


def checks_output_of_userInput(value):
    """
    checks whether income or expense which
    inputs two new columns to the worksheet
    """
    if value == '1':
        print(
            'You chose to update this months income')
        inputs = user_inputs()
        print('updating income')
        return add_entry_to_income_worksheet(inputs)
    elif value == '2':
        print(
            'You chose to update this months expense')
        inputs = user_inputs()
        print('updating Expenses')
        return add_entry_to_expense_worksheet(inputs)
    elif value == '3':
        print(
            'You chose to view your total disposable income')
        print('Your disposable income is:')
        return total_disposable()
    elif value == '4':
        print(
            'You chose to view your disposable income for this month')
        print('Your disposable income for current month is: ')
        return disposable_for_this_month()
    elif value == '5':
        print(
            'You chose to view your average disposable\n'
            'income over all of the months')
        print('Your average disposable income is:')
        return get_average_disposable_income()


def sum_income():
    """
    Checks all info in colum 1 to se if it matches current date time,
    if it does Sums all income entries for this month and returns a total.
    iterate over each entry to compare to current month, year then
    return value under amount colum and add to others
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
    finds disposable income by finding the difference
    for income and expense of comparable date
    """
    disposable = sum_income() - sum_expense()
    print(disposable)
    main()


def sum_income_for_date():
    """
    get the income list and pass through the lists
    where the [0] index is the same as todays date
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
    get the income list and pass through the lists where
    the [0] index is the same as todays date
    """
    expense_list = expense_data
    amount_expense = 0
    length = len(expense_list)
    for item in range(length):
        if expense_list[item][0] == str(date):
            amount_expense += int(expense_list[item][2])
    return amount_expense


def disposable_for_this_month():
    """
    Gets the amount of total income by deducting
    the summed income from the summed expenses
    """
    current_dsiposable = sum_income_for_date() - sum_expense_for_date()
    print(current_dsiposable)
    main()


def get_number_of_months_income():
    """
    returns how many different months there are in the income worksheet
    """
    how_many_months = int(1)
    length = len(income_data)
    i = 0
    income_data[i][0]
    while i < (length - 1):
        if (str(income_data[i][0])) != (str(income_data[i + 1][0])):
            how_many_months += int(1)
        i = i + 1
    return how_many_months


def get_number_of_months_expense():
    """
    returns how many different months there are in the income worksheet
    """
    how_many_months = int(1)
    length = len(expense_data)
    i = 0
    expense_data[i][0]
    while i < (length - 1):
        if (str(expense_data[i][0])) != (str(expense_data[i + 1][0])):
            how_many_months += int(1)
        i = i + 1
    return how_many_months


def more_month_income_or_expense():
    """
    determines which worksheet ahs the most months in it
    the income or expense and returns the amount from that one
    """
    higher_valeu = 0
    if (get_number_of_months_income()) >= (get_number_of_months_expense()):
        return get_number_of_months_income()
    else:
        return get_number_of_months_expense()


def get_average_disposable_income():
    """
    finds average disposable income rounded to 2 decimal place
    """
    diff = sum_income() - sum_expense()
    avg_disposable = diff / more_month_income_or_expense()
    avg_disposable = str(round(avg_disposable, 2))
    print(avg_disposable)
    main()


def main():
    """
    runs the main code
    """
    decide_function()

main()
