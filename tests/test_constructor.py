from selenium.webdriver.common.by import By
from selenium import webdriver
import time
driver = webdriver.Chrome()
import conftest

driver.get("https://stellarburgers.nomoreparties.site/")
def test_check_sauses():
    driver.find_element(By.XPATH,
                        ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']").click()
    driver.find_element(By.NAME, "name").send_keys('somes@ya.ru')
    driver.find_element(By.NAME, "Пароль").send_keys(conftest.password)
    driver.find_element(By.XPATH,
                        ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
    time.sleep(3)
    driver.find_element(By.XPATH,  ".//span[text()='Соусы']").click()
    time.sleep(3)

    driver.quit()

def test_check_bulki():
    driver.find_element(By.XPATH,
                        ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']").click()
    driver.find_element(By.NAME, "name").send_keys('somes@ya.ru')
    driver.find_element(By.NAME, "Пароль").send_keys(conftest.password)
    driver.find_element(By.XPATH,
                        ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
    time.sleep(3)
    driver.find_element(By.XPATH,  ".//span[text()='Соусы']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, ".//div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']/span[text()='Булки']").click()
    time.sleep(3)

    driver.quit()

def test_check_topping():
    driver.find_element(By.XPATH,
                        ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']").click()
    driver.find_element(By.NAME, "name").send_keys('somes@ya.ru')
    driver.find_element(By.NAME, "Пароль").send_keys(conftest.password)
    driver.find_element(By.XPATH,
                        ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, ".//span[text()='Начинки']").click()
    time.sleep(3)
    driver.quit()