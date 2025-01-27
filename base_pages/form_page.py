import allure
from locators.form import Locators
from base_pages.base_page import BasePage

class OrderFormPage(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    @allure.step('В форме на первой странице находим поля и заполняем их.')
    def form_page_1(self, name, sname, adress, loc_metro, telephone):

        self.find_element_on_page(Locators.field_name).send_keys(name)
        self.find_element_on_page(Locators.field_surname).send_keys(sname)
        self.find_element_on_page(Locators.field_adress).send_keys(adress)
        self.click_on_element(Locators.field_metro)
        self.click_on_element(loc_metro)
        self.find_element_on_page(Locators.field_telephone).send_keys(telephone)
        self.click_on_element(Locators.button_next)

    @allure.step('В форме на второй странице находим поля и заполняем их.')
    def form_page_2(self, loc_day, loc_renta, loc_c, com):
        self.click_on_element(Locators.field_date)
        self.click_on_element(loc_day)
        self.click_on_element(Locators.field_renta)
        self.click_on_element(loc_renta)
        self.click_on_element(loc_c)
        self.find_element_on_page(Locators.field_comment).send_keys(com)
        self.click_on_element(Locators.button_order)
