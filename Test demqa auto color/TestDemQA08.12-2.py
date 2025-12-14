import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service(r'./chromedriver.exe')

driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://demoqa.com/auto-complete")
time.sleep(2)

color_multiple = driver.find_element(By.ID, 'autoCompleteMultipleInput')
color_multiple.send_keys("Red")
color_multiple.send_keys(Keys.ENTER)
color_multiple.send_keys("Green")
color_multiple.send_keys(Keys.ENTER)

color_single  = driver.find_element(By.ID, 'autoCompleteSingleInput')
color_single.send_keys("Voilet")
time.sleep(1)
color_single_voilet = driver.find_element(By.ID, 'react-select-3-option-0')
color_single_voilet.click()

try:
    red = driver.find_element(By.XPATH, '//*[@id="autoCompleteMultipleContainer"]//div[text()="Red"]')
    green = driver.find_element(By.XPATH, '//*[@id="autoCompleteMultipleContainer"]//div[text()="Green"]')
    voilet = driver.find_element(By.XPATH, '//*[@id="autoCompleteSingleContainer"]//div[text()="Voilet"]')
    if red and green and voilet:
        print("Поле заполнено")
    else:
        print("Поле не заполнено")
except:
    print("Поле не заполнено")

time.sleep(3)
driver.quit()