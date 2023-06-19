import time
import pytest

from .pages.authorization_page_rt import AuthorizationPage
from .pages.registration_page_rt import RegistrationPage


# проверяем что страница регистрации открывается
@pytest.mark.registration
def test_can_open_registration_page(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
    # открываем страницу авторизации
    page.open()
    # нажимаем кнопку Регистрация
    page.click_registration_button()

    page2 = RegistrationPage(browser,browser.current_url)
    # проверяем, что открылась страница регистрации
    page2.should_be_message_about_registration()

@pytest.mark.registration
def test_that_all_input_forms_presented_on_registration_page(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
    # открываем страницу авторизации
    page.open()
    # нажимаем кнопку Регистрация
    page.click_registration_button()

    page2 = RegistrationPage(browser, browser.current_url)
    # проверяем, что открылась страница регистрации
    page2.should_be_message_about_registration()
    # проверяем что на странице регистрации есть поля
    # для ввода данных пользователя (имя,фамилия,регион,имеил или телефон, пароль, подтверждение пароля)
    page2.should_be_name_surname_login_password_confirm_password_forms()

@pytest.mark.registration
def test_that_logo_is_presented(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
    # открываем страницу авторизации
    page.open()
    # нажимаем кнопку Регистрация
    page.click_registration_button()

    page2 = RegistrationPage(browser, browser.current_url)
    # проверяем что на странице есть лого
    page2.should_have_logo()

@pytest.mark.registration
def test_show_error_message_in_case_name_is_entered_not_in_сyrillic(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
    # открываем страницу авторизации
    page.open()
    # нажимаем кнопку Регистрация
    page.click_registration_button()

    page2 = RegistrationPage(browser, browser.current_url)
    name = "Tany"
    # вводим имя латиницей в поле Имя
    page2.enter_name(name)
     # проверяем что появилась надпись "Необходимо заполнить поле кириллицей. От 2 до 30 символов."
    page2.should_have_name_error_message()

@pytest.mark.registration
def test_show_error_message_in_case_surname_is_entered_not_in_сyrillic(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
    # открываем страницу авторизации
    page.open()
    # нажимаем кнопку Регистрация
    page.click_registration_button()

    page2 = RegistrationPage(browser, browser.current_url)
    surname = "Ivanova"
    # вводим фамилию латиницей в поле Имя
    page2.enter_surname(surname)
     # проверяем что появилась надпись "Необходимо заполнить поле кириллицей. От 2 до 30 символов."
    page2.should_have_surname_error_message()

@pytest.mark.registration
def test_show_error_message_in_case_password_shorter_then_8_simbols(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
    # открываем страницу авторизации
    page.open()
    # нажимаем кнопку Регистрация
    page.click_registration_button()

    page2 = RegistrationPage(browser, browser.current_url)
    password = "QA12345"
    # вводим пароль в поле Пароль длиной 7 символов
    page2.enter_password(password)
    # проверяем что появилась надпись "Длина пароля должна быть не менее 8 символов"
    page2.should_have_error_message_that_password_should_be_more_then_8_symbols()

@pytest.mark.registration
def test_show_error_message_in_case_password_does_not_contain_capital_letters(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
    # открываем страницу авторизации
    page.open()
    # нажимаем кнопку Регистрация
    page.click_registration_button()

    page2 = RegistrationPage(browser, browser.current_url)
    name = "Марина"
    password = "qa123567"
    # вводим пароль в поле Пароль без заглавных букв
    page2.enter_password(password)
    # проверяем что появилась надпись "Пароль должен содержать хотя бы одну заглавную букву"
    page2.should_have_error_message_that_password_does_not_contain_capital_letters()

@pytest.mark.registration
def test_show_error_message_in_case_password_does_not_contain_small_letters(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
    # открываем страницу авторизации
    page.open()
    # нажимаем кнопку Регистрация
    page.click_registration_button()

    page2 = RegistrationPage(browser, browser.current_url)
    name = "Марина"
    password = "QA123567"
    # вводим пароль в поле Пароль без строчных букв
    page2.enter_password(password)
    # проверяем что появилась надпись "Пароль должен содержать хотя бы одну строчную букву"
    page2.should_have_error_message_that_password_does_not_contain_small_letters()

@pytest.mark.registration
def test_show_error_message_in_case_password_contains_cyrrilics_letters(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
    # открываем страницу авторизации
    page.open()
    # нажимаем кнопку Регистрация
    page.click_registration_button()

    page2 = RegistrationPage(browser, browser.current_url)
    name = "Марина"
    password = "апаквпа123567"
    # вводим пароль в поле Пароль без заглавных букв
    page2.enter_password(password)
    # проверяем что появилась надпись "Пароль должен содержать только латинские буквы"
    page2.should_have_error_message_that_password_must_contain_only_latin_letters()

@pytest.mark.registration
def test_show_error_message_in_case_of_password_and_confirmation_password_dont_match(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
    # открываем страницу авторизации
    page.open()
    # нажимаем кнопку Регистрация
    page.click_registration_button()

    page2 = RegistrationPage(browser, browser.current_url)
    password = "QWerty123567"
    confirm_password = "QWerty12356789"
    # вводим пароль в поле Пароль
    page2.enter_password(password)
    # вводим не совпадающий с первым пароль в поле Подтвердить пароль
    page2.enter_confirmation_of_password(confirm_password)
    # нажимаем кнопку Зарегистрироваться
    page2.click_registration_button()
    # проверяем что появилась надпись "Пароли не совпадают"
    page2.should_have_error_message_that_passwords_dont_match()

@pytest.mark.registration
def test_show_message_that_account_already_exists_if_data_of_existing_accoun_entered_for_registration(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
    # открываем страницу авторизации
    page.open()
    # нажимаем кнопку Регистрация
    page.click_registration_button()

    page2 = RegistrationPage(browser, browser.current_url)
    password = "FV4-eQc-P2d-mGZ"
    name = "Марина"
    surname = "Порубова"
    email = "mfporubova@gmail.com"

    page2.enter_name(name)
    page2.enter_surname(surname)
    page2.enter_email(email)
    # вводим пароль в поле Пароль
    page2.enter_password(password)
    page2.enter_confirmation_of_password(password)
    # нажимаем кнопку Зарегистрироваться
    page2.click_registration_button()
    # проверяем что появилась надпись "Учётная запись уже существует"
    page2.should_have_message_that_account_already_exists()

@pytest.mark.registration
def test_register_new_user(browser):
    link = "https://lk.rt.ru/"
    page = AuthorizationPage(browser, link)
    # открываем страницу авторизации
    page.open()
    # нажимаем кнопку Регистрация
    page.click_registration_button()

    page2 = RegistrationPage(browser, browser.current_url)
    password = "FV4-eQc-P2d-mGZ"
    name = "Марина"
    surname = "Порубова"
    # генерируем случайный имеил
    email = str(time.time()) + "@gmail.com"
    # Регистрируем нового пользователя
    page2.register_new_user(name, surname, email, password)
    # проверяем что появилась надпись "Учётная запись уже существует"
    page2.should_have_message_to_confirm_email_of_new_user()

# pytest -m pytest -v --driver Chrome --driver-path /D:/Skillfactory/ChromeDriver/chromedriver_win32/chromedriver.exe/test_registration_page_rt.py
