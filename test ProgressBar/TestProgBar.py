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
driver.get("http://uitestingplayground.com/progressbar")
time.sleep(2)

search_field_Start = driver.find_element(By.ID, 'startButton')
search_field_Start.click()

button_with_75 = WebDriverWait(driver, 20, poll_frequency=0.05).until(EC.text_to_be_present_in_element((By.ID, 'progressBar'), "75"))

if button_with_75 :
    search_field_Stop = driver.find_element(By.ID, 'stopButton')
    search_field_Stop.click()
else:
    driver.quit()
    print("Всё сломалось")

time.sleep(2)
driver.quit()