import pyautogui

pyautogui.sleep(3) # 3초 대기
# print(pyautogui.position())

# pyautogui.click(73, 15, duration=1) # (73, 15) 좌표를 마우스 클릭
# pyautogui.click()
# pyautogui.mouseDown()
# pyautogui.mouseUp()

# pyautogui.doubleClick()
# pyautogui.click(clicks=500)

# pyautogui.moveTo(200, 200)
# pyautogui.mouseDown() # 마우스 누른 상태
# pyautogui.moveTo(300,300) 
# pyautogui.mouseUp() # 마우스 버튼 뗀 상태

pyautogui.sleep(3) # 3초 대기
# pyautogui.rightClick()
# pyautogui.leftClick()


# print(pyautogui.position())
# pyautogui.moveTo(522, 441) # 현재 위치 기준으로 x 100만큼, y 0만큼 드래그
# # pyautogui.drag(100, 0, duration=0.25) # 너무 빠른 동작으로 drag 수행이 안될 때는 duration 값 설정
# pyautogui.dragTo(1515,349, duration=0.25)

pyautogui.scroll(-800) # 양수이면 위 방향으로 300만큼 스크롤, 음수이면 아래 방향으로 300만큼 스크롤