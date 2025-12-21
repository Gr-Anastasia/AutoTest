from selenium.webdriver.common.by import By


class KorzinaPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://guru.qahacking.ru/index.php/magazin/korzina/view"
        self.count = (By.XPATH, '//div[contains(text(), "Количество")]/following-sibling::div//input')
        self.main = (By.ID, 'tm-main')

    def open(self):
        self.driver.get(self.url)

    def get_text_count(self):
        count_product = self.driver.find_element(*self.count)
        return count_product.get_attribute("value")

    def get_url(self):
        return self.driver.current_url