import time

from controls.input import Input
from pages.login_page import LoginPage


def test_form_username(driver):
    login_page = LoginPage(driver)
    login_page.open()
    time.sleep(2)
    login_page.enter_username("Aarrarara")
    login_page.password_input("125879")
    time.sleep(30)
