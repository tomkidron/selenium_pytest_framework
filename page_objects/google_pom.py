from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class GoogleSearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box_locator = "textarea[name='q']"
        self.search_button_locator = "input[name='btnK']"
        self.search_results_links_locator = "//div[@id='search']//h3"

    def perform_search(self, query):
        search_box = self.driver.find_element(By.CSS_SELECTOR, self.search_box_locator)
        search_box.clear()
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)

    def click_search_button(self):
        search_button = self.driver.find_element(
            By.CSS_SELECTOR, self.search_button_locator
        )
        search_button.click()

    def get_page_title(self):
        return self.driver.title

    def get_search_results_links_texts(self):
        return [
            link.text
            for link in self.driver.find_elements(
                By.XPATH, self.search_results_links_locator
            )
        ]
