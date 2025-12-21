from selenium.webdriver.common.by import By


class ShopPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://guru.qahacking.ru/index.php/magazin"
        self.from_price_input = (By.ID, "price_from")
        self.to_price_input = (By.ID, "price_to")
        self.button_start = (By.XPATH, '//input[@value="Старт"]')
        self.button_detailed = (By.XPATH, '//div[contains(@class, "block_product")][.//a[contains(text(), "Еще немного поспать")]]//a[contains(text(), "Подробнее")]')
        self.products = (By.XPATH, '//div[@class = "sblock4"]')

    def open(self):
        self.driver.get(self.url)

    def enter_text(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def click_button(self, locator):
        self.driver.find_element(*locator).click()

    def get_len_product(self):
        return len(self.driver.find_elements(*self.products))

    def get_url(self):
        return self.driver.current_url

