import allure
from selenium import webdriver

from locators.scooter_dzen import Locators
from baseclass.button import Button
import urls


class TestScooterDzenPage:
    driver = None

    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера
        cls.driver = webdriver.Chrome()

    @allure.title('Нажимаем на логотип Самоката.')  # декораторы
    @allure.description(
        'На странице ищем логотип Самоката, нажимаем, переходим на главную страницу Самоката, получаем текущий урл, сравниваем текущий урл с урл главной страницей Самоката.')
    def test_press_scooter_logo(self):
        self.driver.get(urls.order_form)
        button = Button(self.driver)

        assert button.press_button(Locators.scooter, Locators.scooter_text) == urls.squter

    @allure.title('Проверяем редирект на Дзен, если нажать на логотип Яндекса.')  # декораторы
    @allure.description(
        'На странице ищем логотип Яндекса, нажимаем, переходим на открывшуюся страницу, ждем, когда появится элемент на странице, получаем урл окна, сравниваем урл окна с урл страницы Дзена.')
    def test_dzen_page(self):
        self.driver.get(urls.squter)
        button = Button(self.driver)
        url = button.press_logo(Locators.ya_logo, Locators.dzen)

        assert url == urls.dzen

    @classmethod
    def teardown_class(cls):
        # закрыли браузер
        cls.driver.quit()
