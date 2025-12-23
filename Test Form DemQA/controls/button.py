from controls.base_control import BaseControl


class Button(BaseControl):
    def __init__(self, driver, title, wrapper_locator):
        super().__init__(driver, wrapper_locator)
        self.driver = driver
        self.title = title
