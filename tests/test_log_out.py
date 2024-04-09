import config
from locators import LogOutLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class TestLogOut:
    def test_log_out(self, driver):
        log_in_in_account_button = driver.find_element(*LogOutLocators.BUTTON_LOG_IN_ACCOUNT)
        log_in_in_account_button.click()
        email = driver.find_element(*LogOutLocators.EMAIL_FIELD)
        email.send_keys('somes@ya.ru')
        password = driver.find_element(*LogOutLocators.PASSWORD_FIELD)
        password.send_keys(config.password)
        log_in = driver.find_element(*LogOutLocators.BUTTON_LOG_IN)
        log_in.click()
        personal_account = driver.find_element(*LogOutLocators.PERSONAL_ACCOUNT)
        personal_account.click()
        wait = WebDriverWait(driver, 5)
        wait.until(EC.element_to_be_clickable(LogOutLocators.BUTTON_LOG_OUT))
        log_out = driver.find_element(*LogOutLocators.BUTTON_LOG_OUT)
        log_out.click()
        wait = WebDriverWait(driver, 5)
        wait.until(EC.element_to_be_clickable((By.XPATH, ".//h2[text()='Вход']")))
        assert "Вход" in driver.page_source
        driver.quit()