import pytest
from model.application import Application
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser type")
    parser.addoption("--base_url", action="store", default="http://strana-sovetov.com", help="base URL")


@pytest.fixture(scope="session")
def browser_type(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--base_url")

@pytest.fixture(scope="session")
def app(request, browser_type, base_url):
    if browser_type == "firefox":
        driver = webdriver.Firefox()
    elif browser_type == "chrome":
        driver = webdriver.Chrome()
        driver.set_window_size(1366, 768)
    elif browser_type == "ie":
        driver = webdriver.Ie()
    elif browser_type == "phantomjs":
        driver = webdriver.PhantomJS()
        driver.set_window_size(1120, 550)
    request.addfinalizer(driver.quit)
    return Application(driver, base_url)
