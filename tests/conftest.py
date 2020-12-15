import pytest
from selenium import webdriver

from base.webdriverfactory import WebDriverFactory


@pytest.fixture()
def set_up():
    print('running method level setup')
    yield
    print('running method level teardown')


@pytest.fixture(scope='class')
def one_time_set_up(request, browser):
    print('running one time setup')
    # if browser == 'chrome':
    #     base_url = "https://courses.letskodeit.com/"
    #     driver = webdriver.Chrome(
    #             executable_path="C:\\Users\\rashe\\Documents\\AutomationFiles\\drivers\\chromedriver.exe")
    #     driver.maximize_window()
    #     driver.implicitly_wait(10)
    #     driver.get(base_url)
    #     print('running tests on chrome')
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one time tearDown")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")
