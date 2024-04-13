import data
from locators import LogIn
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import  WaitLocators

class TestLogIn:
    def test_log_in_with_button_log_in_in_account(self, driver):
        log_in_in_account_button = driver.find_element(*LogIn.BUTTON_LOG_IN_ACCOUNT)
        log_in_in_account_button.click()
        email = driver.find_element(*LogIn.EMAIL_FIELD)
        email.send_keys(data.email)
        password = driver.find_element(*LogIn.PASSWORD_FIELD)
        password.send_keys(data.password)
        log_in = driver.find_element(*LogIn.BUTTON_LOG_IN)
        log_in.click()
        wait = WebDriverWait(driver, 5)
        wait.until(EC.presence_of_element_located(
            (WaitLocators.WAIT_TEXT_BULKI)))
        assert 'Соберите бургер' in driver.page_source



    def test_test_log_in_through_personal_account(self, driver):
        personal_account = driver.find_element(*LogIn.PERSONAL_ACCOUNT)
        personal_account.click()
        email = driver.find_element(*LogIn.EMAIL_FIELD)
        email.send_keys(data.email)
        password = driver.find_element(*LogIn.PASSWORD_FIELD)
        password.send_keys(data.password)
        log_in = driver.find_element(*LogIn.BUTTON_LOG_IN)
        log_in.click()
        wait = WebDriverWait(driver, 5)
        wait.until(EC.presence_of_element_located(
            (WaitLocators.WAIT_TEXT_BULKI)))
        assert 'Соберите бургер' in driver.page_source



    def test_log_in_through_button_log_in_in_registration_form(self, driver):
        log_in_in_account_button = driver.find_element(*LogIn.BUTTON_LOG_IN_ACCOUNT)
        log_in_in_account_button.click()
        registration = driver.find_element(*LogIn.BUTTON_REGISTRATION)
        registration.click()
        login = driver.find_element(*LogIn.REGISTRATION_VOITY)
        login.click()
        email = driver.find_element(*LogIn.EMAIL_FIELD)
        email.send_keys(data.email)
        password = driver.find_element(*LogIn.PASSWORD_FIELD)
        password.send_keys(data.password)
        log_in = driver.find_element(*LogIn.BUTTON_LOG_IN)
        log_in.click()
        wait = WebDriverWait(driver, 5)
        wait.until(EC.presence_of_element_located(
            (WaitLocators.WAIT_TEXT_BULKI)))
        assert 'Соберите бургер' in driver.page_source


