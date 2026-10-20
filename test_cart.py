from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_cart_workflow(logged_in_driver):
    wait = WebDriverWait(logged_in_driver, 10)

    # 1. Add a product
    add_button = wait.until(
        EC.element_to_be_clickable(
            (By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")
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
    logged_in_driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # 4. Verify the product name
    product_name = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//div[@class='cart_item']//div[@class='inventory_item_name']")
        )
    )
    assert product_name.text == "Test.allTheThings() T-Shirt (Red)"

    # 5. Verify the product price
    product_price = logged_in_driver.find_element(
        By.CLASS_NAME, "inventory_item_price"
    )
    assert product_price.text == "$15.99"

    # 6. Remove the product
    logged_in_driver.find_element(
        By.ID, "remove-test.allthethings()-t-shirt-(red)"
    ).click()

    # 7. Verify the cart is empty
    cart_items = logged_in_driver.find_elements(
        By.CLASS_NAME, "cart_item"
    )
    assert len(cart_items) == 0