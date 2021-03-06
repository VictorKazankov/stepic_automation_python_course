from selenium.webdriver.common.by import By

name_book = "Coders at Work"

class MainPageLocators():
    SEARCH_FIELD = (By.ID, "id_q")
    NAVIGATION_MENU = (By.CSS_SELECTOR, "[data-navigation=dropdown-menu]")
    ALL_PRODUCT_ITEM = (By.XPATH, "//ul[@data-navigation='dropdown-menu']/li[1]")
    SEARCH_BUTTON = (By.XPATH, "//input[@type = 'submit']")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    MAIL_REGISTER_FIELD = (By.ID, "id_registration-email")
    PASSWORD_REGISTER_FIELD = (By.ID, 'id_registration-password1')
    PASSWORD_CONFIRM_REGISTER_FIELD = (By.ID, 'id_registration-password2')
    REGISTRATION_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.ID, "add_to_basket_form")
    SUCCESS_ADD_TO_BASKET_ALERT = (By.XPATH, "//div[@class='alertinner ']/*[contains(text(),'{}')]".format(name_book))
    VIEW_BASKET_BUTTON = (By.XPATH, "//span[@class='btn-group']/*[contains(@href, 'basket')]")
    LOGIN_LINK = (By.ID, "login_link")
    CODERS_AT_WORK_BOOK_NAME = (By.CSS_SELECTOR, ".product_main h1")


class BaskerPageLocators():
    BASKET_ITEMS = (By.CLASS_NAME, "basket-items")
    ITEM_EMPTY_TEXT = (By.ID, "content_inner")


class ListProductsPageLocators():
    ALL_PRODUCTS_NUMBER = (By.XPATH, "//strong[contains(text(),'201')]")
    CODERS_AT_WORK_BOOK = (By.XPATH, "//h3/a[contains(@href, 'coders-at-work_207')]")
