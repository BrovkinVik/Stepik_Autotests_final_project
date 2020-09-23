from .pages.product_page import ProductPage
import pytest

list_link = [f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{n}" for n in range(7)] + \
	[pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail)] + \
	[f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{n}" for n in range(8, 10)]

@pytest.mark.param
@pytest.mark.parametrize("link", list_link)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    print(link)
    page.add_product_to_basket()

@pytest.mark.negative_checks
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	page = ProductPage(browser, link)
	page.open()
	page.add_product_to_basket()
	page.should_not_be_success_message()

@pytest.mark.negative_checks
def test_guest_cant_see_success_message(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	page = ProductPage(browser, link)
	page.open()
	page.should_not_be_success_message()

@pytest.mark.negative_checks
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	page = ProductPage(browser, link)
	page.open()
	page.add_product_to_basket()
	page.should_not_be_success_message_with_disappeared()

@pytest.mark.pom_step8
def test_guest_should_see_login_link_on_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(browser, link)
	page.open()
	page.should_be_login_link()

@pytest.mark.pom_step8
def test_guest_can_go_to_login_page_from_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(browser, link)
	page.open()
	page.go_to_login_page()   