# 구글에서 w3schools radio button 검색, 사이트 참고
import time
from selenium import webdriver

browser = webdriver.Chrome('C:/Users/gmkim/Documents/GitHub/Studied_code/NadoCoding/사무자동화/chromedriver.exe')

browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')

browser.switch_to.frame('iframeResult') # frame 전환

elem = browser.find_element_by_xpath('//*[@id="html"]') # 성공

elem.click()

browser.switch_to.default_content() # 상위 frame으로 빠져 나옴

elem = browser.find_element_by_xpath('//*[@id="html"]') # 실패

elem.click()
time.sleep(5)
browser.quit()