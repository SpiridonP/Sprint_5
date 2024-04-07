from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import conftest
driver = webdriver.Chrome()

driver.get("https://stellarburgers.nomoreparties.site/")

def test_log_in_with_button_log_in_in_account():
    driver.find_element(By.XPATH,
                        ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']").click()
    driver.find_element(By.NAME, "name").send_keys('somes@ya.ru')
    driver.find_element(By.NAME, "Пароль").send_keys(conftest.password)
    driver.find_element(By.XPATH,
                        ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
    assert driver.find_element(By.XPATH,
                        ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").text == 'Войти'
    time.sleep(3)

    driver.quit()

def test_test_log_in_through_personal_account():
    driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
    driver.find_element(By.NAME, "name").send_keys('somes@ya.ru')
    driver.find_element(By.NAME, "Пароль").send_keys(conftest.password)
    driver.find_element(By.XPATH,
                        ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
    time.sleep(3)

    driver.quit()

def test_log_in_through_button_log_in_in_registration_form():
    driver.find_element(By.XPATH,
                        ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']").click()
    driver.find_element(By.CLASS_NAME, "Auth_link__1fOlj").click()
    driver.find_element(By.LINK_TEXT, "Войти").click()
    driver.find_element(By.NAME, "name").send_keys('somes@ya.ru')
    driver.find_element(By.NAME, "Пароль").send_keys(conftest.password)
    driver.find_element(By.XPATH,
                        ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()

    time.sleep(3)

    driver.quit()

def test_log_in_with_password_recovery():
    driver.find_element(By.XPATH,
                        ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']").click()
    driver.find_element(By.LINK_TEXT, "Восстановить пароль").click()
    driver.find_element(By.LINK_TEXT, "Войти").click()
    driver.find_element(By.NAME, "name").send_keys('somes@ya.ru')
    driver.find_element(By.NAME, "Пароль").send_keys(conftest.password)
    driver.find_element(By.XPATH,
                        ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
    time.sleep(3)

    driver.quit()

