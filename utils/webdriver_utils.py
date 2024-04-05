import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WebDriverManager:
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
    with WebDriverManager(browser) as driver:
        yield driver


class PageWait:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def wait_for_page_load(self):
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    def wait_for_page_title_to_contain(self, title):
        self.wait.until(EC.title_contains(title))


class WebDriverActions:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)
