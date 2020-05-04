from .pages.main_page import MainPage
from .pages.backet_page import BasketPage

# pytest -v --tb=line --language=en test_main_page.py
link = "(http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"
promo = "/?promo=newYear"


def test_guest_can_add_product_to_basket(browser):
    page = BasketPage(browser, link, promo=True)
    page.open()
    page.add_book()
    page.solve_quiz()
    page.submit()
