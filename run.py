# imports entire gspread library
import gspread
# imports Credentials class, part of service acc func from google auth lib
from google.oauth2.service_account import Credentials

# scope lists APIs program should access in order to run
# scope is constant so is written in capitals
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("love_sandwiches")

# CSV (comma separated values)
def get_sales_data():
    """ 
    Get sales figures input from the user
    """
    print("Please enter sales data from the last market.")
    print("Data should be 6 numbers, separated by commas.")
    print("Example: 10,20,30,40,50,60\n")

    data_str = input("Enter your data here: ")
    print(f"The data provided is {data_str}")

get_sales_data() # The data provided is {data_str}
