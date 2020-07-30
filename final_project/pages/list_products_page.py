from final_project.pages.base_page import BasePage
from final_project.pages.locators import ListProductsPageLocators


class ListProductsPage(BasePage):
    def result_should_be_201_elements(self):
        assert self.get_element_present(*ListProductsPageLocators.ALL_PRODUCTS_NUMBER), \
            "Count of all elements not equal 201"

    def is_displayed_coders_at_work_book_name(self):
        assert self.get_element_present(*ListProductsPageLocators.CODERS_AT_WORK_BOOK), \
            "Coders at work book isnt displayed"

    def open_coders_at_work_book(self):
        coders_at_work_book = self.get_element_present(*ListProductsPageLocators.CODERS_AT_WORK_BOOK)
        coders_at_work_book.click()
