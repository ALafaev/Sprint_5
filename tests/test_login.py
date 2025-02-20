from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import URL, HeaderLocators, LoginPageLocators, RegisterPageLocators, HomePageLocators, PasswordRecoveryPageLocators

def test_login_by_main_page_enter_account_button_login_successfully(driver, login_values):
    driver.get(URL.HOME_PAGE_URL)
    driver.find_element(*HomePageLocators.ENTER_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(LoginPageLocators.ENTER_BUTTON))
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(login_values['email'])
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(login_values['password'])
    driver.find_element(*LoginPageLocators.ENTER_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(HomePageLocators.MAKE_ORDER_BUTTON))
    assert driver.find_element(*HomePageLocators.MAKE_ORDER_BUTTON)

def test_login_by_personal_account_button_login_successfully(driver, login_values):
    driver.get(URL.HOME_PAGE_URL)
    driver.find_element(*HeaderLocators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(LoginPageLocators.ENTER_BUTTON))
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(login_values['email'])
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(login_values['password'])
    driver.find_element(*LoginPageLocators.ENTER_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(HomePageLocators.MAKE_ORDER_BUTTON))
    assert driver.find_element(*HomePageLocators.MAKE_ORDER_BUTTON)

def test_login_by_registration_page_enter_account_button_login_successfully(driver, login_values):
    driver.get(URL.HOME_PAGE_URL)
    driver.find_element(*HeaderLocators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(LoginPageLocators.ENTER_BUTTON))
    driver.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
    driver.find_element(*RegisterPageLocators.ENTER_BUTTON).click()
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(login_values['email'])
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(login_values['password'])
    driver.find_element(*LoginPageLocators.ENTER_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(HomePageLocators.MAKE_ORDER_BUTTON))
    assert driver.find_element(*HomePageLocators.MAKE_ORDER_BUTTON)

def test_login_by_password_recovery_form_enter_account_button_login_successfully(driver, login_values):
    driver.get(URL.HOME_PAGE_URL)
    driver.find_element(*HeaderLocators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(LoginPageLocators.ENTER_BUTTON))
    driver.find_element(*LoginPageLocators.PASSWORD_RECOVERY_BUTTON).click()
    driver.find_element(*PasswordRecoveryPageLocators.ENTER_BUTTON).click()
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(login_values['email'])
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(login_values['password'])
    driver.find_element(*LoginPageLocators.ENTER_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(HomePageLocators.MAKE_ORDER_BUTTON))
    assert driver.find_element(*HomePageLocators.MAKE_ORDER_BUTTON)
