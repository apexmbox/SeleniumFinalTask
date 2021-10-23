from .locators import BasketPageLocators
from .base_page import BasePage

class BasketPage(BasePage):

    def should_not_be_basket_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket should be empty, but it's not."

    def should_be_empty_basket_message(self):
        #basket_message = self.browser.find_element(*BasePageLocators.BASKET_EMPTY_MESSAGE)
        #assert "Your basket is empty." == self.browser.find_element(*BasePageLocators.BASKET_EMPTY_MESSAGE).text, "Empty basket message is not presented."
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE)