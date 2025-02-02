import allure

from locators.scooter_dzen_page_locators import Locators_logo
from base_pages.dzen_page import ButtonPage
import urls

class TestScooterDzenPage:

    @allure.title('Нажимаем на логотип Самоката.')  # декораторы
    @allure.description(
        'На странице ищем логотип Самоката, нажимаем, переходим на главную страницу Самоката, получаем текущий урл, сравниваем текущий урл с урл главной страницей Самоката.')
    def test_press_scooter_logo(self, driver):
        button = ButtonPage(driver)
        button.get_url(urls.order_form)
        url = button.press_button(Locators_logo.scooter, Locators_logo.scooter_text)

        assert url == urls.squter

    @allure.title('Проверяем редирект на Дзен, если нажать на логотип Яндекса.')  # декораторы
    @allure.description(
        'На странице ищем логотип Яндекса, нажимаем, переходим на открывшуюся страницу, ждем, когда появится элемент на странице, получаем урл окна, сравниваем урл окна с урл страницы Дзена.')
    def test_dzen_page(self, driver):
        button = ButtonPage(driver)
        button.get_url(urls.squter)
        url = button.press_logo(Locators_logo.ya_logo, Locators_logo.dzen)

        assert url == urls.dzen
