from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class Base:

    def __init__(self, driver):
        self.driver = driver

    def wait(self, loc):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(loc))

    def text(self, loc):
        text = self.driver.find_element(*loc).text

        return text
