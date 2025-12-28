from selenium.webdriver.common.by import By


class LeftMenu:
    def __init__(self, driver, title):
        self.driver = driver
        self.title = title

    def wrapper(self):
        return self.driver.find_element(By.XPATH, f'//div[@class = "col-lg-3"]//a[contains(text(), "{self.title}")]')
