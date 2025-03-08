from selenium import webdriver
from selenium.webdriver.common.by import By

class HeaderLocators:
    PERSONAL_ACCOUNT_BUTTON = (By.LINK_TEXT, 'Личный Кабинет')  # Кнопка "Личный кабинет"
    LOGO_HEADER = (By.XPATH, './/div[@class="AppHeader_header__logo__2D0X2"]/a')
    CONSTRUCTOR_BUTTON = (By.XPATH, './/p[text()="Конструктор"]/parent::a')

class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, './/label[text()="Email"]/parent::div/input') # Поле ввода "Email"
    PASSWORD_INPUT = (By.NAME, 'Пароль') # Поле ввода "Пароль"
    ENTER_BUTTON = (By.XPATH, './/button[text()="Войти"]') # Кнопка "Войти"
    REGISTER_BUTTON = (By.CLASS_NAME, 'Auth_link__1fOlj')  # Кнопка "Зарегистрироваться"
    PASSWORD_RECOVERY_BUTTON = (By.LINK_TEXT, 'Восстановить пароль')

class RegisterPageLocators:
    NAME_INPUT = (By.XPATH, './/label[text()="Имя"]/parent::div/input') # Поле ввода "Имя"
    EMAIL_INPUT = (By.XPATH, './/label[text()="Email"]/parent::div/input') # Поле ввода "Email"
    PASSWORD_INPUT = (By.NAME, 'Пароль') # Поле ввода "Пароль"
    REGISTER_BUTTON = (By.XPATH, './/button[text()="Зарегистрироваться"]') # Кнопка Зарегистрироваться
    ENTER_BUTTON = (By.LINK_TEXT, 'Войти') # Ссылка на страницу авторизации
    INVALID_PASSWORD_ERROR_MESSAGE = (By.XPATH, './/p[text()="Некорректный пароль"]') # Сообщение "Некорректный пароль"

class HomePageLocators():
    ENTER_ACCOUNT_BUTTON = (By.XPATH, './/button[text()="Войти в аккаунт"]') # Кнопка "Войти в аккаунт" (пользователь не авторизован)
    MAKE_ORDER_BUTTON = (By.XPATH, './/button[text()="Оформить заказ"]') # Кнопка "Оформить заказ" (пользователь авторизован)

class PasswordRecoveryPageLocators():
    ENTER_BUTTON = (By.LINK_TEXT, 'Войти') # Ссылка на страницу авторизации

class ProfilePageLocators():
    SAVE_BUTTON = (By.XPATH, './/button[text()="Сохранить"]') # Кнопка "Сохранить"
    LOGOUT_BUTTON = (By.XPATH, './/button[text()="Выход"]') # Кнопка "Выход"

class ConstructorLocators():
    BREAD_SECTION = (By.XPATH, './/span[text()="Булки"]') # Раздел "Булки"
    SAUCE_SECTION = (By.XPATH, './/span[text()="Соусы"]') # Раздел "Соусы"
    FILLING_SECTION = (By.XPATH, './/span[text()="Начинки"]') # Раздел "Начинки"
    ACTIVE_SECTION = (By.XPATH, ".//div[contains(@class, 'tab_tab_type_current__2BEPc')]/span") # Раздел активен
