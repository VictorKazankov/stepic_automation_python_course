from final_project.pages.locators import ProductPageLocators, name_book
from .base_page import BasePage


class ProductPage(BasePage):
    def is_displayed_add_to_basket_button(self):
        assert self.get_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), \
            "Add to basket button is not presented"

    def add_product_to_cart(self):
        self.get_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def should_be_success_message(self):
        assert self.get_element_present(*ProductPageLocators.SUCCESS_ADD_TO_BASKET_ALERT), \
            "Product is not add to basket"

    def open_basket(self):
        view_basket_button = self.get_element_present(*ProductPageLocators.VIEW_BASKET_BUTTON)
        view_basket_button.click()

    def go_to_login_page(self):
        link = self.browser.find_element(*ProductPageLocators.LOGIN_LINK)
        link.click()

    def is_displayed_coders_at_work_book_name(self):
        book_locator = self.get_element_present(*ProductPageLocators.CODERS_AT_WORK_BOOK_NAME)
        assert name_book == book_locator.text

