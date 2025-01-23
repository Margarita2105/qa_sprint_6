from locators.form import Locators

class OrderForm:

    def __init__(self, driver):
        self.driver = driver

    def form_1(self, name, sname, adress, loc_metro, telephone):

        self.driver.find_element(*Locators.field_name).send_keys(name)
        self.driver.find_element(*Locators.field_surname).send_keys(sname)
        self.driver.find_element(*Locators.field_adress).send_keys(adress)
        self.driver.find_element(*Locators.field_metro).click()
        self.driver.find_element(*loc_metro).click()
        self.driver.find_element(*Locators.field_telephone).send_keys(telephone)
        self.driver.find_element(*Locators.button_next).click()

    def form_2(self, loc_day, loc_renta, loc_c, com):
        self.driver.find_element(*Locators.field_date).click()
        self.driver.find_element(*loc_day).click()
        self.driver.find_element(*Locators.field_renta).click()
        self.driver.find_element(*loc_renta).click()
        self.driver.find_element(*loc_c).click()
        self.driver.find_element(*Locators.field_comment).send_keys(com)
        self.driver.find_element(*Locators.button_order).click()
