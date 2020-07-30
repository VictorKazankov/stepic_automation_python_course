import pytest

from final_project.pages.list_products_page import ListProductsPage
from .pages.main_page import MainPage

main_page_url = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.need_review_custom_scenarios
def test_is_displayed_login_or_register_link(browser):
    main_page = MainPage(browser, main_page_url)
    main_page.open()
    main_page.is_displayed_login_or_register_link()


@pytest.mark.need_review_custom_scenarios
def test_is_displayed_search_field(browser):
    main_page = MainPage(browser, main_page_url)
    main_page.open()
    main_page.is_displayed_search_field()


@pytest.mark.need_review_custom_scenarios
def test_is_displayed_navigation_menu(browser):
    main_page = MainPage(browser, main_page_url)
    main_page.open()
    main_page.is_displayed_navigation_menu()


@pytest.mark.need_review_custom_scenarios
def test_is_displayed_basket_button(browser):
    main_page = MainPage(browser, main_page_url)
    main_page.open()
    main_page.is_displayed_basket_button()


@pytest.mark.need_review_custom_scenarios
def test_open_all_products_page_via_navigation_menu(browser):
    main_page = MainPage(browser, main_page_url)
    main_page.open()
    main_page.open_all_products_list_on_navigation_menu()
    list_products_page = ListProductsPage(browser, browser.current_url)
    list_products_page.result_should_be_201_elements()


@pytest.mark.need_review_custom_scenarios
def test_result_find_book_by_search_field(browser):
    main_page = MainPage(browser, main_page_url)
    main_page.open()
    main_page.find_book()
    list_products_page = ListProductsPage(browser, browser.current_url)
    list_products_page.is_displayed_coders_at_work_book_name()
