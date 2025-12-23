from selenium.webdriver.common.by import By
from controls.base_control import BaseControl


class Input(BaseControl):
    def __init__(self, driver, title, wrapper_locator):
        super().__init__(driver, wrapper_locator)
        self.title = title

    def get_input(self):
        return self.wrapper().find_element(By.XPATH, './/input')
