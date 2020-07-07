def test_is_exist_add_basket_button_on_product_page(browser):
    books_item_navigation_menu = browser.find_element_by_class_name("dropdown-submenu")
    books_item_navigation_menu.click()
    title_book = browser.find_element_by_css_selector("[title='Coders at Work']")
    title_book.click()
    add_busket_button = browser.find_element_by_id("add_to_basket_form")
    assert add_busket_button, 'Add busket button isnt displayed on page'
