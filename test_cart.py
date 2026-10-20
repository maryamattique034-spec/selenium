import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
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


def test_cart_workflow(driver):
    wait = WebDriverWait(driver, 10)

    # 1. Add a product
    add_button = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "add-to-cart-sauce-labs-backpack")
        )
    )
    add_button.click()

    # 2. Verify the cart count
    cart_badge = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "shopping_cart_badge")
        )
    )
    assert cart_badge.text == "1"

    # 3. Open the shopping cart
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # 4. Verify the product name
    product_name = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "inventory_item_name")
        )
    )
    assert product_name.text == "Sauce Labs Backpack"

    # 5. Verify the product price
    product_price = driver.find_element(
        By.CLASS_NAME, "inventory_item_price"
    )
    assert product_price.text == "$29.99"

    # 6. Remove the product
    driver.find_element(
        By.ID, "remove-sauce-labs-backpack"
    ).click()

    # 7. Verify the cart is empty
    cart_items = driver.find_elements(
        By.CLASS_NAME, "cart_item"
    )
    assert len(cart_items) == 0