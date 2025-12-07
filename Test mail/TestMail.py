import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


s = Service(r'./chromedriver.exe')

driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://ya.ru")
time.sleep(2)

search_field = driver.find_element(By.ID, 'text')
search_field.send_keys("mail")
search_field.send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)
time.sleep(2)

mail_link = driver.find_element(By.XPATH, '//*[@id="search-result"]//li//a[contains(normalize-space(), "Облако, Календарь")]')
mail_link.click()

handles = driver.window_handles
driver.switch_to.window(handles[1])

entry_link = driver.find_element(By.XPATH, '//a[text()="Войти"]')
entry_link.click()

try:
    WebDriverWait(driver, 5).until(
                    EC.visibility_of_element_located((By.XPATH, '//div[@data-test-id = "vkid-login-screen"]')))
    print("Поле ввода почты не найдено")

except:
    print("Поле ввода почты найдено")

driver.quit()