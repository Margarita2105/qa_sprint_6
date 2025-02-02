import pytest

from selenium import webdriver

@pytest.fixture # фикстура, которая создает драйвер
def driver():
    driver = webdriver.Firefox()
    yield  driver

    driver.quit()
