from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import HeaderLocators, LoginPageLocators, RegisterPageLocators, ProfilePageLocators
from urls import URL

class TestRegistration:
    def test_registration_valid_values_account_created(self, driver, registration_values):
        driver.get(URL.HOME_PAGE_URL)
        driver.find_element(*HeaderLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(LoginPageLocators.REGISTER_BUTTON))
        driver.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(registration_values['name'])
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(registration_values['email'])
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(registration_values['password'])
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(LoginPageLocators.ENTER_BUTTON))
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(registration_values['email'])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(registration_values['password'])
        driver.find_element(*LoginPageLocators.ENTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(HeaderLocators.PERSONAL_ACCOUNT_BUTTON))
        driver.find_element(*HeaderLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(ProfilePageLocators.SAVE_BUTTON))
        assert driver.current_url == URL.PROFILE_PAGE_URL

    def test_registration_invalid_password_return_error(self, driver, registration_values):
        driver.get(URL.HOME_PAGE_URL)
        driver.find_element(*HeaderLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(LoginPageLocators.REGISTER_BUTTON))
        driver.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(registration_values['name'])
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(registration_values['email'])
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys('qwert')
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).click()
        assert driver.find_element(*RegisterPageLocators.INVALID_PASSWORD_ERROR_MESSAGE)
