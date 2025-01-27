import allure
from selenium import webdriver
import pytest

from base_pages.button_page import ButtonPage

import urls
from locators.button import Locators

class TestButton:
    driver = None

    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера
        cls.driver = webdriver.Firefox()

    @pytest.mark.parametrize("butt", [Locators.order_above, Locators.order_below])
    @allure.title('Нажимаем кнопку Заказать.')  # декораторы
    @allure.description('На странице ищем кнопку, нажимаем, переходим на страницу формы, получаем текущий урл, сравниваем текущий урл с урл страницы формы.')
    def test_press_button(self, butt):
        button = ButtonPage(self.driver)
        button.get_url(urls.squter)

        assert button.press_button(butt, Locators.form_name) == urls.order_form

    @classmethod
    def teardown_class(cls):
        # закрыли браузер
        cls.driver.quit()
