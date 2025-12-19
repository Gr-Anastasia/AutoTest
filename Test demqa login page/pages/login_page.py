from controls.input import Input


class FormPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/login"

    def open(self):
        self.driver.get(self.url)
        

    def get_username_input(self):
        return Input(self.driver,'UserName')

    def get_username_input(self):
        return Input(self.driver,'Password')
