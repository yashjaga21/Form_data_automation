import gspread
from oauth2client.service_account import ServiceAccountCredentials
import logging
import time
import random

logging.basicConfig(
    filename='form_data_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def authenticate_google_sheets():
    try:
        scope = ["https://spreadsheets.google.com/feeds",
                 "https://www.googleapis.com/auth/drive"]
        creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
        client = gspread.authorize(creds)
        logging.info("Google Sheets authentication successful.")
        return client
    except Exception as e:
        logging.error("Google Sheets authentication failed: %s", e)
        raise

def write_to_sheet(sheet, data):
    try:
        sheet.append_row(data)
        logging.info("Data added to Google Sheet: %s", data)
    except Exception as e:
        logging.error("Failed to write data to sheet: %s", e)
        raise

def get_form_data():
    names = ["Alice", "Bob", "Charlie", "Diana"]
    emails = ["alice@example.com", "bob@example.com", "charlie@example.com", "diana@example.com"]
    feedbacks = ["Great!", "Could be better.", "Loved it.", "Not bad."]
    index = random.randint(0, 3)
    return [names[index], emails[index], feedbacks[index]]

def main():
    try:
        client = authenticate_google_sheets()
        sheet = client.open("Form Responses").sheet1

        for _ in range(5):
            form_data = get_form_data()
            write_to_sheet(sheet, form_data)
            time.sleep(2)
    except Exception as e:
        logging.critical("Automation script failed: %s", e)

if __name__ == "__main__":
    main()
