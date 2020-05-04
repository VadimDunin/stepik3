from .pages.product_page import ProductPage
import time

# pytest -v --tb=line --language=en test_product_page.py
# pytest -v --tb=line test_product_page.py

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = ProductPage(browser, link)
    page.go_to_product_page()
    page.push_button_add_to_basket()
    page.check_tovar_name()
    text = page.solve_quiz_and_get_code()
    time.sleep(5)
    print(text)
    assert False
