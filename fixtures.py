import pytest
from selenium import webdriver


class WebDriverFixture:
    def __init__(self, browser):
        if browser == "chrome":
            self.driver = webdriver.Chrome()  # Chrome WebDriver
        elif browser == "firefox":
            self.driver = webdriver.Firefox()  # Firefox WebDriver
        else:
            raise ValueError(f"Unsupported browser: {browser}")

        self.driver.maximize_window()

    def __enter__(self):
        return self.driver

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.quit()


@pytest.fixture(scope="class", params=["chrome", "firefox"])
def init_webdriver_instance(request: pytest.FixtureRequest):
    browser = request.param
    with WebDriverFixture(browser) as driver:
        yield driver
