from .base_page import BasePage
from .locators import MainPageLocators, ProductPageLocators, name_book


class MainPage(BasePage):
    def is_displayed_login_or_register_link(self):
        assert self.get_element_present(*ProductPageLocators.LOGIN_LINK), "Login link is not presented"

    def is_displayed_search_field(self):
        assert self.get_element_present(*MainPageLocators.SEARCH_FIELD), "Search field is not presented"

    def is_displayed_navigation_menu(self):
        assert self.get_element_present(*MainPageLocators.NAVIGATION_MENU), "Navigation menu is not presented"

    def is_displayed_basket_button(self):
        assert self.get_element_present(*ProductPageLocators.VIEW_BASKET_BUTTON), "View basket button is not presented"

    def open_all_products_list_on_navigation_menu(self):
        all_products_item = self.get_element_present(*MainPageLocators.ALL_PRODUCT_ITEM)
        all_products_item.click()

    def find_book(self):
        search_field = self.get_element_present(*MainPageLocators.SEARCH_FIELD)
        self.fill_field(search_field, name_book)
        search_button = self.get_element_present(*MainPageLocators.SEARCH_BUTTON)
        search_button.click()
