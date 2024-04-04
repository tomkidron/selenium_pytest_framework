import pytest
from selenium import webdriver


@pytest.fixture(
    scope="class", params=["chrome", "firefox"]
)  # List of supported browsers
def init_webdriver_instance(request: pytest.FixtureRequest):
    browser = request.param

    if browser == "chrome":
        driver = webdriver.Chrome()  # Chrome WebDriver
    elif browser == "firefox":
        driver = webdriver.Firefox()  # Firefox WebDriver
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()

    yield driver

    driver.quit()
