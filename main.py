from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service


#https://sites.google.com/chromium.org/driver/
#https://googlechromelabs.github.io/chrome-for-testing/

# no need to install manually chrome driver , in latest version it will download it automatically acoording to your chrome
# service = Service(executable_path="/Users/macbookpro/Documents/django-celery-project/chromedriver")
# driver = webdriver.Chrome(service=service)


driver = webdriver.Chrome()

driver.get("https://www.google.com")

time.sleep(10)

driver.quit()