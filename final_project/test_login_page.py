import pytest

from final_project.pages.login_page import LoginPage

login_page_url = 'http://selenium1py.pythonanywhere.com/accounts/login/'


@pytest.mark.need_review_custom_scenarios
def test_open_login_page(browser):
    login_page = LoginPage(browser, login_page_url)
    login_page.open()
    login_page.should_be_login_form()
    login_page.should_be_register_form()
