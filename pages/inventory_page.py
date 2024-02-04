from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.product_page import ProductPage


class InventoryPage(BasePage):
    PRODUCT_NAME = (By.LINK_TEXT, "Sauce Labs Fleece Jacket")

    def click_product(self):
        self.click_element(*self.PRODUCT_NAME)

        return ProductPage(self.driver)
