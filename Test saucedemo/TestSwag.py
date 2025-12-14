import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service(r'./chromedriver.exe')

@pytest.mark.parametrize("username, password, expected_login",
                    [ ("standard_user", "secret_sauce", "https://www.saucedemo.com/inventory.html"),
                      ("locked_out_user", "secret_sauce", "https://www.saucedemo.com/inventory.html"),#.
                      ("problem_user", "secret_sauce", "https://www.saucedemo.com/inventory.html"),
                      ("performance_glitch_user", "secret_sauce", "https://www.saucedemo.com/inventory.html"), #глюкнутый
                      ("error_user", "secret_sauce", "https://www.saucedemo.com/inventory.html"),
                      ("visual_user", "secret_sauce", "https://www.saucedemo.com/inventory.html"),
                    ])
def test_param(username, password, expected_login):
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    search_field_username = driver.find_element(By.ID, 'user-name')
    search_field_password = driver.find_element(By.ID, 'password')
    search_field_login = driver.find_element(By.ID, 'login-button')
    search_field_username.send_keys(username)
    search_field_password.send_keys(password)
    search_field_login.click()
    time.sleep(2)
    assert driver.current_url == expected_login
    driver.quit()

# time.sleep(5)
# driver.quit()