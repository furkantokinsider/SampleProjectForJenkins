from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.cart_page import CartPage


class ProductPage(BasePage):
    PRODUCT_NAME = (By.XPATH, "//div[text()='Sauce Labs Fleece Jacket']")
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[contains(@id, 'add-to-cart')]")
    REMOVE_BUTTON = (By.XPATH, "//button[contains(@id, 'remove')]")
    CART_BUTTON = (By.ID, "shopping_cart_container")

    def is_on_right_product_page(self):
        self.is_element_visible(self.PRODUCT_NAME)
        return True

    def click_add_to_cart_button(self):
        self.click_element(*self.ADD_TO_CART_BUTTON)

    def is_product_added_to_cart(self):
        self.is_element_visible(self.REMOVE_BUTTON)
        return True

    def click_cart_button(self):
        self.click_element(*self.CART_BUTTON)

        return CartPage(self.driver)
