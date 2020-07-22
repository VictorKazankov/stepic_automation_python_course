from final_project.pages.base_page import BasePage
from final_project.pages.locators import BaskerPageLocators


class BasketPage(BasePage):
    def should_not_be_item_products(self):
        assert self.is_not_element_present(*BaskerPageLocators.BASKET_ITEMS), \
            "Item product is presented, but should not be"

    def should_be_empty_basket_text(self):
        assert self.get_element_present(*BaskerPageLocators.ITEM_EMPTY_TEXT)
