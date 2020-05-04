from .pages.main_page import MainPage
from .pages.bucket_page import BasketPage

# pytest -v --tb=line --language=en test_main_page.py
 link = "(http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
# browser.find_element_by_css(".btn-add-to-basket'").click()
# browser.switch_to_alert()


def test_guest_can_add_product_to_basket(browser):
    page = BasketPage(browser, link, promo=True)
    page.open()
    page.add_book()
    page.solve_quiz()
    page.submit()




    # page = MainPage(browser, link)
    # page.open()
    # page.go_to_login_page()
    # login_page = LoginPage(browser, browser.current_url)
    # login_page.should_be_login_page()