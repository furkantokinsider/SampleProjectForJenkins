import unittest

from selenium import webdriver


class BaseTest(unittest.TestCase):
    base_url = 'https://www.saucedemo.com/'

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(20)
