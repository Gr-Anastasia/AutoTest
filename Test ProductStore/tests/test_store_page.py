import time

from selenium.webdriver.common.by import By
from pages.homepage import HomePage

def test_store(driver):
    store_page = HomePage(driver)
    store_page.open()
    store_page.menu_click_by_title("Monitors")
    time.sleep(2)
    store_page.pagination_click_by_title("Next")
    time.sleep(2)
    product_name_by_store = driver.find_element(By.XPATH, '//a[contains(text(), "Dell i7")]').text
    store_page.product_click_by_title("Dell i7")
    time.sleep(2)
    product_name_by_product = driver.find_element(By.XPATH, '//h2[@class = "name"]').text

    assert product_name_by_store == product_name_by_product, 'Заголовки продуктов отличаются'



