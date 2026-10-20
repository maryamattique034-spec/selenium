from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


#https://sites.google.com/chromium.org/driver/
#https://googlechromelabs.github.io/chrome-for-testing/

# no need to install manually chrome driver , in latest version it will download it automatically acoording to your chrome
# service = Service(executable_path="/Users/macbookpro/Documents/django-celery-project/chromedriver")
# driver = webdriver.Chrome(service=service)


driver = webdriver.Chrome()

driver.get("https://www.saucedemo.com/")

# Maximize browser window
driver.maximize_window()

print(driver.title)

# Find username field and enter username
username = driver.find_element(By.ID, "user-name")
username.send_keys("standard_user")


# Find password field and enter password
password = driver.find_element(By.ID, "password")
password.send_keys("secrett_sauce")


# Find login button and click it
login_button = driver.find_element(By.ID, "login-button")
login_button.click()

time.sleep(5)


# Find the error message with the CSS selector(attribute selector)
error_message = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")


# Verify that the error is displayed
assert error_message.is_displayed()


print("Error message is displayed:", error_message.text)

driver.quit()