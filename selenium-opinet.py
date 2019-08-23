from selenium import webdriver
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import time
import pandas as pd

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')

driver = webdriver.Chrome('./chromedriver.exe', options=options)
driver.implicitly_wait(3)
driver.get('http://www.opinet.co.kr/searRgSelect.do')
time.sleep(1)
driver.get('http://www.opinet.co.kr/searRgSelect.do')

time.sleep(1)
print('해당 사이트로 이동 완료..')

sido_select = Select(driver.find_element_by_id('SIDO_NM0'))
sido_select.select_by_visible_text('부산')
time.sleep(0.5)
sido_select = Select(driver.find_element_by_id('SIGUNGU_NM0'))
sido_select.select_by_visible_text('해운대구')
time.sleep(3)
print('부산/해운대구 선택 완료..')
driver.get_screenshot_as_file('screen-shot.png')

html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')

href_value = soup.select_one('#body1 > tr:nth-child(16) > td.rlist > a')['href']

print(href_value.split(',')[22][1:-1])

driver.close()
