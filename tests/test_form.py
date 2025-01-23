import allure
from selenium import webdriver

from baseclass.form import OrderForm
import urls
import data
from locators.form import Locators

class TestOrderForm:
    driver = None

    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера
        cls.driver = webdriver.Firefox()

    @allure.title('Заполняем первую часть формы с первыми тестовыми данными')
    @allure.description(
        'На странице ищем поле Имя и заполоняем, ищем поле Фамилия и заполняем, ищем поле адрес и заполняем, ищем поле Станция метро, кликаем, выбираем станцию, кликаем на неё, ищем поле телефон и заполняем, ищем и нажимаем кнопку Далее. Переходим ко второй части формы. На странице ищем поле Когда привезти самокат и нажимаем, выбираем дату, нажимаем, ищем поле Срок аренды, нажимаем, выбираем из списка, нажимаем, ищем поле Цвет самоката, из двух чек боксов выбираем нужный и кликаем на него, находим поле Комментарий и заполняем его, находим и нажимаем на кнопку Заказать.')
    def test_data_1(self):
        self.driver.get(urls.order_form)
        page = OrderForm(self.driver)
        page.form_1(data.name_1, data.sname_1, data.adress_1, Locators.metro_1, data.telephone_1)
        page.form_2(Locators.day_1, Locators.renta_1, Locators.color_grey, data.comment_1)

        assert data.win_text in self.driver.find_element(*Locators.window).text

    @allure.title('Заполняем первую часть формы со вторыми тестовыми данными')
    @allure.description(
        'На странице ищем поле Имя и заполоняем, ищем поле Фамилия и заполняем, ищем поле адрес и заполняем, ищем поле Станция метро, кликаем, выбираем станцию, кликаем на неё, ищем поле телефон и заполняем, ищем и нажимаем кнопку Далее. Переходим ко второй части формы. На странице ищем поле Когда привезти самокат и нажимаем, выбираем дату, нажимаем, ищем поле Срок аренды, нажимаем, выбираем из списка, нажимаем, ищем поле Цвет самоката, из двух чек боксов выбираем нужный и кликаем на него, находим поле Комментарий и заполняем его, находим и нажимаем на кнопку Заказать.')
    def test_data_2(self):
        self.driver.get(urls.order_form)
        page = OrderForm(self.driver)
        page.form_1(data.name_2, data.sname_2, data.adress_2, Locators.metro_2, data.telephone_2)
        page.form_2(Locators.day_2, Locators.renta_2, Locators.color_black, data.comment_2)

        assert data.win_text in self.driver.find_element(*Locators.window).text

    @classmethod
    def teardown_class(cls):
        # закрыли браузер
        cls.driver.quit()
