from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    PRODUCT_NAME = (By.LINK_TEXT, "Sauce Labs Fleece Jacket")

    def verify_product_is_added(self):
        self.is_element_visible(self.PRODUCT_NAME)