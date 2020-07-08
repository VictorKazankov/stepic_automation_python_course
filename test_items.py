from week4.home_task.tests_user_registration.locators import BOOKS_ITEM_NAVIGATION_MENU_CLASS, \
    CODERS_WORK_BOOK_TITLE_CSS, ADD_BUSKET_BUTTON_ID


def test_is_exist_add_basket_button_on_product_page(browser):
    books_item_navigation_menu = browser.find_element_by_class_name(BOOKS_ITEM_NAVIGATION_MENU_CLASS)
    books_item_navigation_menu.click()
    title_book = browser.find_element_by_css_selector(CODERS_WORK_BOOK_TITLE_CSS)
    title_book.click()
    add_busket_button = browser.find_element_by_id(ADD_BUSKET_BUTTON_ID)
    assert add_busket_button, 'Add busket button isnt displayed on page'
