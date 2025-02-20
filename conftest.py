from selenium import webdriver
import pytest

@pytest.fixture(scope="function") # Запуск браузера
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture(scope="function") # Данные для проверки регистрации нового пользователя
def registration_values():
    import random
    return {'name':"Антон",
            'email':f'anton_lafaev_15_{random.randint(100,999)}@yandex.ru',
            'password': 'qwerty'}

@pytest.fixture(scope="function") # Данные для проверки авторизации
def login_values():
    return {'name': "Антон",
            'email': f'anton_lafaev_15_573@yandex.ru',
            'password': 'qwerty'}