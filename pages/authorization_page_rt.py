from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import LoginPageLocators
import time

class AuthorizationPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_authorization_message()
        self.should_be_login_form()
        self.should_be_enter_button()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert "https://lk.rt.ru/" in current_url, \
            f"подстроки https://lk.rt.ru/ нет в {current_url}"

    def should_be_authorization_message(self):
        assert self.is_element_present(*LoginPageLocators.AUTHORIZATION_MESSAGE), "Authorization message is not presented"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.USERNAME_FORM), "User name form is not presented"

    def should_be_enter_button(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.ENTER_BUTTON), "ENTER BUTTON is not presented"

    def should_have_tabs(self):
        assert self.is_element_present(*LoginPageLocators.EMAIL_TAB), "EMAIL_TAB is not presented"
        assert self.is_element_present(*LoginPageLocators.TELEPHONE_TAB), "EMAIL_TAB is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_TAB), "EMAIL_TAB is not presented"
        assert self.is_element_present(*LoginPageLocators.ACCOUNT_TAB), "EMAIL_TAB is not presented"

    def should_have_active_telephone_tab(self):
        assert self.is_element_present(*LoginPageLocators.TELEPHONE_TAB_ACTIVE), "TELEPHONE TAB is not is not active"

    def should_have_active_email_tab(self):
        assert self.is_element_present(*LoginPageLocators.EMAIL_TAB_ACTIVE), "EMAIL TAB is not is not active"

    def should_have_active_login_tab(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_TAB_ACTIVE), "LOGIN TAB is not is not active"

    def should_have_active_account_tab(self):
        assert self.is_element_present(*LoginPageLocators.ACCOUNT_TAB_ACTIVE), "ACCOUNT TAB is not is not active"

    def should_have_logo(self):
        assert self.is_element_present(*LoginPageLocators.LOGO), "LOGO is not is not presented"

    def enter_email(self, email):
        email_input = self.browser.find_element(*LoginPageLocators.USERNAME_FORM)
        email_input.send_keys(email)
        pass_input = self.browser.find_element(*LoginPageLocators.PASSWORD_FORM)
        pass_input.click()

    def enter_login(self, login):
        email_input = self.browser.find_element(*LoginPageLocators.USERNAME_FORM)
        email_input.send_keys(login)
        pass_input = self.browser.find_element(*LoginPageLocators.PASSWORD_FORM)
        pass_input.click()

    def enter_account(self, account):
        email_input = self.browser.find_element(*LoginPageLocators.USERNAME_FORM)
        email_input.send_keys(account)
        pass_input = self.browser.find_element(*LoginPageLocators.PASSWORD_FORM)
        pass_input.click()

    def enter_phone(self, phone):
        phone_input = self.browser.find_element(*LoginPageLocators.USERNAME_FORM)
        phone_input.send_keys(phone)

    def enter_password(self, password):
        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD_FORM)
        password_input.send_keys(password)

    def click_enter_button(self):
        enter_button = self.browser.find_element(*LoginPageLocators.ENTER_BUTTON)
        enter_button.click()

    def click_logout_button(self):
        icon = self.browser.find_element(*LoginPageLocators.ACCOUNT_ICON)
        icon.click()
        logout = self.browser.find_element(*LoginPageLocators.EXIT)
        logout.click()

    def click_forgot_password_button(self):
        forgot_password_button = self.browser.find_element(*LoginPageLocators.FORGOT_PASSWORD_BUTTON)
        forgot_password_button.click()

    def click_registration_button(self):
        registration_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        registration_button.click()

    def should_have_opened_account_page(self):
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print(self.browser.current_url)
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        assert self.browser.current_url == "https://start.rt.ru/"

    def should_have_error_message(self):
        assert self.browser.find_element(*LoginPageLocators.ERROR_MESSAGE).text == \
               "Неверный логин или пароль"
        assert self.is_element_present(*LoginPageLocators.FORGOT_PASSWORD_LINK), \
                "FORGOT_PASSWORD_LINK is not red colour"


