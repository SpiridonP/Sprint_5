import config
from locators import PersonalAccount
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestPersonalAccount:
    def test_click_personal_account(self, driver):
        log_in = driver.find_element(*PersonalAccount.BUTTON_LOG_IN_ACCOUNT)
        log_in.click()
        email = driver.find_element(*PersonalAccount.EMAIL_FIELD)
        email.send_keys('somes@ya.ru')
        password = driver.find_element(*PersonalAccount.PASSWORD_FIELD)
        password.send_keys(config.password)
        log_in = driver.find_element(*PersonalAccount.BUTTON_LOG_IN)
        log_in.click()
        personal_account = driver.find_element(*PersonalAccount.PERSONAL_ACCOUNT)
        personal_account.click()
        wait = WebDriverWait(driver, 5)
        wait.until(EC.presence_of_element_located((By.XPATH, ".//p[text()='В этом разделе вы можете изменить свои персональные данные']")))
        assert 'В этом разделе вы можете изменить свои персональные данные'in driver.page_source
        driver.quit()

    def test_from_personal_account_to_constructor(self, driver):
        log_in = driver.find_element(*PersonalAccount.BUTTON_LOG_IN_ACCOUNT)
        log_in.click()
        email = driver.find_element(*PersonalAccount.EMAIL_FIELD)
        email.send_keys('somes@ya.ru')
        password = driver.find_element(*PersonalAccount.PASSWORD_FIELD)
        password.send_keys(config.password)
        log_in = driver.find_element(*PersonalAccount.BUTTON_LOG_IN)
        log_in.click()
        personal_account = driver.find_element(*PersonalAccount.PERSONAL_ACCOUNT)
        personal_account.click()
        constructor = driver.find_element(*PersonalAccount.BUTTON_CONSTRUCTOR)
        constructor.click()
        wait = WebDriverWait(driver, 5)
        wait.until(EC.presence_of_element_located(
            (By.XPATH, ".//h2[text()='Булки']")))
        assert 'Соберите бургер' in driver.page_source

    def test_from_personal_account_to_title_page_through_click_logo(self, driver):
        log_in = driver.find_element(*PersonalAccount.BUTTON_LOG_IN_ACCOUNT)
        log_in.click()
        email = driver.find_element(*PersonalAccount.EMAIL_FIELD)
        email.send_keys('somes@ya.ru')
        password = driver.find_element(*PersonalAccount.PASSWORD_FIELD)
        password.send_keys(config.password)
        log_in = driver.find_element(*PersonalAccount.BUTTON_LOG_IN)
        log_in.click()
        personal_account = driver.find_element(*PersonalAccount.PERSONAL_ACCOUNT)
        personal_account.click()
        logo = driver.find_element(*PersonalAccount.LOGO)
        logo.click()
        wait = WebDriverWait(driver, 5)
        wait.until(EC.presence_of_element_located(
            (By.XPATH, ".//h2[text()='Булки']")))
        assert 'Соберите бургер' in driver.page_source