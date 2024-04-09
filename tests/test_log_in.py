import config
from locators import LogIn
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogIn:
    def test_log_in_with_button_log_in_in_account(self, driver):
        log_in_in_account_button = driver.find_element(*LogIn.BUTTON_LOG_IN_ACCOUNT)
        log_in_in_account_button.click()
        email = driver.find_element(*LogIn.EMAIL_FIELD)
        email.send_keys('somes@ya.ru')
        password = driver.find_element(*LogIn.PASSWORD_FIELD)
        password.send_keys(config.password)
        log_in = driver.find_element(*LogIn.BUTTON_LOG_IN)
        log_in.click()
        wait = WebDriverWait(driver, 5)
        wait.until(EC.presence_of_element_located(
            (By.XPATH, ".//h2[text()='Булки']")))
        assert 'Соберите бургер' in driver.page_source
        driver.quit()

    def test_test_log_in_through_personal_account(self, driver):
        personal_account = driver.find_element(*LogIn.PERSONAL_ACCOUNT)
        personal_account.click()
        email = driver.find_element(*LogIn.EMAIL_FIELD)
        email.send_keys('somes@ya.ru')
        password = driver.find_element(*LogIn.PASSWORD_FIELD)
        password.send_keys(config.password)
        log_in = driver.find_element(*LogIn.BUTTON_LOG_IN)
        log_in.click()
        wait = WebDriverWait(driver, 5)
        wait.until(EC.presence_of_element_located(
            (By.XPATH, ".//h2[text()='Булки']")))
        assert 'Соберите бургер' in driver.page_source
        driver.quit()

    def test_log_in_through_button_log_in_in_registration_form(self, driver):
        log_in_in_account_button = driver.find_element(*LogIn.BUTTON_LOG_IN_ACCOUNT)
        log_in_in_account_button.click()
        registration = driver.find_element(*LogIn.BUTTON_REGISTRATION)
        registration.click()
        login = driver.find_element(*LogIn.REGISTRATION_VOITY)
        login.click()
        email = driver.find_element(*LogIn.EMAIL_FIELD)
        email.send_keys('somes@ya.ru')
        password = driver.find_element(*LogIn.PASSWORD_FIELD)
        password.send_keys(config.password)
        log_in = driver.find_element(*LogIn.BUTTON_LOG_IN)
        log_in.click()
        wait = WebDriverWait(driver, 5)
        wait.until(EC.presence_of_element_located(
            (By.XPATH, ".//h2[text()='Булки']")))
        assert 'Соберите бургер' in driver.page_source
        driver.quit()
