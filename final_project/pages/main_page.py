from .base_page import BasePage
from .locators import MainPageLocators, ProductPageLocators


class MainPage(BasePage):
    def is_displayed_login_or_register_link(self):
        assert self.get_element_present(*ProductPageLocators.LOGIN_LINK), "Login link is not presented"

    def is_displayed_search_field(self):
        assert self.get_element_present(*MainPageLocators.SEARCH_FIELD), "Search field is not presented"

    def is_displayed_navigation_menu(self):
        assert self.get_element_present(*MainPageLocators.NAVIGATION_MENU), "Navigation menu is not presented"

    def is_displayed_basket_button(self):
        assert self.get_element_present(*ProductPageLocators.VIEW_BASKET_BUTTON), "View basket button is not presented"
