# pip install gspread oauth2client selenium pandas
# !wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
# !apt-get install -y ./google-chrome-stable_current_amd64.deb
# pip install selenium webdriver-manager
import time
import urllib.parse
import gspread
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from oauth2client.service_account import ServiceAccountCredentials

# ======================
# Google Sheets Setup
# ======================
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("doctor-469410-7312531c7123.json", scope)
client = gspread.authorize(creds)

# Open Google Sheet by name
# sheet = client.open("Doctors Outreach").sheet1
sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1cN85nU1JYUDc9EcKMty5mXogASbrvqQ1p8b3IT_SqFM/edit?usp=sharing").sheet1


# Convert sheet data to pandas dataframe
data = pd.DataFrame(sheet.get_all_records())

# ======================
# WhatsApp Web Automation
# ======================
# # Auto-manage ChromeDriver
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.get("https://web.whatsapp.com")
# input("👉 Scan QR code in WhatsApp Web, then press ENTER here...")

# Setup Chrome options
options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--headless")  # ❌ remove this if you need to scan QR manually
options.binary_location = "/usr/bin/google-chrome"

# Initialize driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://web.whatsapp.com")

input("👉 Scan QR code in WhatsApp Web, then press ENTER here...")

# Message Template
message_template = """Hello Doctor,
My name is Adnan Fraz, I’m a Computer Science student at IIT Patna and a web developer. I specialize in building modern, easy-to-manage websites.

Today, most patients look online before choosing a doctor. A professional website helps build trust, makes it easier for patients to find you, and allows them to learn about your services or even book appointments directly.

I’d be happy to create a website tailored to your practice and needs. Would you be open to a quick chat about this?

Best regards,
Adnan Fraz
"""

# Loop through doctors
for index, row in data.iterrows():
    name = row["Name"]
    phone = row["Phone"]  # must be in 0XXXXXXXXXX format

    message = message_template.format(name=name)
    text = urllib.parse.quote(message)
    url = f"https://web.whatsapp.com/send?phone={phone}&text={text}"

    driver.get(url)
    time.sleep(8)  # wait for chat to load

    try:
        send_btn = driver.find_element(By.XPATH, "//button[@aria-label='Send']")
        send_btn.click()
        print(f"✅ Message sent to {name} ({phone})")

        # Update Google Sheet (mark contacted)
        sheet.update_cell(index+2, data.columns.get_loc("Contacted")+1, "Yes")

    except:
        print(f"❌ Failed for {name} ({phone})")

    time.sleep(15)  # pause to avoid spam

driver.quit()
