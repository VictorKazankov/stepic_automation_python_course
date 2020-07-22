from final_project.pages.locators import ProductPageLocators
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
