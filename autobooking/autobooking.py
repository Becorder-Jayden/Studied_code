from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(
    executable_path=r'C:/Users/gmkim/Documents/GitHub/Studied_code/chromedriver.exe',
    chrome_options=options)



url = 'https://google.com'
driver.get(url)

driver.find_element_by_css_selector('input').send_keys('파이썬')
driver.implicitly_wait(3)
