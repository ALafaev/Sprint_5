from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import URL, HeaderLocators, LoginPageLocators, HomePageLocators, ProfilePageLocators

def test_personal_account_button_click_not_authorised_user_open_login_page(driver):
    driver.get(URL.HOME_PAGE_URL)
    driver.find_element(*HeaderLocators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(LoginPageLocators.REGISTER_BUTTON))
    assert driver.current_url == URL.LOGIN_PAGE_URL

def test_personal_account_button_click_authorised_user_open_profile_page(driver, login_values):
    driver.get(URL.HOME_PAGE_URL)
    driver.find_element(*HomePageLocators.ENTER_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(LoginPageLocators.ENTER_BUTTON))
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(login_values['email'])
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(login_values['password'])
    driver.find_element(*LoginPageLocators.ENTER_BUTTON).click()
    driver.find_element(*HeaderLocators.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(ProfilePageLocators.SAVE_BUTTON))
    assert driver.current_url == URL.PROFILE_PAGE_URL

def test_click_to_constructor_button_in_personal_account_page_authorised_user_open_main_page(driver, login_values):
    driver.get(URL.HOME_PAGE_URL)
    driver.find_element(*HomePageLocators.ENTER_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(LoginPageLocators.ENTER_BUTTON))
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(login_values['email'])
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(login_values['password'])
    driver.find_element(*LoginPageLocators.ENTER_BUTTON).click()
    driver.find_element(*HeaderLocators.CONSTRUCTOR_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(HomePageLocators.MAKE_ORDER_BUTTON))
    assert driver.current_url == URL.HOME_PAGE_URL

def test_click_to_logo_in_personal_account_page_authorised_user_open_main_page(driver, login_values):
    driver.get(URL.HOME_PAGE_URL)
    driver.find_element(*HomePageLocators.ENTER_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(LoginPageLocators.ENTER_BUTTON))
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(login_values['email'])
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(login_values['password'])
    driver.find_element(*LoginPageLocators.ENTER_BUTTON).click()
    driver.find_element(*HeaderLocators.LOGO_HEADER).click()
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(HomePageLocators.MAKE_ORDER_BUTTON))
    assert driver.current_url == URL.HOME_PAGE_URL