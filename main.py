from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#https://sites.google.com/chromium.org/driver/
#https://googlechromelabs.github.io/chrome-for-testing/

# no need to install manually chrome driver , in latest version it will download it automatically acoording to your chrome
# service = Service(executable_path="/Users/macbookpro/Documents/django-celery-project/chromedriver")
# driver = webdriver.Chrome(service=service)


driver = webdriver.Chrome()


# Maximize browser window
driver.maximize_window()


# Create an explicit wait with a 10-second timeout
wait = WebDriverWait(driver, 10)


try:
    driver.get("https://www.saucedemo.com/")

    print(driver.title)

    # Find username field and enter username
    username = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
    username.send_keys("standard_user")


    # Find password field and enter password
    password = wait.until(EC.visibility_of_element_located((By.ID, "password")))
    password.send_keys("secret_sauce")


    # Find login button and click it
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    # Wait for products page heading
    heading = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "title")
        )
    )

    #Verify the results 
    assert heading.text == "Products"


    print("Login successful, heading is:", heading.text)

finally:

    driver.quit()