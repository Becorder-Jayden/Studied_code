# 구글에서 w3school checkboxes 검색, 사이트 참고
# radio button과 다르게 checkbox는 여러 개 선택이 가능함

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome('C:/Users/gmkim/Documents/GitHub/Studied_code/NadoCoding/사무자동화/chromedriver.exe')
browser.maximize_window()

browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_checkbox')

browser.switch_to.frame('iframeResult')

# elem = browser.find_element_by_xpath('//*[@id="vehicle1"]')
elem = browser.find_element(By.XPATH, '//*[@id="vehicle1"]')
elem = browser.find_element(By.ID, 'vehicle1')

if elem.is_selected() == False:
    print("선택 안되어 있으므로 선택")
    elem.click()
else:
    print("선택되어 있으므로 아무것도 안함")

time.sleep(3)