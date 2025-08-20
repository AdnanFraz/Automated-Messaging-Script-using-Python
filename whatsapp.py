
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Launch Chrome
chrome_options = Options()
chrome_options.add_argument("--user-data-dir=/Users/adnanfraz/Library/Application Support/Google/Chrome/Default")
driver = webdriver.Chrome(options=chrome_options)

# Open WhatsApp Web
driver.get("https://web.whatsapp.com/")

# ✅ Wait until search box is visible
wait = WebDriverWait(driver, 30)
search_box = wait.until(
    EC.presence_of_element_located((By.XPATH, '//div[@aria-label="Search input textbox"]'))
)

# ✅ Make sure no popup is blocking
time.sleep(2)

# ✅ Use JavaScript click instead of normal click
driver.execute_script("arguments[0].click();", search_box)

# Type a contact name (example: "Doctor")
search_box.send_keys("Yaseen")
search_box.send_keys(Keys.ENTER)

# ✅ Wait and send message
time.sleep(2)
message_box = wait.until(
    EC.presence_of_element_located((By.XPATH, '//div[@aria-label="Type a message"]'))
)

# message_box.click()
message_box.send_keys("Hola")
message_box.send_keys(Keys.ENTER)


message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
message_box.send_keys("Hello from Selenium!" + Keys.ENTER)

# send_button = driver.find_element(By.XPATH, '//span[@data-icon="send"]')
# send_button.click()

# print("Message sent successfully ✅")
print("✅ Message sent. Browser will stay open.")
input("Press ENTER here to close browser manually...")
driver.quit()
