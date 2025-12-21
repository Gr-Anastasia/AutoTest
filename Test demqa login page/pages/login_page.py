from controls.input import Input


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/login"
        self.username_input = Input(self.driver, 'UserName')
        self.password_input = Input(self.driver, 'Password')

    def open(self):
        self.driver.get(self.url)

    def enter_username(self, username):
        self.username_input.set_value(username)

    def enter_password(self, password):
        self.password_input.set_value(password)