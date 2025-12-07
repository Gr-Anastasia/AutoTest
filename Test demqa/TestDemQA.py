import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service(r'./chromedriver.exe')

driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://demoqa.com/text-box")
time.sleep(2)

search_field_FullName = driver.find_element(By.ID, 'userName')
search_field_FullName.send_keys("Anastasiya")

search_field_UserEmail = driver.find_element(By.ID, 'userEmail')
search_field_UserEmail.send_keys("1023@mail.ru")

search_field_CurrentAddress = driver.find_element(By.ID, 'currentAddress')
search_field_CurrentAddress.send_keys("г.Уфа, ул. Жукова, д. 39")

search_field_PermanentAddress = driver.find_element(By.ID, 'permanentAddress')
search_field_PermanentAddress.send_keys("г.Уфа, ул. Гагарина, д. 39")

search_field_Submit = driver.find_element(By.XPATH, '//button[@id = "submit"]/parent::div')
search_field_Submit.click()

time.sleep(2)
driver.quit()

