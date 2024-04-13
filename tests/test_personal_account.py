import data
from locators import PersonalAccount
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import WaitLocators

class TestPersonalAccount:
    def test_click_personal_account(self, driver):
        log_in = driver.find_element(*PersonalAccount.BUTTON_LOG_IN_ACCOUNT)
        log_in.click()
        email = driver.find_element(*PersonalAccount.EMAIL_FIELD)
        email.send_keys(data.email)
        password = driver.find_element(*PersonalAccount.PASSWORD_FIELD)
        password.send_keys(data.password)
        log_in = driver.find_element(*PersonalAccount.BUTTON_LOG_IN)
        log_in.click()
        personal_account = driver.find_element(*PersonalAccount.PERSONAL_ACCOUNT)
        personal_account.click()
        wait = WebDriverWait(driver, 5)
        wait.until(EC.presence_of_element_located((WaitLocators.WAIT_TEXT_CHANGE_PERSONAL_DATA)))
        assert 'В этом разделе вы можете изменить свои персональные данные'in driver.page_source


    def test_from_personal_account_to_constructor(self, driver):
        log_in = driver.find_element(*PersonalAccount.BUTTON_LOG_IN_ACCOUNT)
        log_in.click()
        email = driver.find_element(*PersonalAccount.EMAIL_FIELD)
        email.send_keys(data.email)
        password = driver.find_element(*PersonalAccount.PASSWORD_FIELD)
        password.send_keys(data.password)
        log_in = driver.find_element(*PersonalAccount.BUTTON_LOG_IN)
        log_in.click()
        personal_account = driver.find_element(*PersonalAccount.PERSONAL_ACCOUNT)
        personal_account.click()
        constructor = driver.find_element(*PersonalAccount.BUTTON_CONSTRUCTOR)
        constructor.click()
        wait = WebDriverWait(driver, 5)
        wait.until(EC.presence_of_element_located(
            (WaitLocators.WAIT_TEXT_BULKI)))
        assert 'Соберите бургер' in driver.page_source

    def test_from_personal_account_to_title_page_through_click_logo(self, driver):
        log_in = driver.find_element(*PersonalAccount.BUTTON_LOG_IN_ACCOUNT)
        log_in.click()
        email = driver.find_element(*PersonalAccount.EMAIL_FIELD)
        email.send_keys(data.email)
        password = driver.find_element(*PersonalAccount.PASSWORD_FIELD)
        password.send_keys(data.password)
        log_in = driver.find_element(*PersonalAccount.BUTTON_LOG_IN)
        log_in.click()
        personal_account = driver.find_element(*PersonalAccount.PERSONAL_ACCOUNT)
        personal_account.click()
        logo = driver.find_element(*PersonalAccount.LOGO)
        logo.click()
        wait = WebDriverWait(driver, 5)
        wait.until(EC.presence_of_element_located(
            (WaitLocators.WAIT_TEXT_BULKI)))
        assert 'Соберите бургер' in driver.page_source