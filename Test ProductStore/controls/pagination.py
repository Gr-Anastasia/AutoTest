from selenium.webdriver.common.by import By

class Pagination:
    def __init__(self, driver, title):
        self.driver = driver
        self.title = title

    def wrapper(self):
        return self.driver.find_element(By.XPATH, f'//li[@class = "page-item"]//button[text() = "{self.title}"]')
