class BaseComponent:
    def __init__(self, driver, wrapper_locator):
        self.wrapper_locator = wrapper_locator
        self.driver = driver

    def wrapper(self):
        return self.driver.find_element(*self.wrapper_locator)

    # def get_locator(self, title, locator):
    #     return BaseControl(self.driver,title, (*self.locator))

