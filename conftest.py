from selenium import webdriver
import pytest
import random

@pytest.fixture(scope="function") # Запуск браузера
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture(scope="function") # Данные для проверки регистрации нового пользователя
def registration_values():
    return {'name':"Антон",
            'email':f'anton_lafaev_15_{random.randint(100,999)}@yandex.ru',
            'password': 'qwerty'}
