# w3school option tag 검색, 사이트 활용

import time
from selenium import webdriver

browser = webdriver.Chrome('C:/Users/gmkim/Documents/GitHub/Studied_code/NadoCoding/사무자동화/chromedriver.exe')
browser.maximize_window()

browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_option')
browser.switch_to_frame('iframeResult')

# 방법 1
# cars에 해당하는 element를 찾고, 드롭다운 내부에 있는 4번째 옵션을 선택
# elem = browser.find_element_by_xpath('//*[@id="cars"]/option[4]')
# option[1] : 첫 번째 항목
# option[2] : 두 번째 항목
# elem.click()

time.sleep(5)

# 방법 2
# 완전히 일치하는 텍스트 값을 통해서 선택하는 방법
# 옵션 중에서 텍스트가 Audi인 항목을 선택
# elem = browser.find_element_by_xpath('//*[@id="cars"]/option[text()="Audi"]')
# elem.click()

# 방법 3
# 텍스트 값이 부분 일치하는 항목 선택하는 방법
elem = browser.find_element_by_xpath('//*[@id="cars"]/option[contains(text(), "Au")]')
elem.click()

time.sleep(5)