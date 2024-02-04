import time

from tests.base_test import BaseTest
from pages.landing_page import LandingPage


class TestCheckAddToCart(BaseTest):
    username = "standard_user"
    password = "secret_sauce"

    def test_check_add_to_cart(self):
        landing_page = LandingPage(self.driver)
        assert landing_page.is_landing_successful(), "landing page has failed"
        landing_page.enter_username(self.username)
        landing_page.enter_password(self.password)

        inventory_page = landing_page.click_login_button()
        assert inventory_page.is_on_inventory_page(), "you are not in the inventory page"

        product_page = inventory_page.click_product()
        assert product_page.is_on_right_product_page(), "you are not in the right product page"
        product_page.click_add_to_cart_button()
        assert product_page.is_product_added_to_cart(), "adding the product to the cart has failed"

        cart_page = product_page.click_cart_button()
        assert cart_page.is_on_cart_page(), "you are not in the cart page"
        assert cart_page.verify_product_is_added(), "products do not match"





