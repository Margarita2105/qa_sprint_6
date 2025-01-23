import urls
from baseclass.base import Base

#Переход к вопросам
class Questions(Base):

    def __init__(self, driver):
        self.driver = driver

    def question(self, loc, loc_text):
        self.driver.get(urls.squter)
        # находим вопрос
        element = self.driver.find_element(*loc)
        # скролим до вопроса
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        # задаем ожидание пока появится вопрос
        self.wait(loc)
        # кликаем на вопрос
        self.driver.find_element(*loc).click()
        # Добавить явное ожидание пока появится текст ответа на вопрос
        self.wait(loc_text)
        # Запоминаем текст ответа в переменную
        text = self.text(loc_text)

        return text
