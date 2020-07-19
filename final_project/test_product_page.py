import pytest
from .pages.product_page import ProductPage



# @pytest.mark.need_review
# def test_user_can_add_product_to_basket(browser):
#     page = ProductPage(url="", browser)  # инициализируем объект Page Object
#     page.open()  # открываем страницу в браузере
#     page.should_be_add_to_cart_button()  # проверяем что есть кнопка добавления в корзину
#     page.add_product_to_cart()  # жмем кнопку добавить в корзину
#     page.should_be_success_message()  # проверяем что есть сообщение с нужным текстом
#     pass


@pytest.mark.need_review
def test_guest_can_add_product_to_basket():
    pass


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page():
    pass


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page():
    pass
