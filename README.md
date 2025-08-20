# 📩 WhatsApp Message Automation (Python + Selenium)

This project allows you to **send WhatsApp messages automatically** from an Excel file.  
It uses **Selenium** to control Chrome and WhatsApp Web.

---

## 🚀 Features
- Automatically open WhatsApp Web in Chrome.  
- Lets you scan the QR code once manually.  
- Reads contacts and messages from an Excel sheet.  
- Sends personalized messages to each contact.  
- Works on **Windows, macOS, and Linux**.  

---

## 📂 Project Structure
```
.
├── whatsapp.py   # Main script
├── contacts.xlsx # Excel file with contacts & messages
└── README.md     # Documentation
```

---

## 🛠️ Requirements

- Python 3.8 or later  
- Google Chrome (installed)  
- ChromeDriver (auto-managed by `webdriver_manager`)  

### Install dependencies:
```bash
pip install selenium webdriver-manager pandas openpyxl
```

---

## 📊 Excel File Format

Create an Excel file (e.g., `contacts.xlsx`) with at least two columns:

| Name    | Message              |
|---------|----------------------|
| Yaseen  | Hola                 |
| Adnan   | Good morning 🌞       |
| Fatima  | Don’t forget the call |

⚠️ **Column names must match exactly** (`Name`, `Message`).  

---

## ▶️ Usage

Run the script:

```bash
python whatsapp.py
```

Steps:
1. Chrome will open with WhatsApp Web.  
2. **Scan the QR code** with your WhatsApp mobile app (only needed the first time).  
3. The script will read the Excel file and start sending messages one by one.  
4. Console will print ✅ success messages.  

---

## 📝 Example Code Snippet

```python
import pandas as pd

# Load Excel file
data = pd.read_excel("contacts.xlsx")

for index, row in data.iterrows():
    contact_name = row["Name"]
    message = row["Message"]
    # Your selenium logic here to send
```

---

## ⚠️ Educational Purpose Advisory

This project is created **strictly for learning and personal automation purposes**.  

- Do **not** use this script to send bulk messages, spam, advertisements, or unsolicited content.  
- Automated messaging may violate **WhatsApp’s Terms of Service** and can lead to your number being **temporarily or permanently banned**.  
- Always use this responsibly, for example:
  - Sending reminders to yourself.  
  - Automating messages to a small group of friends/family with their **consent**.  
  - Exploring and learning how Selenium works with real-world websites.  

By using this script, **you accept full responsibility** for how it is used. The author(s) are **not liable** for any misuse.  

---

## 📌 To-Do / Improvements
- Add error handling if a contact is not found.  
- Add scheduling (send at specific times).  
- Support for attachments (images, PDFs).  
