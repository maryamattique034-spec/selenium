import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.maximize_window()

    browser.get("https://www.saucedemo.com/")

    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()

    yield browser

    browser.quit()


def test_products_displayed(driver):
    products = driver.find_elements(By.CLASS_NAME, "inventory_item")

    assert len(products) == 6


def test_sort_products_by_price(driver):
    sort_dropdown = Select(
        driver.find_element(By.CLASS_NAME, "product_sort_container")
    )

    sort_dropdown.select_by_value("lohi")

    prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")

    price_values = [
        float(price.text.replace("$", ""))
        for price in prices
    ]

    assert price_values == sorted(price_values)


def test_add_product_to_cart(driver):
    add_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.ID, "add-to-cart-sauce-labs-backpack")
        )
    )
    add_button.click()

    cart_badge = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )

    assert cart_badge.text == "1"