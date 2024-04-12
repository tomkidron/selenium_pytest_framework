# Import the fixture function from the fixtures.py file in the parent directory
from selenium.webdriver.common.by import By
from utils.webdriver_utils import PageWait
from utils.webdriver_utils import init_webdriver_instance
from utils.webdriver_utils import WebDriverActions
from page_objects.google_pom import GoogleSearchPage


google_search_homepage_url = "https://www.google.com"


class TestSearch:
    # perform search on the google search homepage
    def test_google_search_functionality(self, request, init_webdriver_instance):
        driver = init_webdriver_instance
        query = request.config.getoption("--query")
        if query is None:
            query = "Selenium"
        web_action = WebDriverActions(driver)
        web_action.open_url(google_search_homepage_url)
        google_search_page = GoogleSearchPage(driver)
        google_search_page.perform_search(query)
        page_wait = PageWait(driver)
        page_wait.wait_for_page_title_to_contain(query)
        title = driver.title
        assert query in title
        links_texts = google_search_page.get_search_results_links_texts()
        assert len(links_texts) > 0
        lower_case_texts = {
            text.lower() for text in google_search_page.get_search_results_links_texts()
        }
        assert query.lower() in lower_case_texts

    # verify page title on the google search homepage
    def test_verify_google_homepage_title(self, init_webdriver_instance):
        driver = init_webdriver_instance
        web_action = WebDriverActions(driver)
        web_action.open_url(google_search_homepage_url)
        google_search_page = GoogleSearchPage(driver)
        assert google_search_page.get_page_title() == "Google"
