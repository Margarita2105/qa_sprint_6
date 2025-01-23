from selenium.webdriver.common.by import By

class Locators:
    cuc = (By.XPATH, ".//button[@id='rcc-confirm-button']")
    scooter =(By.XPATH, ".//img[@alt='Scooter']")
    scooter_text = (By.XPATH, ".//div[@class='Home_Header__iJKdX']")
    ya_logo =(By.XPATH, ".//img[@alt='Yandex']")
    dzen =(By.XPATH, ".//button[text()='Найти']")
