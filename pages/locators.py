from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    FORM_LOGIN = (By.CSS_SELECTOR, "input#id_login-username")
    FORM_PASSWORD = (By.CSS_SELECTOR, "input#id_login-password")
    REG_EMAIL = (By.CSS_SELECTOR, "input#id_registration-email")
    REG_PASS1 = (By.CSS_SELECTOR, "input#id_registration-passwrd1")
    REG_PASS2 = (By.CSS_SELECTOR, "input#id_registration-passwrd2")