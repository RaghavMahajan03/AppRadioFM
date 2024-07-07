import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxDriver
from selenium.webdriver.ie.service import Service as IEService
from selenium.webdriver.ie.webdriver import WebDriver as IEDriver

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = ChromeDriver(service=ChromeService(ChromeDriverManager().install()))
    elif browser_name == "firefox":
        driver = FirefoxDriver(service=FirefoxService(GeckoDriverManager().install()))
    elif browser_name == "IE":
        driver = IEDriver(service=IEService(IEDriverManager().install()))
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.implicitly_wait(10)
    driver.get("https://appradiofm.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()
