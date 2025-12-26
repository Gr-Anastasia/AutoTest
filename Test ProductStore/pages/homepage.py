from selenium.webdriver.common.by import By
# from components.catalog import
# from components.leftmenu import

class StorePages:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://www.demoblaze.com/index.html'

    def open(self):
        self.driver.get(self.url)
