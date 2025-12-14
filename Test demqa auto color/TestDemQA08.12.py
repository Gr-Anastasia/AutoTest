import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service(r'./chromedriver.exe')

driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://demoqa.com/checkbox")
time.sleep(2)

search_field_check_home = driver.find_element(By.XPATH, '//input[@id= "tree-node-home"]/following-sibling::span[1]')
search_field_check_home.click()
home_is_checked = driver.find_element(By.XPATH, '//input[@id = "tree-node-home"]').is_selected()
if home_is_checked:
    print("Чекбокс home активен")
else:
    print("Чекбокс home неактивен")

search_field_arrow_home = driver.find_element(By.XPATH, '//span[text()="Home"]/ancestor::label/preceding-sibling::button')
search_field_arrow_home.click()
desktop_is_checked = driver.find_element(By.ID, 'tree-node-desktop').is_selected()
documents_is_checked = driver.find_element(By.ID, 'tree-node-documents').is_selected()
downloads_is_checked = driver.find_element(By.ID, 'tree-node-downloads').is_selected()
if desktop_is_checked and documents_is_checked and downloads_is_checked:
    print("Чекбоксы desktop,documents,downloads активны")
else:
    print("Чекбоксы desktop,documents,downloads неактивны")

search_field_arrow_desktop = driver.find_element(By.XPATH, '//span[text()="Desktop"]/ancestor::label/preceding-sibling::button')
search_field_arrow_desktop.click()
notes_is_checked = driver.find_element(By.ID, 'tree-node-notes').is_selected()
commands_is_checked = driver.find_element(By.ID, 'tree-node-commands').is_selected()
if notes_is_checked and commands_is_checked:
    print("Чекбоксы notes,commands активны")
else:
    print("Чекбоксы notes,commands неактивны")

search_field_arrow_download = driver.find_element(By.XPATH, '//span[text()="Downloads"]/ancestor::label/preceding-sibling::button')
search_field_arrow_download.click()
wordFile_is_checked = driver.find_element(By.ID, 'tree-node-wordFile').is_selected()
excelFile_is_checked = driver.find_element(By.ID, 'tree-node-excelFile').is_selected()
if wordFile_is_checked and excelFile_is_checked:
    print("Чекбоксы wordFile,excelFile активны")
else:
    print("Чекбоксы wordFile,excelFile неактивны")

time.sleep(2)
driver.quit()