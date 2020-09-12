from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\Python-Driver\chromedriver.exe')
driver.implicitly_wait(1000)

driver.get('https://www.goindigo.in/')
driver.maximize_window()

