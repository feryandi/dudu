from __future__ import print_function
import pickle
import os.path
import util.credentials
from googleapiclient.discovery import build

SPREADSHEET_ID = '1CfW0mxAcCZujxRcAiHCCZ2eoTU5cKF0fUMnvRQfweUM'
RANGE_NAME = 'Master!A1:F'

SERVICE = build('sheets', 'v4', credentials=util.credentials.get_creds())
SHEET = SERVICE.spreadsheets()

def write_row(item):
    global SHEET
    values = [item]
    body = {
        'values': values
    }

    SHEET.values().append(spreadsheetId=SPREADSHEET_ID,
                          range=RANGE_NAME,
                          valueInputOption='USER_ENTERED',
                          body=body).execute()

def read_rows():
    global SHEET
    result = SHEET.values().get(spreadsheetId=SPREADSHEET_ID,
                                range=RANGE_NAME).execute()
    values = result.get('values', [])
    if not values:
        return None

    data = []
    for value in values[1:]:
        row = {}
        for idx, column in enumerate(values[0]):
            if idx > len(value) - 1:
                break
            row[column] = value[idx]
        data.append(row)

    return data
