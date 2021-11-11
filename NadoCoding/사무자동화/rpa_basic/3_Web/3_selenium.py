from selenium import webdriver

#browser = webdriver.Chrome('./chromedriver.exe')
browser = webdriver.Chrome()

# 네이버 이동
browser.get('http://naver.com')

# 카페 메뉴 찾기
elem = browser.find_element_by_link_text('카페')

# 속성 가져오기
elem.get_attribute('href')
elem.get_attribute('class')

# 클릭
elem.click()

# 뒤로 가기
browser.back()

# 앞으로 가기
browser.forward()

# 새로고침
browser.refresh()

# 뒤로 가기
browser.back()

# 검색창 찾기 (개발자 도구 이용)
elem = browser.find_element_by_id('query')

# 글자 입력하기
elem.send_keys('나도코딩')

# enter 치기
from selenium.webdriver.common.keys import Keys
elem.send_keys(Keys.ENTER)

# a 태그 찾기
elem = browser.find_element_by_tag_name('a')
elem.get_attribute('href')

# a 태그 모두 찾기
elems = browser.find_elements_by_tag_name('a')
for e in elems:
    e.get_attribute('href')

# 다음으로 이동
browser.get('http://daum.net')

# 검색창 찾기
elem = browser.find_element_by_name('q')

# 글자 입력하기
elem.send_keys("나도코딩")

# 글자 지우기
elem.clear()

# 글자 입력하기
elem.send_keys("나도코딩")

# 검색 버튼 찾기
elem = browser.find_element_by_xpath('//*[@id="daumSearch"]/fieldset/div/div/button[2]')

# 클릭하기
elem.click()

# 스크린샷 찍기
browser.save_screenshot('daum.png')

# 페이지 소스 보기
browser.page_source

# 브라우저 종료
browser.close() # 현재 탭 닫기
browser.quit() # 브라우저 종료하기

# 참고 URL : https://selenium-python.readthedocs.io/







# 직접 작성했던 코드

from selenium import webdriver
import time

browser = webdriver.Chrome(r"C:/Users/gmkim/Documents/GitHub/Studied_code/NadoCoding/사무자동화/chromedriver.exe")
browser.get("http://naver.com") # 네이버로 이동

elem = browser.find_element_by_link_text("카페")

# print(elem)
# print(elem.get_attribute("href"))
# print(elem.get_attribute("class"))

# elem.click() # 클릭
# browser.back() # 뒤로가기
# browser.forward() # 앞으로가기
# browser.refresh() # 새로고침

elem = browser.find_element_by_id("query")
elem.send_keys("나도코딩") # 글자를 입력

from selenium.webdriver.common.keys import Keys
elem.send_keys(Keys.ENTER) # enter 입력
elem = browser.find_element_by_tag_name("a")
# print(elem.get_attribute("href"))
elems = browser.find_elements_by_tag_name("a")
# print(elems)

# for e in elems:
#     e.get_attribute("herf")
#     print(e)

browser.get('http://www.daum.net')
elem = browser.find_element_by_name("q")
elem.send_keys("나도코딩")
elem.clear() # 입력된 글자를 모두 지움
elem.send_keys("나도코딩2")
elem = browser.find_element_by_xpath('//*[@id="daumSearch"]/fieldset/div/div/button[2]') # xpath 내의 큰따옴표와 작은 따옴표 입력에 헷갈리지 않도록 주의
elem.click()
# brower.save_screenshort('name') # 스크린샷
# browser.page_source # 페이지 소스 정보 가져오기
# browser.close() # 브라우저를 종료 (모든 탭을 종료)
# browser.quit() # 현재 탭만 종료