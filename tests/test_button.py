import allure
from selenium import webdriver

from baseclass.button import Button
import urls
from locators.button import Locators


class TestButton:
    driver = None

    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера
        cls.driver = webdriver.Firefox()

    @allure.title('Нажимаем кнопку Заказать вверху страницы.')  # декораторы
    @allure.description('На странице ищем кнопку, нажимаем, переходим на страницу формы, получаем текущий урл, сравниваем текущий урл с урл страницы формы.')
    def test_press_button_above(self):
        #
        self.driver.get(urls.squter)
        button = Button(self.driver)

        assert button.press_button(Locators.order_above, Locators.form_name) == urls.order_form

    @allure.title('Нажимаем кнопку Заказать внизу страницы.')  # декораторы
    @allure.description(
        'На странице ищем кнопку, скроллим до неё, нажимаем, переходим на страницу формы, получаем текущий урл, сравниваем текущий урл с урл страницы формы.')
    def test_press_button_below(self):
        #
        self.driver.get(urls.squter)
        button = Button(self.driver)

        assert button.press_button(Locators.order_below, Locators.form_name) == urls.order_form

    @classmethod
    def teardown_class(cls):
        # закрыли браузер
        cls.driver.quit()
