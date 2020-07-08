from week4.home_task.tests_user_registration.helpers import create_user_data, fill_field
from week4.home_task.tests_user_registration.locators import EMAIL_REGISTRATION_FIELD_ID, \
    PASSWORD_REGISTRATION_FIELD_ID, PASSWORD_CONFIRM_REGISTRATION_FIELD_ID, REGISTRATION_BUTTON_NAME, \
    CONFIRM_REGISTRATION_ALERT_NAME, LOGIN_LINK_ID


def test_user_registration(browser):

    value_mail_address, value_password = create_user_data()

    login_link = browser.find_element_by_id(LOGIN_LINK_ID)
    login_link.click()

    fill_field(browser, EMAIL_REGISTRATION_FIELD_ID, value_mail_address)
    fill_field(browser, PASSWORD_REGISTRATION_FIELD_ID, value_password)
    fill_field(browser, PASSWORD_CONFIRM_REGISTRATION_FIELD_ID, value_password)

    registration_button = browser.find_element_by_name(REGISTRATION_BUTTON_NAME)
    registration_button.click()

    assert browser.find_element_by_class_name(CONFIRM_REGISTRATION_ALERT_NAME)






