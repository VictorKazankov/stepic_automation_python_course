import random

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert '/login/' in current_url

    def should_be_login_form(self):
        assert self.get_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.get_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def create_user_data(self):
        num = int(random.random() * 10000)
        mail_address = f"mymail{num}@mail.com"
        password = "21071976#ED2wsqwer"
        password_confirm = password
        return mail_address, password, password_confirm

    def add_new_user(self):
        mail, password, password_confirm = self.create_user_data()
        mail_field = self.get_element_present(*LoginPageLocators.MAIL_REGISTER_FIELD)
        password_field = self.get_element_present(*LoginPageLocators.PASSWORD_REGISTER_FIELD)
        password_confirm_field = self.get_element_present(*LoginPageLocators.PASSWORD_CONFIRM_REGISTER_FIELD)
        self.fill_field(mail_field, mail)
        self.fill_field(password_field, password)
        self.fill_field(password_confirm_field, password_confirm)
        registration_button = self.get_element_present(*LoginPageLocators.REGISTRATION_BUTTON)
        registration_button.click()
        # здесь не проверяем что пользователь добавился т.к. для этого есть отдельный тест
