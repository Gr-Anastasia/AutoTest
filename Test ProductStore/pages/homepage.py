from components.catalog import Catalog
from components.leftmenu import LeftMenu

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://www.demoblaze.com/index.html'

    def open(self):
        self.driver.get(self.url)

    def get_catalog(self):
        return Catalog(self.driver)

    def get_menu(self, title):
        return LeftMenu(self.driver, title)

    def menu_click_by_title(self, title):
        self.get_menu(title).wrapper().click()

    def product_click_by_title(self, title):
        self.get_catalog().get_product_by_title(title).wrapper().click()

    def pagination_click_by_title(self, title):
        self.get_catalog().get_pagination_by_title(title).wrapper().click()


