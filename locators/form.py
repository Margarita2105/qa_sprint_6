from selenium.webdriver.common.by import By

from data import  Data, Time

class Locators:

    field_name = (By.XPATH, ".//input[@placeholder='* Имя']")
    field_surname = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    field_adress = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    field_telephone = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    button_next = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    field_date = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    field_renta = (By.XPATH, ".//div[text()='* Срок аренды']")
    field_color = (By.XPATH, ".//div[text()='Цвет самоката']")
    color_black = (By.XPATH, ".//label[@for='black']")
    color_grey = (By.XPATH, ".//label[@for='grey']")
    field_comment = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
    button_order = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    day_1 = (By.XPATH, ".//div[text()='"+Time.currentTime_1+"']")
    day_2 = (By.XPATH, ".//div[text()='"+Time.currentTime_2+"']")
    metro_1 = (By.XPATH, "(.//div[text()='"+Data.metro_1+"'])")
    metro_2 = (By.XPATH, "(.//div[text()='"+Data.metro_2+"'])")
    renta_1 = (By.XPATH, ".//div[text() = '"+Data.renta_1+"']")
    renta_2 = (By.XPATH, ".//div[text() = '"+Data.renta_2+"']")
    window = (By.XPATH, ".//div[@class = 'Order_ModalHeader__3FDaJ']")
    field_metro = (By.XPATH, ".//input[@placeholder='* Станция метро']")
