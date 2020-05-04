from .base_page import BasePage
from .locators import BasketPageLocators
import math
from selenium.common.exceptions import NoAlertPresentException


class BasketPage(BasePage):
    def __init__(self, browser, link, promo):
        self.login_page_url = link
        if promo:
            self.login_page_url += "/?promo=newYear"

    def open(self):
        self.browser.get(self.login_page_url)

    def add_book(self):
        self.click_element(BasketPageLocators.BUTTON_ADD_OT_BASKET)

    def solve_quiz(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        alert_text = None
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
        return alert_text

    def submit(self):
        pass