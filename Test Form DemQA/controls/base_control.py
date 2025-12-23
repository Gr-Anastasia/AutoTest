class BaseControl:
    def __init__(self, driver, wrapper_locator):
        self.driver = driver
        self.wrapper_locator = wrapper_locator

    def wrapper(self):
        return self.driver.find_element(*self.wrapper_locator)

