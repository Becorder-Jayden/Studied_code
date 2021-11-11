import time
from selenium import webdriver

browser = webdriver.Chrome('C:/Users/gmkim/Documents/GitHub/Studied_code/NadoCoding/사무자동화/chromedriver.exe')
browser.maximize_window()

browser.get('https://shopping.naver.com/home/p/index.naver')

# '무선마우스' 입력
browser.find_element_by_xpath('//*[@id="autocompleteWrapper"]/input[1]').send_keys('무선마우스')

# 검색 버튼 클릭
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div/div[2]/div/div[2]/form/fieldset/div[1]/button[2]').click()

time.sleep(5)
