import pytest

from final_project.pages.basket_page import BasketPage
from final_project.pages.login_page import LoginPage
from .pages.product_page import ProductPage

product_page_url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


class TestRegisteredUser():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        # create new user
        url = 'http://selenium1py.pythonanywhere.com/accounts/login/'
        login_page = LoginPage(browser, url)
        login_page.open()
        login_page.add_new_user()
        yield

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        product_page = ProductPage(browser, product_page_url)
        product_page.open()
        product_page.add_product_to_cart()
        product_page.should_be_success_message()


class TestUnregisteredUser():
    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser):
        product_page = ProductPage(browser, product_page_url)
        product_page.open()
        product_page.is_displayed_add_to_basket_button()
        product_page.add_product_to_cart()
        product_page.should_be_success_message()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        product_page = ProductPage(browser, product_page_url)
        product_page.open()
        product_page.open_basket()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_not_be_item_products()
        basket_page.should_be_empty_basket_text()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        product_page = ProductPage(browser, product_page_url)
        product_page.open()
        product_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_form()
        login_page.should_be_register_form()
