from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_products_displayed(logged_in_driver):
    products = logged_in_driver.find_elements(By.CLASS_NAME, "inventory_item")

    assert len(products) == 6


def test_sort_products_by_price(logged_in_driver):
    sort_dropdown = Select(
        logged_in_driver.find_element(By.CLASS_NAME, "product_sort_container")
    )

    sort_dropdown.select_by_value("lohi")

    prices = logged_in_driver.find_elements(By.CLASS_NAME, "inventory_item_price")

    price_values = [
        float(price.text.replace("$", ""))
        for price in prices
    ]

    assert price_values == sorted(price_values)


def test_add_product_to_cart(logged_in_driver):
    add_button = WebDriverWait(logged_in_driver, 10).until(
        EC.element_to_be_clickable(
            (By.ID, "add-to-cart-sauce-labs-backpack")
        )
    )
    add_button.click()

    cart_badge = WebDriverWait(logged_in_driver, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )

    assert cart_badge.text == "1"