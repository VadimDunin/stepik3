from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import math, time


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def click_element(self, how, what):
        try:
            button = self.browser.find_element(how, what)
            button.click()
        except (NoSuchElementException):
            return False
        return True

    def switch_to_alert(self):
        alert = self.browser.switch_to.alert
        alert.accept()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        time.sleep(0)
        alert.accept()
        alert_text = None
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            time.sleep(10)
            alert.accept()
            time.sleep(600)
        except NoAlertPresentException:
            print("No second alert presented")
        return alert_text