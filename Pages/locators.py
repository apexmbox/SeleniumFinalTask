from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
    TOTAL_BASKET_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner")
    SUCCESS_MESSAGE_PRODUCT = (By.CSS_SELECTOR, ".alertinner strong")
    CURRENT_BASKET_MESSAGE = (By.CSS_SELECTOR, ".alert-noicon .alertinner p")
    CURRENT_BASKET_MESSAGE_PRICE = (By.CSS_SELECTOR, ".alert-noicon .alertinner p strong")
