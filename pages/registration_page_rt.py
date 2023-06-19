from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import RegistrationPageLocators
import time

class RegistrationPage(BasePage):

    def should_be_registration_page(self):
        self.should_be_message_about_registration()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert "https://lk.rt.ru/" in current_url, \
            f"подстроки https://lk.rt.ru/ нет в {current_url}"

    def should_be_message_about_registration(self):
        assert self.is_element_present(*RegistrationPageLocators.REGISTRATION_MESSAGE), \
                "MESSAGE ABOUT REGISTRATION is not presented"

    def should_be_name_surname_login_password_confirm_password_forms(self):
        assert self.is_element_present(*RegistrationPageLocators.NAME_FORM), "User name form is not presented"
        assert self.is_element_present(*RegistrationPageLocators.SURNAME_FORM), "User surname form is not presented"
        assert self.is_element_present(*RegistrationPageLocators.USERNAME_FORM), "Username form is not presented"
        assert self.is_element_present(*RegistrationPageLocators.PASSWORD_FORM), "Password form is not presented"
        assert self.is_element_present(*RegistrationPageLocators.CONFIRMATION_PASSWORD_FORM), "Confirmation password form is not presented"

    def enter_name(self, name):
        name_input = self.browser.find_element(*RegistrationPageLocators.NAME_FORM)
        name_input.send_keys(name)
        surname_input = self.browser.find_element(*RegistrationPageLocators.SURNAME_FORM)
        surname_input.click()

    def enter_surname(self, surname):
        surname_input = self.browser.find_element(*RegistrationPageLocators.SURNAME_FORM)
        surname_input.send_keys(surname)
        name_input = self.browser.find_element(*RegistrationPageLocators.NAME_FORM)
        name_input.click()

    def enter_password(self, password):
        password_input = self.browser.find_element(*RegistrationPageLocators.PASSWORD_FORM)
        password_input.send_keys(password)
        name_input = self.browser.find_element(*RegistrationPageLocators.NAME_FORM)
        name_input.click()

    def enter_confirmation_of_password(self, password):
        surname_input = self.browser.find_element(*RegistrationPageLocators.CONFIRMATION_PASSWORD_FORM)
        surname_input.send_keys(password)
        name_input = self.browser.find_element(*RegistrationPageLocators.NAME_FORM)
        name_input.click()

    def enter_email(self, email):
        password_input = self.browser.find_element(*RegistrationPageLocators.USERNAME_FORM)
        password_input.send_keys(email)
        name_input = self.browser.find_element(*RegistrationPageLocators.NAME_FORM)
        name_input.click()

    def enter_telephone(self, telephone):
        password_input = self.browser.find_element(*RegistrationPageLocators.USERNAME_FORM)
        password_input.send_keys(telephone)
        name_input = self.browser.find_element(*RegistrationPageLocators.NAME_FORM)
        name_input.click()

    def should_have_name_error_message(self):
        assert self.browser.find_element(*RegistrationPageLocators.NAME_ERROR_MESSAGE).text == \
               "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

    def should_have_surname_error_message(self):
        assert self.browser.find_element(*RegistrationPageLocators.SURNAME_ERROR_MESSAGE).text == \
               "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

    def should_have_error_message_that_password_should_be_more_then_8_symbols(self):
        assert self.browser.find_element(*RegistrationPageLocators.PASSWORD_ERROR_MESSAGE).text == \
               "Длина пароля должна быть не менее 8 символов"

    def should_have_error_message_that_password_does_not_contain_capital_letters(self):
        assert self.browser.find_element(*RegistrationPageLocators.PASSWORD_ERROR_MESSAGE).text == \
               "Пароль должен содержать хотя бы одну заглавную букву"

    def should_have_error_message_that_password_does_not_contain_small_letters(self):
        assert self.browser.find_element(*RegistrationPageLocators.PASSWORD_ERROR_MESSAGE).text == \
               "Пароль должен содержать хотя бы одну прописную букву"

    def should_have_error_message_that_password_must_contain_only_latin_letters(self):
        assert self.browser.find_element(*RegistrationPageLocators.PASSWORD_ERROR_MESSAGE).text == \
               "Пароль должен содержать только латинские буквы"

    def should_have_error_message_that_passwords_dont_match(self):
        assert self.browser.find_element(*RegistrationPageLocators.PASSWORD_CONFIRM_ERROR_MESSAGE).text == \
               "Пароли не совпадают"

    def should_have_message_that_account_already_exists(self):
        assert self.browser.find_element(*RegistrationPageLocators.MESSAGE_THAT_ACCOUNT_ALREADY_EXISTS).text == \
               "Учётная запись уже существует"

    def should_have_message_to_confirm_email_of_new_user(self):
        assert self.browser.find_element(*RegistrationPageLocators.MESSAGE_TO_CONFIRM_EMAIL).text == \
               "Подтверждение email"

    def click_registration_button(self):
        registration_button = self.browser.find_element(*RegistrationPageLocators.REGISTRATION_BUTTON)
        registration_button.click()

    def should_have_logo(self):
        assert self.is_element_present(*RegistrationPageLocators.LOGO), "LOGO is not is not presented"

    def register_new_user(self, name, surname, email, password):
        self.enter_name(name)
        self.enter_surname(surname)
        self.enter_email(email)
        self.enter_password(password)
        self.enter_confirmation_of_password(password)
        self.click_registration_button()
