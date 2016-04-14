from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pytest

@pytest.fixture
def driver(request):
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    request.addfinalizer(driver.quit)
    return driver