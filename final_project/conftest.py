import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--language", action="store", default="ru")


def get_language_local_chrome(request):
    local = request.config.getoption("--language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': local})
    return options


def get_language_local_firefox(request):
    local = request.config.getoption("--language")
    fp = webdriver.FirefoxProfile()
    fp.set_preference("intl.accept_languages", local)
    return fp


def change_browser(request):
    browser_name = request.config.getoption("--browser")
    if browser_name == "chrome":
        br = webdriver.Chrome(options=get_language_local_chrome(request))
    elif browser_name == "firefox":
        br = webdriver.Firefox(firefox_profile=get_language_local_firefox(request))
    else:
        raise ValueError("Unrecognized browser {}".format(browser_name))
    return br


@pytest.fixture(scope="function")
def browser(request):
    print("\nstart chrome browser for test..")
    browser = change_browser(request)
    yield browser
    print("\nquit browser..")
    browser.quit()
