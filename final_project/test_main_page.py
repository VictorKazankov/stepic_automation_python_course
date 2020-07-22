import pytest

from .pages.main_page import MainPage
from .pages.login_page import LoginPage

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

# def test_guest_can_go_to_login_page(browser):
#     page = MainPage(browser,
#                     main_page_url)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#     page.open()  # открываем страницу
#     page.go_to_login_page()  # выполняем метод страницы - переходим на страницу логина
#     login_page = LoginPage(browser, browser.current_url)
#     login_page.should_be_login_page()
#
#
# def test_guest_should_see_login_link(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)
#     page.open()
#     page.should_be_login_link()
