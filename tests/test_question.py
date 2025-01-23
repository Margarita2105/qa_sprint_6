import allure
from selenium import webdriver

from baseclass.question import Questions
import data
from locators.question import Locators


class TestOrderForm:
    driver = None

    @classmethod
    def setup_class(cls):
        # создали драйвер для браузера
        cls.driver = webdriver.Firefox()

    @allure.title('Получаем ответ на первый вопрос')
    @allure.description(
        'На странице ищем первый вопрос, скроллим до него, кликаем на вопрос, ждем когда появится ответ, получаем текст ответа и сравниваем с тем, что должно быть.')
    def test_question_how_much(self):
        ques = Questions(self.driver)
        text = ques.question(Locators.how_much, Locators.how_much_text)

        assert data.how_much == text

    @allure.title('Получаем ответ на второй вопрос')
    @allure.description(
        'На странице ищем второй вопрос, скроллим до него, кликаем на вопрос, ждем когда появится ответ, получаем текст ответа и сравниваем с тем, что должно быть.')
    def test_question_several_scooters(self):
        ques = Questions(self.driver)
        text = ques.question(Locators.several_scooters, Locators.several_scooters_text)

        assert data.several_scooters == text

    @allure.title('Получаем ответ на третий вопрос')
    @allure.description(
        'На странице ищем третий вопрос, скроллим до него, кликаем на вопрос, ждем когда появится ответ, получаем текст ответа и сравниваем с тем, что должно быть.')
    def test_calculated_rental_time(self):
        ques = Questions(self.driver)
        text = ques.question(Locators.rental_time, Locators.rental_time_text)

        assert data.rental_time == text

    @allure.title('Получаем ответ на четвертый вопрос')
    @allure.description(
        'На странице ищем четвертый вопрос, скроллим до него, кликаем на вопрос, ждем когда появится ответ, получаем текст ответа и сравниваем с тем, что должно быть.')
    def test_scooter_directly_for_today(self):
        ques = Questions(self.driver)
        text = ques.question(Locators.scooter_today, Locators.scooter_today_text)

        assert data.scooter_today == text

    @allure.title('Получаем ответ на пятый вопрос')
    @allure.description(
        'На странице ищем пятый вопрос, скроллим до него, кликаем на вопрос, ждем когда появится ответ, получаем текст ответа и сравниваем с тем, что должно быть.')
    def test_extend_or_return_scooter(self):
        ques = Questions(self.driver)
        text = ques.question(Locators.extend_or_return, Locators.extend_or_return_text)

        assert data.extend_or_return == text

    @allure.title('Получаем ответ на шестой вопрос')
    @allure.description(
        'На странице ищем шестой вопрос, скроллим до него, кликаем на вопрос, ждем когда появится ответ, получаем текст ответа и сравниваем с тем, что должно быть.')
    def test_bring_charger(self):
        ques = Questions(self.driver)
        text = ques.question(Locators.charger, Locators.charger_text)

        assert data.charger == text

    @allure.title('Получаем ответ на седьмой вопрос')
    @allure.description(
        'На странице ищем седьмой вопрос, скроллим до него, кликаем на вопрос, ждем когда появится ответ, получаем текст ответа и сравниваем с тем, что должно быть.')
    def test_cancel_order(self):
        ques = Questions(self.driver)
        text = ques.question(Locators.cancel, Locators.cancel_text)

        assert data.cancel == text

    @allure.title('Получаем ответ на восьмой вопрос')
    @allure.description(
        'На странице ищем восьмой вопрос, скроллим до него, кликаем на вопрос, ждем когда появится ответ, получаем текст ответа и сравниваем с тем, что должно быть.')
    def test_question_mkad(self):
        ques = Questions(self.driver)
        text = ques.question(Locators.mkad, Locators.mkad_text)

        assert data.mkad == text

    @classmethod
    def teardown_class(cls):
        # закрыли браузер
        cls.driver.quit()
