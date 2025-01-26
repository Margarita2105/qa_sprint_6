import allure
import  pytest
from selenium import webdriver

import urls
from base_pages.question_page import QuestionsPage
from data import Data
from locators.question import Locators


class TestOrderForm:
    driver = None

    @allure.step('Открываем браузер Firefox')
    @classmethod
    def setup_class(cls):
         #создали драйвер для браузера
        cls.driver = webdriver.Firefox()

    @allure.title('Получаем ответ на вопрос')
    @allure.description(
        'На странице ищем вопрос, скроллим до него, кликаем на вопрос, ждем когда появится ответ, получаем текст ответа и сравниваем с тем, что должно быть.')
    @pytest.mark.parametrize("questions, locator_q, locator_a", [
        (Data.list_question[0], Locators.list_question[0], Locators.list_answer[0]),
        (Data.list_question[1], Locators.list_question[1], Locators.list_answer[1]),
        (Data.list_question[2], Locators.list_question[2], Locators.list_answer[2]),
        (Data.list_question[3], Locators.list_question[3], Locators.list_answer[3]),
        (Data.list_question[4], Locators.list_question[4], Locators.list_answer[4]),
        (Data.list_question[5], Locators.list_question[5], Locators.list_answer[5]),
        (Data.list_question[6], Locators.list_question[6], Locators.list_answer[6]),
        (Data.list_question[7], Locators.list_question[7], Locators.list_answer[7])
        ])
    def test_question(self, questions, locator_q, locator_a):
        ques = QuestionsPage(self.driver)
        ques.get_url(urls.squter)
        text = ques.question(locator_q, locator_a)

        assert questions == text

    @allure.step('Закрываем браузер')
    @classmethod
    def teardown_class(cls):
    #    # закрыли браузер
        cls.driver.quit()
