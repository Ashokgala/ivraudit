from pprint import pprint


import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet1 = client.open("IVR Auto-Audit Dump")

data = sheet.get_all_records()

sheetID = '1FGBuqQEUse8IRoaVpsZX6QYYHy8sSHtpn4tXOO6mJSY'

# sheet_range = 'Sheet!A1:B3'


append = sheet.append_row(["a man", "a plan", "panama"])

print(append)



# values = result.get('Values', [])

# if not values:
#     print("No Data found")


# range = 'A1:B1'

# value_input_option = 'USER_ENTERED'

# insert_data_option = 'INSERT_ROWS'

# value_range_body = [["IVR NAME", "ITS PORPER"]]

# response = sheet.values().append(spreadsheetId=spreadsheet_id, range=range_, valueInputOption=value_input_option, insertDataOption=insert_data_option, body=value_range_body)
# response = request.execute()

# sheet2 = client.open("IVR Auto-Audit Dump") # Open the spreadhseet

        
# sheet = sheet2.worksheet("Sheet1")

