from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class BasketPageLocators():
    BUTTON_ADD_OT_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")


class LoginPageLocators():
    FORM_LOGIN = (By.CSS_SELECTOR, "input#id_login-username")
    FORM_PASSWORD = (By.CSS_SELECTOR, "input#id_login-password")
    REG_EMAIL = (By.CSS_SELECTOR, "input#id_registration-email")
    REG_PASS1 = (By.CSS_SELECTOR, "input#id_registration-passwrd1")
    REG_PASS2 = (By.CSS_SELECTOR, "input#id_registration-passwrd2")


class ProductPageLocators():
    PRODUCT_NAME = (By.CSS_SELECTOR, "input#id_login-username")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "input#id_login-username")
    ADD_TO_BUCKET = (By.CSS_SELECTOR, ".btn-add-to-basket")