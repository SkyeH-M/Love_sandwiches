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

sales = SHEET.worksheet('sales')
data = sales.get_all_values()
print(data) # works
