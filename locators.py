from selenium.webdriver.common.by import By
class RegistrationLocators:
    BUTTON_LOG_IN_ACCOUNT = (By.XPATH,
                        ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")
    BUTTON_REGISTRATION = (By.CLASS_NAME, "Auth_link__1fOlj")
    NAME_FIELD = (By.NAME, "name")
    EMAIL_FIELD = (By.XPATH,
                        ".//form[@class='Auth_form__3qKeq mb-20']/fieldset[2]/div/div/input[@class='text input__textfield text_type_main-default']")
    PASSWORD_FIELD = (By.NAME, "Пароль")
    BUTTON_LOG_IN = (By.XPATH,
                        ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")


class LogOutLocators:
    BUTTON_LOG_IN_ACCOUNT = (By.XPATH,
                             ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")
    EMAIL_FIELD = (By.NAME, "name")
    PASSWORD_FIELD = (By.NAME, "Пароль")
    BUTTON_LOG_IN = (By.XPATH,
                     ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")
    PERSONAL_ACCOUNT = (By.LINK_TEXT, "Личный Кабинет")
    BUTTON_LOG_OUT = (By.XPATH, ".//button[text()='Выход']")


class PersonalAccount:
    BUTTON_LOG_IN_ACCOUNT = (By.XPATH,
                             ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")
    EMAIL_FIELD = (By.NAME, "name")
    PASSWORD_FIELD = (By.NAME, "Пароль")
    BUTTON_LOG_IN = (By.XPATH,
                     ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")
    PERSONAL_ACCOUNT = (By.LINK_TEXT, "Личный Кабинет")
    BUTTON_CONSTRUCTOR = (By.LINK_TEXT, "Конструктор")
    LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")

class LogIn:
    BUTTON_LOG_IN_ACCOUNT = (By.XPATH,
                             ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")
    EMAIL_FIELD = (By.NAME, "name")
    PASSWORD_FIELD = (By.NAME, "Пароль")
    BUTTON_LOG_IN = (By.XPATH,
                     ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")
    PERSONAL_ACCOUNT = (By.LINK_TEXT, "Личный Кабинет")
    BUTTON_REGISTRATION = (By.CLASS_NAME, "Auth_link__1fOlj")
    PASSWORD_RECOVERY = (By.LINK_TEXT, "Восстановить пароль")
    REGISTRATION_VOITY = (By.LINK_TEXT, "Войти")

class Constructor:
    BUTTON_LOG_IN_ACCOUNT = (By.XPATH,
                             ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")
    EMAIL_FIELD = (By.NAME, "name")
    PASSWORD_FIELD = (By.NAME, "Пароль")
    BUTTON_LOG_IN = (By.XPATH,
                     ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")
    SAUSES = (By.XPATH,  ".//span[text()='Соусы']")
    BULKI = (By.XPATH, ".//div[@class='tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect']/span[text()='Булки']")
    TOPPING = (By.XPATH, ".//span[text()='Начинки']")
    BUTTON_CONSTRUCTOR = (By.LINK_TEXT, "Конструктор")

class WaitLocators:
    WAIT_TEXT_VHOD = (By.XPATH, ".//h2[text()='Вход']")
    WAIT_TEXT_BULKI = (By.XPATH, ".//h2[text()='Булки']")
    WAIT_TEXT_SAUSES = (By.XPATH, ".//h2[text()='Соусы']")
    WAIT_TEXT_TOPPING = (By.XPATH, ".//h2[text()='Начинки']")
    WAIT_TEXT_CHANGE_PERSONAL_DATA = (By.XPATH, ".//p[text()='В этом разделе вы можете изменить свои персональные данные']")
    WAIT_BUTTON_LOG_IN = (By.XPATH, ".//button[text()='Войти']")

