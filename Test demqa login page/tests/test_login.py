import time
from pages.login_page import FormPage


def test_form_username(driver):
    login_page = FormPage(driver)
    login_page.open()
    login_page.username_input.get_input().send_keys('ARBYZIC')
    login_page.password_input.get_input().send_keys('May')
    time.sleep(30)
