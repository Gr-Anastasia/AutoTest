from selenium.webdriver.common.by import By
from components.form import Form


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/login"

    def open(self):
        self.driver.get(self.url)

    def get_form(self):
        return Form(self.driver, (By.ID, 'userForm'))

    def send_keys_in_input_be_title(self, title, word):
        self.get_form().get_input_by_title(title).get_input().send_keys(word)

    def click_in_button_by_title(self, title):
        self.get_form().get_button_by_title(title).wrapper().click()

