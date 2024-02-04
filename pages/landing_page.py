from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.inventory_page import InventoryPage


class LandingPage(BasePage):
    USERNAME_TEXTBOX = (By.ID, "user-name")
    PASSWORD_TEXTBOX = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input[name='login-button']")
    LOGIN_LOGO = (By.CLASS_NAME, "login_logo")

    def is_landing_successful(self):
        self.is_element_visible(self.LOGIN_LOGO)
        return True

    def enter_username(self, username):
        self.send_text(username, *self.USERNAME_TEXTBOX)

    def enter_password(self, password):
        self.send_text(password, *self.PASSWORD_TEXTBOX)

    def click_login_button(self):
        self.click_element(*self.LOGIN_BUTTON)

        return InventoryPage(self.driver)
