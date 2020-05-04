from .base_page import BasePage
from .locators import LoginPageLocators


class BasketPage(BasePage):
    def __init__(self, promo):
        self.login_page_url = self.url + "/catalogue/the-shellcoders-handbook_209"
        if promo:
            self.login_page_url += "/?promo=newYear"

    def open(self):
        self.browser.get(self.login_page_url)

    def add_book(self):
        self.browser.find_element_by_css(".btn-add-to-basket'").click()