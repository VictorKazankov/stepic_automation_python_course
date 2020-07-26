import random


def create_user_data():
    num = int(random.random() * 10000)
    mail_address = f"mymail{num}@mail.com"
    password = "21071976#ED2ws"
    password_confirm = password
    return mail_address, password, password_confirm


def fill_field(browser, locator, value):
    email_field = browser.find_element_by_id(locator)
    email_field.clear()
    email_field.send_keys(value)
