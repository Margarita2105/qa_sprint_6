import allure
import  pytest

import urls
from base_pages.main_page import QuestionsPage
from base_pages.dzen_page import ButtonPage
from data import Data
from locators.main_page_locators import Locators_main


class TestQuestions:

    @allure.title('Получаем ответ на вопрос')
    @allure.description(
        'На странице ищем вопрос, скроллим до него, кликаем на вопрос, ждем когда появится ответ, получаем текст ответа и сравниваем с тем, что должно быть.')
    @pytest.mark.parametrize("questions, locator_q, locator_a", [
        (Data.list_question[0], Locators_main.list_question[0], Locators_main.list_answer[0]),
        (Data.list_question[1], Locators_main.list_question[1], Locators_main.list_answer[1]),
        (Data.list_question[2], Locators_main.list_question[2], Locators_main.list_answer[2]),
        (Data.list_question[3], Locators_main.list_question[3], Locators_main.list_answer[3]),
        (Data.list_question[4], Locators_main.list_question[4], Locators_main.list_answer[4]),
        (Data.list_question[5], Locators_main.list_question[5], Locators_main.list_answer[5]),
        (Data.list_question[6], Locators_main.list_question[6], Locators_main.list_answer[6]),
        (Data.list_question[7], Locators_main.list_question[7], Locators_main.list_answer[7])
        ])
    def test_question(self, driver, questions, locator_q, locator_a):
        ques = QuestionsPage(driver)
        ques.get_url(urls.squter)
        text = ques.question(locator_q, locator_a)

        assert questions == text

class TestButton:

    @pytest.mark.parametrize("butt", [Locators_main.order_above, Locators_main.order_below])
    @allure.title('Нажимаем кнопку Заказать.')  # декораторы
    @allure.description('На странице ищем кнопку, нажимаем, переходим на страницу формы, получаем текущий урл, сравниваем текущий урл с урл страницы формы.')
    def test_press_button(self, driver, butt):
        button = ButtonPage(driver)
        button.get_url(urls.squter)

        assert button.press_button(butt, Locators_main.form_name) == urls.order_form
