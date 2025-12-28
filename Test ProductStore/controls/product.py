from selenium.webdriver.common.by import By


class Product:
    def __init__(self, driver, title):
        self.driver = driver
        self.title = title

    def wrapper(self):
        return self.driver.find_element(By.XPATH, f'//div[@class = "card-block"]//a[contains(text(), "{self.title}")]')
