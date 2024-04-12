import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Manages WebDriver instances based on the specified browser type
class WebDriverManager:
    def __init__(self, browser):
        if browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        else:
            raise ValueError(f"Unsupported browser: {browser}")

        self.driver.maximize_window()

    def __enter__(self):
        return self.driver

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.quit()


# Fixture to initialize a WebDriver instance for test classes
@pytest.fixture(scope="class")
def init_webdriver_instance(request):
    browser_option = request.config.getoption("--browser")
    if browser_option:
        selected_browser = browser_option
    else:
        selected_browser = "chrome"  # Default browser is Chrome
    with WebDriverManager(selected_browser) as driver:
        yield driver


# Helper class for waiting for page elements to load
class PageWait:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)  # Initialize WebDriverWait

    def wait_for_page_load(self):
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    def wait_for_page_title_to_contain(self, title):
        self.wait.until(EC.title_contains(title))


class WebDriverActions:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)
