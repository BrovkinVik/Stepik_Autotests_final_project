from .base_page import BasePage
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):

    def add_product_to_basket(self):
        self.click_button_basket()
        self.solve_quiz_and_get_code()
        time.sleep(60)
        self.should_be_message_added_to_basket()
        self.basket_price_is_equal_to_price_of_goods()

    def click_button_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button.click()
        

    def should_be_message_added_to_basket(self):
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_ADDED_TO_BASKET)
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        print("Message text:", message.text)
        print("Product name:", product_name.text)
        assert product_name.text in message.text, "Product name in basket does not correspond to the added product"

    def basket_price_is_equal_to_price_of_goods(self):
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        print("Basket price:", basket_price.text)
        print("Product price:", product_price.text)
        assert product_price.text in basket_price.text, "Basket price does not equal product price"