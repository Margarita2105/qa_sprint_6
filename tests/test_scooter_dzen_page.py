import allure
from selenium import webdriver

from locators.scooter_dzen import Locators
from base_pages.button_page import ButtonPage
import urls


class TestScooterDzenPage:
    driver = None

    @allure.step('Открываем браузер Chrome')
    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера
        cls.driver = webdriver.Chrome()

    @allure.title('Нажимаем на логотип Самоката.')  # декораторы
    @allure.description(
        'На странице ищем логотип Самоката, нажимаем, переходим на главную страницу Самоката, получаем текущий урл, сравниваем текущий урл с урл главной страницей Самоката.')
    def test_press_scooter_logo(self):
        button = ButtonPage(self.driver)
        button.get_url(urls.order_form)
        url = button.press_button(Locators.scooter, Locators.scooter_text)

        assert url == urls.squter

    @allure.title('Проверяем редирект на Дзен, если нажать на логотип Яндекса.')  # декораторы
    @allure.description(
        'На странице ищем логотип Яндекса, нажимаем, переходим на открывшуюся страницу, ждем, когда появится элемент на странице, получаем урл окна, сравниваем урл окна с урл страницы Дзена.')
    def test_dzen_page(self):
        button = ButtonPage(self.driver)
        button.get_url(urls.squter)
        url = button.press_logo(Locators.ya_logo, Locators.dzen)

        assert url == urls.dzen

    @allure.step('Закрываем браузер')
    @classmethod
    def teardown_class(cls):
        # закрыли браузер
        cls.driver.quit()
