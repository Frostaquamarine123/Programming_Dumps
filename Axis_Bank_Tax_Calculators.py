from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='C:\Python-Driver\chromedriver.exe')
driver.implicitly_wait(100)

driver.get("https://www.axisbank.com/retail/calculators/home-loan-calculators/home-loan-tax-saving-calculator")
driver.maximize_window()
print(driver.title)

if driver.find_element_by_xpath('.//label[@for="seniorCitizen"]').is_enabled():
        driver.find_element_by_xpath('.//label[@for="seniorCitizen"]').click()
else:
    print('RadioButton Element is not enabled')

if driver.find_element_by_xpath('.//input[@id="annualIncome"]').is_enabled():
            driver.find_element_by_xpath('.//input[@id="annualIncome"]').send_keys('100000')
else:
    print('Annual Income Textbox is not enabled')

if driver.find_element_by_xpath('.//input[@id="interestPaid"]').is_enabled():
    driver.find_element_by_xpath('.//input[@id="interestPaid"]').send_keys('1000')
else:
    print('Interest Paid textbox is not enabled')
if driver.find_element_by_xpath('.//input[@id="principleRepaid"]').is_enabled():
    driver.find_element_by_xpath('.//input[@id="principleRepaid"]').send_keys('1000')
else:
    print('Principle Re paid textbox is not enabled')
if driver.find_element_by_xpath('.//a[@class="calculteAmt"]').is_enabled():
    driver.find_element_by_xpath('.//a[@class="calculteAmt"]').click()


driver.quit()