from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import PasswordRecoveryPageLocators
import time

class PasswordRecoveryPage(BasePage):

    def should_be_password_recovery_page(self):
        self.should_be_message_about_password_recovery()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert "https://lk.rt.ru/" in current_url, \
            f"подстроки https://lk.rt.ru/ нет в {current_url}"

    def should_be_message_about_password_recovery(self):
        assert self.is_element_present(*PasswordRecoveryPageLocators.MESSAGE_ABOUT_PASSWORD_RECOVERY), \
                "MESSAGE ABOUT PASSWORD_RECOVERY message is not presented"

    def should_be_login_form(self):
        assert self.is_element_present(*PasswordRecoveryPageLocators.USERNAME_FORM), "User name form is not presented"

    def should_be_continue_button(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*PasswordRecoveryPageLocators.CONTINUE_BUTTON), "ENTER BUTTON is not presented"

    def should_be_back_button(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*PasswordRecoveryPageLocators.BACK_BUTTON), "ENTER BUTTON is not presented"

    def should_have_tabs(self):
        assert self.is_element_present(*PasswordRecoveryPageLocators.EMAIL_TAB), "EMAIL_TAB is not presented"
        assert self.is_element_present(*PasswordRecoveryPageLocators.TELEPHONE_TAB), "EMAIL_TAB is not presented"
        assert self.is_element_present(*PasswordRecoveryPageLocators.LOGIN_TAB), "EMAIL_TAB is not presented"
        assert self.is_element_present(*PasswordRecoveryPageLocators.ACCOUNT_TAB), "EMAIL_TAB is not presented"

    def should_have_active_telephone_tab(self):
        assert self.is_element_present(*PasswordRecoveryPageLocators.TELEPHONE_TAB_ACTIVE), "TELEPHONE TAB is not is not active"

    def should_have_active_email_tab(self):
        assert self.is_element_present(*PasswordRecoveryPageLocators.EMAIL_TAB_ACTIVE), "EMAIL TAB is not is not active"

    def should_have_active_login_tab(self):
        assert self.is_element_present(*PasswordRecoveryPageLocators.LOGIN_TAB_ACTIVE), "LOGIN TAB is not is not active"

    def should_have_active_account_tab(self):
        assert self.is_element_present(*PasswordRecoveryPageLocators.ACCOUNT_TAB_ACTIVE), "ACCOUNT TAB is not is not active"

    def should_have_logo(self):
        assert self.is_element_present(*PasswordRecoveryPageLocators.LOGO), "LOGO is not is not presented"
