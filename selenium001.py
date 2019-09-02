PASS = ''


import time
from selenium import webdriver

driver = webdriver.Chrome('./chromedriver.exe')

driver.get('https://login.coupang.com/login/login.pang')

time.sleep(3)

driver.find_element_by_id('login-email-input').send_keys('soongon@gmail.com')
driver.find_element_by_id('login-password-input').send_keys(PASS)

time.sleep(3)

driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[5]/button').click()

html = driver.page_source

time.sleep(5)

driver.close()
