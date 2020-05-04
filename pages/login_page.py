from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, browser, url):
        self.login_page_url = self.url + "/accounts/login"

    def open(self):
        self.browser.get(self.login_page_url)

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        self.open()
        assert self.login_page_url == self.browser.get_current_url

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.FORM_LOGIN), "Login link is not presented"
        assert self.is_element_present(*LoginPageLocators.FORM_PASSWORD), "Login link is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REG_EMAIL), "Login link is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_PASS1), "Login link is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_PASS2), "Login link is not presented"
