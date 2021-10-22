from .locators import ProductPageLocators
from .base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage(BasePage):

    def add_product_to_basket(self):
        self.should_be_promo_url()
        product_name = self.should_be_product_name()
        product_price = self.should_be_product_price()
        self.should_be_add_to_basket_button()

        self.press_add_to_basket_button()
        self.solve_quiz_and_get_code()

        self.should_be_success_messages()
        self.should_be_current_basket_message()

        self.check_product_name_in_basket(product_name)
        self.check_product_price_in_basket(product_price)

    def should_be_promo_url(self):
        assert '?promo=newYear' in self.browser.current_url, "Current URL is not contains 'promo' link."

    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not presented."
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def should_be_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not presented."
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Button 'Add to basket' is not presented."

    def should_be_success_messages(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Message about successful adding product to basket is not presented."

    def should_be_current_basket_message(self):
        assert self.is_element_present(*ProductPageLocators.CURRENT_BASKET_MESSAGE), "Message about current basket status is not presented."

    def press_add_to_basket_button(self):
        basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        basket.click()

    def check_product_name_in_basket(self, product_name):
        assert product_name == self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT).text, "Wrong product name in basket."

    def check_product_price_in_basket(self, product_price):
        assert product_price == self.browser.find_element(*ProductPageLocators.CURRENT_BASKET_MESSAGE_PRICE).text, "Wrong product price in basket."
