from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import conftest
driver = webdriver.Chrome()

driver.get("https://stellarburgers.nomoreparties.site/")

def test_correct_registration():
    driver.find_element(By.XPATH,
                        ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']").click()
    driver.find_element(By.CLASS_NAME, "Auth_link__1fOlj").click()
    driver.find_element(By.NAME, "name").send_keys("Spirids")
    driver.find_element(By.XPATH,
                        ".//form[@class='Auth_form__3qKeq mb-20']/fieldset[2]/div/div/input[@class='text input__textfield text_type_main-default']").send_keys(
        'somes@ya.ru')
    driver.find_element(By.NAME, "Пароль").send_keys(conftest.password)
    driver.find_element(By.XPATH,
                        ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
    time.sleep(5)
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/register"
    driver.quit()

def test_check_empty_name():
    driver.find_element(By.XPATH,
                        ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']").click()
    driver.find_element(By.CLASS_NAME, "Auth_link__1fOlj").click()
    driver.find_element(By.NAME, "name").send_keys("")
    driver.find_element(By.XPATH,
                        ".//form[@class='Auth_form__3qKeq mb-20']/fieldset[2]/div/div/input[@class='text input__textfield text_type_main-default']").send_keys(
        'somes@ya.ru')
    driver.find_element(By.NAME, "Пароль").send_keys(conftest.password)
    driver.find_element(By.XPATH,
                        ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
    time.sleep(5)
    check = driver.find_element(By.XPATH,
                        ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")
    assert check.get_attribute('onclick') == None
    driver.quit()



def test_password_minimum_symbols():
    password_1 = conftest.password_1
    driver.find_element(By.XPATH,
                        ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']").click()
    driver.find_element(By.CLASS_NAME, "Auth_link__1fOlj").click()
    driver.find_element(By.NAME, "name").send_keys("Spirids")
    driver.find_element(By.XPATH,
                        ".//form[@class='Auth_form__3qKeq mb-20']/fieldset[2]/div/div/input[@class='text input__textfield text_type_main-default']").send_keys(
        'somes@ya.ru')
    driver.find_element(By.NAME, "Пароль").send_keys(password_1)
    driver.find_element(By.XPATH,
                        ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
    time.sleep(3)
    check = driver.find_element(By.XPATH,
                                ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")
    if len(password_1) < 6:
        assert check.get_attribute('onclick') == None
        driver.quit()




def test_incorrect_password():
    driver.find_element(By.XPATH,
                        ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']").click()
    driver.find_element(By.NAME, "name").send_keys('somes@ya.ru')
    driver.find_element(By.NAME, "Пароль").send_keys('qazxs')
    driver.find_element(By.XPATH,
                        ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()

    time.sleep(3)
    assert "Некорректный пароль" in driver.page_source
    time.sleep(5)

    driver.quit()
