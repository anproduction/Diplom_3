import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import allure
from pages.main_page import MainPage
from pages.feed_page import FeedPage
from pages.auth_page import AuthPage
from data import EXISTING_USER


@pytest.fixture(scope="function")
def main_page(browser):
    page = MainPage(browser)
    page.open_main_page()
    return page

@pytest.fixture(scope="function")
def feed_page(browser):
    return FeedPage(browser)


@pytest.fixture(scope="function")
def authorized_main_page(browser):
    auth_page = AuthPage(browser)
    main_page = MainPage(browser)
    feed_page = FeedPage(browser)

    auth_page.open("/login")
    with allure.step("Авторизация существующим пользователем"):
        auth_page.login(EXISTING_USER['email'], EXISTING_USER['password'])
    main_page.open_main_page()
    return main_page, feed_page


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("--browser")

    if browser_name == "chrome":
        options = ChromeOptions()
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
    else:
        raise ValueError("--browser must be chrome or firefox")

    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        if "browser" in item.fixturenames:
            web_driver = item.funcargs["browser"]
            allure.attach(web_driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
