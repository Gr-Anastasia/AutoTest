from selenium.webdriver.common.by import By


class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://guru.qahacking.ru/index.php/magazin/product/view/1/6"
        self.shop_button = (By.XPATH, '//input[@value = "В корзину"]')
        self.h1 = (By.XPATH, '//h1[text()="Еще немного поспать"]')

    def open(self):
        self.driver.get(self.url)

    def click_button(self, locator):
        self.driver.find_element(*locator).click()

    def get_text_h1(self):
        h1 = self.driver.find_element(*self.h1)
        return h1.text

    def get_url(self):
        return self.driver.current_url