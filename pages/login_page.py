from .base_page import BasePage
from .locators import LoginPageLocators



class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url 
        

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_SUBMIT), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_SUBMIT), "Registration form is not presented"

    def register_new_user(self, email, password):
        input_email = self.browser.find_element(*LoginPageLocators.EMAIL)
        input_email.send_keys(email)

        input_password = self.browser.find_element(*LoginPageLocators.PASSWORD)
        input_password.send_keys(password)

        input_confirm_password = self.browser.find_element(*LoginPageLocators.CONF_PASSWORD)
        input_confirm_password.send_keys(password)

        submit = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT)
        submit.click()

