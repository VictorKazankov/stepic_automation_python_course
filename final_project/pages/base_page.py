from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from final_project.pages.locators import GeneralLocators


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def open_basket(self):
        view_basket_button = self.get_element_present(*GeneralLocators.VIEW_BASKET_BUTTON)
        view_basket_button.click()

    def get_element_present(self, how, what):
        try:
            object = self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return object

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def go_to_login_page(self):
        link = self.browser.find_element(*GeneralLocators.LOGIN_LINK)
        link.click()

    def fill_field(self, field, text):
        field.click()
        field.clear()
        field.send_keys(text)