from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductPage(BasePage):
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[contains(@id, 'add-to-cart')]")
    REMOVE_BUTTON = (By.XPATH, "//button[contains(@id, 'remove')]")
    CART_BUTTON = (By.ID, "shopping_cart_container")

    def click_add_to_cart_button(self):
        self.click_element(*self.ADD_TO_CART_BUTTON)

    def assert_remove_button_is_visible(self):
        self.is_element_visible(self.REMOVE_BUTTON)

    def click_cart_button(self):
        self.click_element(*self.CART_BUTTON)

        return