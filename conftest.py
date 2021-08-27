import pytest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from simple_settings import settings


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def environment_settings():
    return {"url": settings.BASE_URL}


@pytest.fixture(scope="session")
def setup(browser, environment_settings):
    driver = None
    if browser == "chrome":
        driver = webdriver.Chrome(
            executable_path=ChromeDriverManager().install()
        )
    elif browser == "firefox":
        driver = webdriver.Firefox(
            executable_path=GeckoDriverManager().install()
        )
    else:
        driver = webdriver.Chrome(
            executable_path=ChromeDriverManager().install()
        )
    driver.maximize_window()
    driver.get(environment_settings["url"])
    yield driver
    driver.quit()
