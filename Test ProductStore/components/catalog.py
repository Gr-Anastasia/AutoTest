from selenium.webdriver.common.by import By

from controls.product import Product
from controls.pagination import Pagination

class Catalog:
    def __init__(self, driver):
        self.driver = driver

    def wrapper(self):
        return self.driver.find_element(By.XPATH, '//div[@class = "col-lg-9"]')

    def get_pagination_by_title(self, title):
        return Pagination(self.driver, title)

    def get_product_by_title(self, title):
        return Product(self.driver, title)

