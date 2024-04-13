import data
import helpers
from locators import RegistrationLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import  WaitLocators




class TestRegistration:
    def test_correct_registration(self, driver):

        log_in_in_account_button = driver.find_element(*RegistrationLocators.BUTTON_LOG_IN_ACCOUNT)
        log_in_in_account_button.click()
        registration_button = driver.find_element(*RegistrationLocators.BUTTON_REGISTRATION)
        registration_button.click()
        name_field = driver.find_element(*RegistrationLocators.NAME_FIELD)
        name_field.send_keys(data.name)
        email_field = driver.find_element(*RegistrationLocators.EMAIL_FIELD)
        email_field.send_keys(helpers.email)
        password_field = driver.find_element(*RegistrationLocators.PASSWORD_FIELD)
        password_field.send_keys(data.password)
        log_in_button = driver.find_element(*RegistrationLocators.BUTTON_LOG_IN)
        log_in_button.click()
        wait = WebDriverWait(driver, 5)
        wait.until(EC.presence_of_element_located(
            (WaitLocators.WAIT_BUTTON_LOG_IN)))
        assert "Вход" in driver.page_source


    def test_check_empty_name(self, driver):
        log_in_in_account_button = driver.find_element(*RegistrationLocators.BUTTON_LOG_IN_ACCOUNT)
        log_in_in_account_button.click()
        registration_button = driver.find_element(*RegistrationLocators.BUTTON_REGISTRATION)
        registration_button.click()
        name_field = driver.find_element(*RegistrationLocators.NAME_FIELD)
        name_field.send_keys("")
        email_field = driver.find_element(*RegistrationLocators.EMAIL_FIELD)
        email_field.send_keys(data.email)
        password_field = driver.find_element(*RegistrationLocators.PASSWORD_FIELD)
        password_field.send_keys(data.password)
        log_in_button = driver.find_element(*RegistrationLocators.BUTTON_LOG_IN)
        log_in_button.click()
        assert log_in_button.get_attribute('onclick') == None


    def test_password_minimum_symbols(self, driver):
        log_in_in_account_button = driver.find_element(*RegistrationLocators.BUTTON_LOG_IN_ACCOUNT)
        log_in_in_account_button.click()
        registration_button = driver.find_element(*RegistrationLocators.BUTTON_REGISTRATION)
        registration_button.click()
        name_field = driver.find_element(*RegistrationLocators.NAME_FIELD)
        name_field.send_keys(data.name)
        email_field = driver.find_element(*RegistrationLocators.EMAIL_FIELD)
        email_field.send_keys(data.email)
        password_field = driver.find_element(*RegistrationLocators.PASSWORD_FIELD)
        password_field.send_keys(data.incorrect_password)
        log_in_button = driver.find_element(*RegistrationLocators.BUTTON_LOG_IN)
        log_in_button.click()
        assert log_in_button.get_attribute('onclick') == None


    def test_incorrect_password(self, driver):
        log_in_in_account_button = driver.find_element(*RegistrationLocators.BUTTON_LOG_IN_ACCOUNT)
        log_in_in_account_button.click()
        email = driver.find_element(*RegistrationLocators.NAME_FIELD)
        email.send_keys(data.email)
        password_field = driver.find_element(*RegistrationLocators.PASSWORD_FIELD)
        password_field.send_keys(data.incorrect_password)
        log_in_button = driver.find_element(*RegistrationLocators.BUTTON_LOG_IN)
        log_in_button.click()
        wait = WebDriverWait(driver, 5)
        wait.until(EC.presence_of_element_located(
            (WaitLocators.WAIT_BUTTON_LOG_IN)))
        assert "Некорректный пароль" in driver.page_source











