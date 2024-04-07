from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import conftest
driver = webdriver.Chrome()

driver.get("https://stellarburgers.nomoreparties.site/")

def test_click_personal_account():
    driver.find_element(By.XPATH,
                        ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']").click()
    driver.find_element(By.NAME, "name").send_keys('somes@ya.ru')
    driver.find_element(By.NAME, "Пароль").send_keys(conftest.password)
    driver.find_element(By.XPATH,
                        ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
    driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
    time.sleep(3)

    driver.quit()

def test_from_personal_account_to_constructor():
    driver.find_element(By.XPATH,
                        ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']").click()
    driver.find_element(By.NAME, "name").send_keys('somes@ya.ru')
    driver.find_element(By.NAME, "Пароль").send_keys(conftest.password)
    driver.find_element(By.XPATH,
                        ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
    driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
    driver.find_element(By.LINK_TEXT, "Конструктор").click()

    time.sleep(3)

    driver.quit()

def test_from_personal_account_to_title_page_through_click_logo():
    driver.find_element(By.XPATH,
                        ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']").click()
    driver.find_element(By.NAME, "name").send_keys('somes@ya.ru')
    driver.find_element(By.NAME, "Пароль").send_keys(conftest.password)
    driver.find_element(By.XPATH,
                        ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()
    driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
    driver.find_element(By.CLASS_NAME, "AppHeader_header__logo__2D0X2").click()


    time.sleep(3)

    driver.quit()