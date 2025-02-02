import allure
import pytest

from base_pages.order_page import OrderFormPage
import urls
from data import Data
from locators.order_page_locators import Locators_order

class TestOrderForm:

    @allure.title('Заполняем форму с разными тестовыми данными')
    @allure.description(
        'На странице ищем поле Имя и заполоняем, ищем поле Фамилия и заполняем, ищем поле адрес и заполняем, ищем поле Станция метро, кликаем, выбираем станцию, кликаем на неё, ищем поле телефон и заполняем, ищем и нажимаем кнопку Далее. Переходим ко второй части формы. На странице ищем поле Когда привезти самокат и нажимаем, выбираем дату, нажимаем, ищем поле Срок аренды, нажимаем, выбираем из списка, нажимаем, ищем поле Цвет самоката, из двух чек боксов выбираем нужный и кликаем на него, находим поле Комментарий и заполняем его, находим и нажимаем на кнопку Заказать.')
    @pytest.mark.parametrize("name, sname, adress, metro, telephone, day, renta, color, comment", [
        (Data.name_1, Data.sname_1, Data.adress_1, Locators_order.metro_1, Data.telephone_1, Locators_order.day_1, Locators_order.renta_1, Locators_order.color_grey, Data.comment_1),
        (Data.name_2, Data.sname_2, Data.adress_2, Locators_order.metro_2, Data.telephone_2, Locators_order.day_2, Locators_order.renta_2, Locators_order.color_black, Data.comment_2),
        ])
    def test_order_form_with_two_sets_of_test_data(self, driver, name, sname, adress, metro, telephone, day, renta, color, comment):

        page = OrderFormPage(driver)
        page.get_url(urls.order_form)
        page.form_page_1(name, sname, adress, metro, telephone)
        page.form_page_2(day, renta, color, comment)

        assert Data.win_text in page.text_of_element(Locators_order.window)
