from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

	def should_be_empty_basket(self):
		self.should_not_be_items_at_basket()
		self.should_be_empty_basket_message()

	def should_not_be_items_at_basket(self):
		assert self.is_not_element_present(*BasketPageLocators.ITEM_AT_BASKET), \
        	"Items basket is presented, but should not be"

	def should_be_empty_basket_message(self):
		assert "Your basket is empty." in self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text, \
			"Empty basket message is not presented"