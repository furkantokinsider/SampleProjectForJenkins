from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.product_page import ProductPage


class InventoryPage(BasePage):
    PRODUCT_NAME = (By.LINK_TEXT, "Sauce Labs Fleece Jacket")
    PAGE_TITLE = (By.XPATH, "//span[text()='Products']")

    def is_on_inventory_page(self):
        self.is_element_visible(self.PAGE_TITLE)
        return True

    def click_product(self):
        self.click_element(*self.PRODUCT_NAME)

        return ProductPage(self.driver)
