from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from .locators import AuthorizationByCodePageLocators
import time

class AuthorizationByCodePage(BasePage):

    def should_be_opened_authorization_by_code_page(self):
        self.should_be_authorization_by_code_message()
        self.should_be_form_to_enter_the_way_of_getting_code()
        self.should_be_get_code_button()

    def should_be_authorization_by_code_message(self):
        # реализуем проверку, что на странице есть сообщение Авторизация по коду
        assert self.is_element_present(*AuthorizationByCodePageLocators.AUTHORIZATION_BY_CODE_MESSAGE), \
            "Авторизация по коду is not presented"

    def should_be_form_to_enter_the_way_of_getting_code(self):
        # реализуем проверку, что есть есть форма для ввода способа получения кода
        assert self.is_element_present(*AuthorizationByCodePageLocators.WAY_OF_GETTING_CODE_FORM), \
            "form to enter the way of getting code is not presented"

    def should_be_get_code_button(self):
        # реализуем проверку, что есть кнопка Получить код на странице
        assert self.is_element_present(*AuthorizationByCodePageLocators.GET_CODE_BUTTON),\
            "Get button is not presented"

    def should_have_logo(self):
        assert self.is_element_present(*AuthorizationByCodePageLocators.LOGO), "LOGO is not is not presented"

    def enter_email(self, email):
        email_input = self.browser.find_element(*AuthorizationByCodePageLocators.WAY_OF_GETTING_CODE_FORM)
        email_input.send_keys(email)

    def enter_phone(self, phone):
        email_input = self.browser.find_element(*AuthorizationByCodePageLocators.WAY_OF_GETTING_CODE_FORM)
        email_input.send_keys(phone)

    def click_get_code_button(self):
        enter_button = self.browser.find_element(*AuthorizationByCodePageLocators.GET_CODE_BUTTON)
        enter_button.click()

    def click_enter_with_password_button(self):
        forgot_password_button = self.browser.find_element(*AuthorizationByCodePageLocators.ENTER_WITH_PASSWORD_BUTTON)
        forgot_password_button.click()

    def should_have_message_that_code_was_sent(self):
        assert self.browser.find_element(*AuthorizationByCodePageLocators.CODE_WAS_SENT_MESSAGE).text == \
               "Код подтверждения отправлен"

