# Import the fixture function from the fixtures.py file in the parent directory
from selenium.webdriver.common.by import By
from utils.webdriver_utils import PageWait
from utils.webdriver_utils import init_webdriver_instance
from utils.webdriver_utils import WebDriverActions
from page_objects.google_pom import GoogleSearchPage


class TestSearch:
    # Use the fixture as a parameter in your test method
    def test_google_search(self, init_webdriver_instance):
        driver = init_webdriver_instance
        url = "https://www.google.com"
        text = "Selenium"
        web_action = WebDriverActions(driver)
        web_action.open_url(url)
        google_search_page = GoogleSearchPage(driver)
        google_search_page.perform_search(text)
        page_wait = PageWait(driver)
        page_wait.wait_for_page_title_to_contain(text)
        assert text in driver.title
