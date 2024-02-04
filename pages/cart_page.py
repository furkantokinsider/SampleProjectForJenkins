from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    CART_PAGE = (By.XPATH, "//span[text()='Your Cart']")
    PRODUCT_NAME = (By.LINK_TEXT, "Sauce Labs Fleece Jacket")

    def is_on_cart_page(self):
        self.is_element_visible(self.CART_PAGE)

    def verify_product_is_added(self):
        self.is_element_visible(self.PRODUCT_NAME)
