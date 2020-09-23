from selenium.webdriver.common.by import By

class BasePageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class LoginPageLocators():
	LOGIN_SUBMIT = (By.CSS_SELECTOR, "[name='login_submit']")
	REGISTRATION_SUBMIT = (By.CSS_SELECTOR, "[name='registration_submit']")

class ProductPageLocators():
	BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
	MESSAGE_ADDED_TO_BASKET = (By.CSS_SELECTOR, "#messages > div.alert-success:nth-child(1) .alertinner strong")
	BASKET_PRICE = (By.CSS_SELECTOR, "#messages > div.alert-info p strong")
	PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main .price_color")
	PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
	SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages div.alert-success:nth-child(1)")
