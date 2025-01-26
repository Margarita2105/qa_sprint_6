from base_pages.base_page import BasePage
import allure



#Переход к вопросам
class QuestionsPage(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    @allure.step('Сравниваем ответ на вопрос из Вопросов о важном с текстом по требованиям.')
    def question(self, locator, locator_text):
        # находим вопрос
        element = self.find_element_on_page(locator)
        # скролим до вопроса
        self.scroll(element)
        # задаем ожидание пока появится вопрос
        self.wait_visibility_of_element(locator)
        # кликаем на вопрос
        self.click_on_element(locator)
        # Добавить явное ожидание пока появится текст ответа на вопрос
        self.wait_visibility_of_element(locator_text)
        # Запоминаем текст ответа в переменную
        text = self.text_of_element(locator_text)

        return text
