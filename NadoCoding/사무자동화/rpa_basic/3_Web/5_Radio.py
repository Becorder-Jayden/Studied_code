# Radio button : 여러 개 중에서 하나를 선택하면 다른 선택이 해제되는 것

import time
from selenium import webdriver

browser = webdriver.Chrome('C:/Users/gmkim/Documents/GitHub/Studied_code/NadoCoding/사무자동화/chromedriver.exe')
browser.maximize_window() # 창 최대화

browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')

browser.switch_to.frame('iframeResult')

elem = browser.find_element_by_xpath('//*[@id="html"]')

# 선택이 안되어 있으면 선택하기
if elem.is_selected() == False: # 라디오 버튼이 선택되어 있지 않으면
    print("선택 안되어 있으므로 선택하기")
    elem.click()
else: # 라디오 버튼이 선택되어 있으면
    print("선택되어 있으므로 아무것도 안함")

time.sleep(3)
