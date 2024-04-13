import data
from locators import Constructor
from locators import  WaitLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestConstructor:
    def test_check_sauses(self, driver):
        log_in_account = driver.find_element(*Constructor.BUTTON_LOG_IN_ACCOUNT)
        log_in_account.click()
        email = driver.find_element(*Constructor.EMAIL_FIELD)
        email.send_keys(data.email)
        password = driver.find_element(*Constructor.PASSWORD_FIELD)
        password.send_keys(data.password)
        log_in_button = driver.find_element(*Constructor.BUTTON_LOG_IN)
        log_in_button.click()
        constructor = driver.find_element(*Constructor.BUTTON_CONSTRUCTOR)
        constructor.click()
        sauses = driver.find_element(*Constructor.SAUSES)
        sauses.click()
        wait = WebDriverWait(driver, 5)
        wait.until(EC.presence_of_element_located(
            (WaitLocators.WAIT_TEXT_SAUSES)))
        assert driver.find_element(*WaitLocators.WAIT_TEXT_SAUSES).text == 'Соусы'





    def test_check_bulki(self, driver):
        log_in_account = driver.find_element(*Constructor.BUTTON_LOG_IN_ACCOUNT)
        log_in_account.click()
        email = driver.find_element(*Constructor.EMAIL_FIELD)
        email.send_keys(data.email)
        password = driver.find_element(*Constructor.PASSWORD_FIELD)
        password.send_keys(data.password)
        log_in_button = driver.find_element(*Constructor.BUTTON_LOG_IN)
        log_in_button.click()
        constructor = driver.find_element(*Constructor.BUTTON_CONSTRUCTOR)
        constructor.click()
        sauses = driver.find_element(*Constructor.SAUSES)
        sauses.click()
        bulki = driver.find_element(*Constructor.BULKI)
        bulki.click()
        wait = WebDriverWait(driver, 5)
        wait.until(EC.presence_of_element_located(
            (WaitLocators.WAIT_TEXT_BULKI)))
        assert driver.find_element(*WaitLocators.WAIT_TEXT_BULKI).text == 'Булки'


    def test_check_topping(self, driver):
        log_in_account = driver.find_element(*Constructor.BUTTON_LOG_IN_ACCOUNT)
        log_in_account.click()
        email = driver.find_element(*Constructor.EMAIL_FIELD)
        email.send_keys(data.email)
        password = driver.find_element(*Constructor.PASSWORD_FIELD)
        password.send_keys(data.password)
        log_in_button = driver.find_element(*Constructor.BUTTON_LOG_IN)
        log_in_button.click()
        constructor = driver.find_element(*Constructor.BUTTON_CONSTRUCTOR)
        wait = WebDriverWait(driver, 5)
        wait.until(EC.element_to_be_clickable(
            (WaitLocators.WAIT_TEXT_TOPPING)))
        constructor.click()
        topping = driver.find_element(*Constructor.TOPPING)
        topping.click()
        wait = WebDriverWait(driver, 5)
        wait.until(EC.presence_of_element_located(
            (WaitLocators.WAIT_TEXT_TOPPING)))
        assert driver.find_element(*WaitLocators.WAIT_TEXT_TOPPING).text == 'Начинки'



