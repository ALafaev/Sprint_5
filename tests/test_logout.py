from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import HeaderLocators, LoginPageLocators, HomePageLocators, ProfilePageLocators
from urls import URL
from data import LoginValues

class TestLogout:
    def test_logout_click_logout_button_in_personal_account_page_logout_successfully(self, driver):
        driver.get(URL.HOME_PAGE_URL)
        driver.find_element(*HomePageLocators.ENTER_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(LoginPageLocators.ENTER_BUTTON))
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(LoginValues.EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(LoginValues.PASSWORD)
        driver.find_element(*LoginPageLocators.ENTER_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(HomePageLocators.MAKE_ORDER_BUTTON))
        driver.find_element(*HeaderLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver,3).until(expected_conditions.element_to_be_clickable(ProfilePageLocators.LOGOUT_BUTTON))
        driver.find_element(*ProfilePageLocators.LOGOUT_BUTTON).click()
        WebDriverWait(driver,3).until(expected_conditions.element_to_be_clickable(LoginPageLocators.ENTER_BUTTON))
        assert driver.current_url == URL.LOGIN_PAGE_URL
