from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\Python-Driver\chromedriver.exe')
driver.implicitly_wait(1000)

driver.get('https://www.bigbasket.com/')
driver.maximize_window()

# Perform search through Search Bar
try:
 if driver.find_element_by_xpath('.//input[@qa="searchBar"]').is_displayed():
    driver.find_element_by_xpath('.//input[@qa="searchBar"]').click()
    driver.find_element_by_xpath('.//input[@qa="searchBar"]').send_keys('cashew')
    if driver.find_element_by_xpath('.//button[@type="submit"]').is_enabled():
        driver.find_element_by_xpath('.//button[@type="submit"]').click()
    else:
        print('Search Button is not enabled')
    driver.find_element_by_xpath('(.//div[@qa="qty"]/input)[1]').click()
    driver.find_element_by_xpath('(.//div[@qa="qty"]/input)[1]').send_keys('5')
    driver.find_element_by_xpath('(.//button[@qa="add"])[1]').click()

 else:
    print('Search Button is Not Visible')

# validate no of quantity in cart
 if driver.find_element_by_xpath('.//span[@id="mobiletotalNumberOfCartItems"]').is_displayed():

        quantity = driver.find_element_by_xpath('.//span[@id="mobiletotalNumberOfCartItems"]').text
        assert quantity.text == 1
 else:
     print('Cart functionality is not working')

finally:
    driver.close()
