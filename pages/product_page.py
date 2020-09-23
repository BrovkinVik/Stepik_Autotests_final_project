from .base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):

    def add_product_to_basket(self):
        self.click_button_basket()
        self.solve_quiz_and_get_code()
        #time.sleep(10)
        product_name = self.get_product_name()
        self.should_be_message_added_to_basket(product_name)
        product_price = self.get_product_price()
        self.basket_price_is_equal_to_price_of_goods(product_price)

    def click_button_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button.click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
    
    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)   

    def should_be_message_added_to_basket(self, product_name):
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_ADDED_TO_BASKET)
        print("Message text:", message.text)
        print("Product name:", product_name.text)
        assert product_name.text == message.text, "Product name in basket does not correspond to the added product"
 
    def basket_price_is_equal_to_price_of_goods(self, product_price):
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        print("Basket price:", basket_price.text)
        print("Product price:", product_price.text)
        assert product_price.text == basket_price.text, "Basket price does not equal product price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"

    def should_not_be_success_message_with_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message don't disappeared"