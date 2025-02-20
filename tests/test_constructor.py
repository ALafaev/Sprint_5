from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import URL, ConstructorLocators

def test_move_to_section_bread_by_click_not_authorised_user_open_section_bread(driver, login_values):
    driver.get(URL.HOME_PAGE_URL)
    WebDriverWait(driver,3).until(expected_conditions.element_to_be_clickable(ConstructorLocators.SAUCE_SECTION))
    driver.find_element(*ConstructorLocators.SAUCE_SECTION).click()
    driver.find_element(*ConstructorLocators.BREAD_SECTION).click()
    assert driver.find_element(*ConstructorLocators.ACTIVE_SECTION).text == 'Булки'

def test_move_to_section_sauce_by_click_not_authorised_user_open_section_sauce(driver, login_values):
    driver.get(URL.HOME_PAGE_URL)
    WebDriverWait(driver,3).until(expected_conditions.element_to_be_clickable(ConstructorLocators.SAUCE_SECTION))
    driver.find_element(*ConstructorLocators.SAUCE_SECTION).click()
    assert driver.find_element(*ConstructorLocators.ACTIVE_SECTION).text == 'Соусы'

def test_move_to_section_filling_by_click_not_authorised_user_open_section_filling(driver, login_values):
    driver.get(URL.HOME_PAGE_URL)
    WebDriverWait(driver,3).until(expected_conditions.element_to_be_clickable(ConstructorLocators.SAUCE_SECTION))
    driver.find_element(*ConstructorLocators.FILLING_SECTION).click()
    assert driver.find_element(*ConstructorLocators.ACTIVE_SECTION).text == 'Начинки'
