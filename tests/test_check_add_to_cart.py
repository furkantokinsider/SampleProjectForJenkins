import time

from tests.base_test import BaseTest
from pages.landing_page import LandingPage


class TestCheckAddToCart(BaseTest):
    username = "standard_user"
    password = "secret_sauce"

    def test_check_add_to_cart(self):
        landing_page = LandingPage(self.driver)
        landing_page.is_landing_successful()
        landing_page.enter_username(self.username)
        time.sleep(2)
        landing_page.enter_password(self.password)
        time.sleep(2)

        inventory_page = landing_page.click_login_button()
        time.sleep(2)

        product_page = inventory_page.click_product()
        time.sleep(2)
        product_page.click_add_to_cart_button()
        time.sleep(2)

        cart_page = product_page.click_cart_button()
        time.sleep(2)
        cart_page.verify_product_is_added()





