from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='C:\Python-Driver\chromedriver.exe')

driver.get("https://www.google.com/")
driver.maximize_window()
print(driver.title)


driver.close()