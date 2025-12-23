from selenium.webdriver.common.by import By
from components.base_form import BaseComponent
from controls.button import Button
from controls.input import Input


class Form(BaseComponent):
    def __init__(self, driver, wrapper_locator):
        super().__init__(driver, wrapper_locator)


    def get_input_by_title(self, title):
        return Input(self.driver,title, (By.XPATH, f'//form//label[contains(text(), "{title}")]//ancestor::div[@class = "mt-2 row"]'))

    def get_button_by_title(self, title):
        return Button(self.driver, title, (By.XPATH, f'//form//button[contains(text(),"{title}")]'))

