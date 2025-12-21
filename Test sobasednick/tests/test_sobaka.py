import pytest

from pages.korzina_page import KorzinaPage
from pages.product_page import ProductPage
from pages.shop_page import ShopPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_open(driver):
    shop_page = ShopPage(driver)
    shop_page.open()

def test_form_filter(driver):
    shop_page = ShopPage(driver)
    shop_page.open()
    shop_page.enter_text(shop_page.from_price_input, "100")
    shop_page.enter_text(shop_page.to_price_input, "6000")
    shop_page.click_button(shop_page.button_start)
    products_count = shop_page.get_len_product()

    assert products_count == 2, "Ожидалось 2 товара"

def test_button_detailed(driver):
    shop_page = ShopPage(driver)
    product_page = ProductPage(driver)
    shop_page.open()
    shop_page.click_button(shop_page.button_detailed)
    current_url = shop_page.get_url()
    WebDriverWait(driver, 2).until(
        EC.visibility_of_element_located(product_page.h1))

    assert current_url == "https://guru.qahacking.ru/index.php/magazin/product/view/1/6", "Ожидался другой URL"
    assert product_page.get_text_h1() == "Еще немного поспать", "Ожидался другой заголовок"


def test_shop_button(driver):
    product_page = ProductPage(driver)
    korzina_page = KorzinaPage(driver)
    product_page.open()
    product_page.click_button(product_page.shop_button)
    current_url = korzina_page.get_url()
    WebDriverWait(driver, 2).until(
        EC.visibility_of_element_located(korzina_page.main))

    assert current_url == "https://guru.qahacking.ru/index.php/magazin/korzina/view", "Ожидался другой URL"
    assert korzina_page.get_text_count() == '1', "Ожидалось количество 1"
