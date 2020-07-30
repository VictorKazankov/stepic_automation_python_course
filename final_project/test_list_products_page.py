import pytest

from final_project.pages.list_products_page import ListProductsPage
from final_project.pages.product_page import ProductPage

list_products_page_url = 'http://selenium1py.pythonanywhere.com/catalogue/'


@pytest.mark.need_review_custom_scenarios
def test_open_product_page_from_list_page(browser):
    list_products_page = ListProductsPage(browser, list_products_page_url)
    list_products_page.open()
    list_products_page.open_coders_at_work_book()
    product_page = ProductPage(browser, browser.current_url)
    product_page.is_displayed_coders_at_work_book_name()
