from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def __init__(self, browser, url, product=None):
        super().__init__(browser, url)
        self.product_page_link = "http://selenium1py.pythonanywhere.com/catalogue"
        self.product = product
        self.default_product = "/coders-at-work_207"
        self.promo = "/?promo=newYear"

    def go_to_product_page(self, product=None, use_promo=True):
        if product is None:
            self.product_page_link += self.product
        if use_promo:
            self.product_page_link += self.promo
        self.browser.get(self.product_page_link)

    def push_button_add_to_basket(self):
        self.click_element(ProductPageLocators.ADD_TO_BUCKET)

    def get_book_name(self):
        return self.browser.find_element_by_css_selector("h1").text

    def get_price(self):
        return self.browser.find_element_by_css_selector("p.price_color").text

    def check_tovar_name(self, book_name, price):
        assert self.get_book_name() == book_name
        assert self.get_price() == price
