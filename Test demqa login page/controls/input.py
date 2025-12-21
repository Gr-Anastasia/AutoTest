from selenium.webdriver.common.by import By


class Input:
    def __init__(self, driver, title):
        self.driver = driver
        self.wrapper = self.driver.find_element(By.XPATH, f'//form//label[contains(text(), "{title}")]//ancestor::div[@class = "mt-2 row"]')

    def get_input(self):
        return self.wrapper.find_element(By.XPATH, './/input')

    def set_value(self, value):
        input_element = self.get_input()
        input_element.send_keys(value)

