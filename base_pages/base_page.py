import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Задаем явное ожидание до видимости элемента на странице.')
    def wait_visibility_of_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Находим элемент на странице.')
    def find_element_on_page(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Находим элемент на странице и получаем его текст.')
    def text_of_element(self, locator):
        text = self.driver.find_element(*locator).text

        return text

    @allure.step('Находим элемент на странице и нажимаем на него.')
    def click_on_element(self, locator):
        self.find_element_on_page(locator).click()

    @allure.step('Скролим до элемента.')
    def scroll(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Вводим урл страницы на которую нужно перейти.')
    def get_url(self, url):
        self.driver.get(url)

    @allure.step('Переходим на открывшуюся страницу в новой вкладке.')
    def get_tab_and_switch(self):
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[1])
        return tabs

    @allure.step('Получаем урл текущей страницы.')
    def current_urls(self):
        return self.driver.current_url
