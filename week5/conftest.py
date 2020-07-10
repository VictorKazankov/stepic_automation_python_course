import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en-gb',
                     help="Choose site language")
    parser.addoption('--browser', action='store', default='Chrome')


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser")
    browser = None
    if browser_name == "Chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "Firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    browser.implicitly_wait(20)
    link = change_languages(request)
    browser.get(link)
    yield browser
    print("\nquit browser..")
    browser.quit()


def change_languages(request):
    languare_name = request.config.getoption("language")
    if languare_name == 'ru':
        print("\nopen russian page")
        link = f'http://selenium1py.pythonanywhere.com/{languare_name}/'
    elif languare_name == 'en-gb':
        print("\nopen english page")
        link = f'http://selenium1py.pythonanywhere.com/{languare_name}/'
    else:
        raise pytest.UsageError("--languare_name should be ru, en-gb")
    return link
