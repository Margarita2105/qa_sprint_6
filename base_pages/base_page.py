from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_visibility_of_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    def find_element_on_page(self, locator):
        return self.driver.find_element(*locator)

    def text_of_element(self, locator):
        text = self.driver.find_element(locator).text

        return text

    def click_on_element(self, locator):
        self.find_element_on_page(locator).click()

    def scroll(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_url(self, url):
        self.driver.get(url)

    def get_tab_and_switch(self):
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[1])
        return tabs

    def current_urls(self):
        return self.driver.current_url
