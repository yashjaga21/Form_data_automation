# 📝 Form Data to Google Sheets Automation

This Python script simulates form submissions and syncs the data directly to a Google Sheet using the Google Sheets API.

## 🚀 Features
- Google Sheets integration
- Simulated form data
- Logging of operations and errors
- Retry and delay handling

## 📦 Requirements

- Python 3.x
- Google Sheets API credentials (as `credentials.json`)
- Required libraries:
  ```
  pip install -r requirements.txt
  ```

## 🔧 Setup
1. Create a project in [Google Developers Console](https://console.developers.google.com/).
2. Enable Google Sheets API.
3. Download the `credentials.json` file and place it in the project folder.
4. Share your sheet with the service account email from the credentials.

## ▶️ Run
```bash
python main.py
```

## ✅ Example Sheet Format
| Name   | Email              | Feedback        |
|--------|--------------------|-----------------|
| Alice  | alice@example.com  | Great!          |

---

Happy automating! 🔄
