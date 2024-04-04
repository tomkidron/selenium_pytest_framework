from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageWait:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def wait_for_page_load(self):
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    def wait_for_page_title_to_contain(self, title):
        self.wait.until(EC.title_contains(title))
