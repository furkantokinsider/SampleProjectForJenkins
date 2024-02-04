from tests.base_test import BaseTest
from pages.landing_page import LandingPage


class TestCheckAddToCart(BaseTest):
    username = "standard_user"
    password = "secret_sauce"

    def test_check_add_to_cart(self):
        landing_page = LandingPage(self.driver)
        landing_page.enter_username(self.username)
        landing_page.enter_password(self.password)
        landing_page.click_login_button()





