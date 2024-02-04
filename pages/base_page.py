from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def click_element(self, *locator):
        self.find_element(*locator).click()

    def send_text(self, text, *locator):
        self.find_element(*locator).send_keys(text)

    def is_element_visible(self, locator):
        self.wait.until(ec.visibility_of_element_located(locator))
