# Import the fixture function from the fixtures.py file in the parent directory
from selenium.webdriver.common.by import By
from helper_functions import PageWait
from fixtures import init_webdriver_instance


class TestSearch:
    # Use the fixture as a parameter in your test method
    def test_google_search(self, init_webdriver_instance):
        driver = init_webdriver_instance
        url = "https://www.google.com"
        text = "Selenium"
        driver.get(url)
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys(text)
        search_box.submit()
        page_wait = PageWait(driver)
        page_wait.wait_for_page_title_to_contain(text)
        assert text in driver.title
