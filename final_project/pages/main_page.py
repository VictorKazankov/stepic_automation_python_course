from .base_page import BasePage
from .locators import MainPageLocators, GeneralLocators


class MainPage(BasePage):
    def is_displayed_login_or_register_link(self):
        assert self.get_element_present(*GeneralLocators.LOGIN_LINK), "Login link is not presented"

    def is_displayed_search_field(self):
        assert self.get_element_present(*MainPageLocators.SEARCH_FIELD), "Search field is not presented"

    def is_displayed_navigation_menu(self):
        assert self.get_element_present(*MainPageLocators.NAVIGATION_MENU), "Navigation menu is not presented"

    def is_displayed_basket_button(self):
        assert self.get_element_present(*GeneralLocators.VIEW_BASKET_BUTTON), "View basket button is not presented"



    # def should_be_login_link(self):
    #     assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
