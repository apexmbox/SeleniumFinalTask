from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert WebDriverWait(self.browser, 3).until(
            EC.url_contains('login')
        ), "Current URL is not contains 'login'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"

    def should_be_registration_email_field(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), "Registration email field is not presented"

    def should_be_registration_password1_field(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD1), "Registration password1 field is not presented"

    def should_be_registration_password2_field(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD2), "Registration password2 field is not presented"

    def should_be_registration_button(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_BUTTON), "Registration button is not presented"

    def register_new_user(self, email, password):
        self.should_be_registration_email_field()
        self.should_be_registration_password1_field()
        self.should_be_registration_password2_field()

        email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        password1_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1)
        password2_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2)
        registration_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)

        email_field.send_keys(email)
        password1_field.send_keys(password)
        password2_field.send_keys(password)
        registration_button.click()
