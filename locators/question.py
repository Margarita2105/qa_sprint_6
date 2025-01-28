from selenium.webdriver.common.by import By

class Locators:

    how_much = (By.XPATH, ".//div[@id='accordion__heading-0']")
    how_much_text = (By.XPATH, ".//div[@id='accordion__panel-0']")
    mkad = (By.XPATH, ".//div[@id='accordion__heading-7']")
    mkad_text = (By.XPATH, ".//div[@id='accordion__panel-7']")
    several_scooters = (By.XPATH, ".//div[@id='accordion__heading-1']")
    several_scooters_text = (By.XPATH, ".//div[@id='accordion__panel-1']")
    rental_time = (By.XPATH, ".//div[@id='accordion__heading-2']")
    rental_time_text = (By.XPATH, ".//div[@id='accordion__panel-2']")
    scooter_today = (By.XPATH, ".//div[@id='accordion__heading-3']")
    scooter_today_text = (By.XPATH, ".//div[@id='accordion__panel-3']")
    extend_or_return = (By.XPATH, ".//div[@id='accordion__heading-4']")
    extend_or_return_text = (By.XPATH, ".//div[@id='accordion__panel-4']")
    charger = (By.XPATH, ".//div[@id='accordion__heading-5']")
    charger_text = (By.XPATH, ".//div[@id='accordion__panel-5']")
    cancel = (By.XPATH, ".//div[@id='accordion__heading-6']")
    cancel_text = (By.XPATH, ".//div[@id='accordion__panel-6']")
    list_question = [how_much, several_scooters, rental_time, scooter_today, extend_or_return, charger, cancel, mkad]
    list_answer = [how_much_text, several_scooters_text, rental_time_text, scooter_today_text, extend_or_return_text,
                   charger_text, cancel_text, mkad_text]
