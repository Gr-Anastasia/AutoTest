import time

from selenium.webdriver.common.by import By
from pages.login_page import LoginPage


def test_form_invalid_username(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.send_keys_in_input_be_title('UserName', 'UserNameK')
    login_page.send_keys_in_input_be_title('Password', '7498463')
    login_page.click_in_button_by_title('Login')
    time.sleep(2)

    error_message = driver.find_element(By.ID, 'name').text
    assert error_message == 'Invalid username or password!', 'Ошибка - пользователь найден'

def test_form_username(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.send_keys_in_input_be_title('UserName', 'UserNameAr')
    login_page.send_keys_in_input_be_title('Password', '895468541')
    login_page.click_in_button_by_title('New User')
    time.sleep(2)

    form_register = driver.current_url
    assert form_register == 'https://demoqa.com/register', 'Ошибка - не перешли на форму регистрации'



