import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help="Choose site language")


@pytest.fixture(scope="function")
def browser(request):
    print("\nstart chrome browser for test..")
    browser = webdriver.Chrome()
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
    elif languare_name == 'es':
        print("\nopen spanish page")
        link = f'http://selenium1py.pythonanywhere.com/{languare_name}/'
    elif languare_name == 'fr':
        print("\nopen france page")
        link = f'http://selenium1py.pythonanywhere.com/{languare_name}/'
    else:
        raise pytest.UsageError("--languare_name should be es,ru,fr or en-gb")
    return link
