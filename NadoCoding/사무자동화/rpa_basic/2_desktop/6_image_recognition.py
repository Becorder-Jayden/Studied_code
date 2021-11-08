import pyautogui
# file_menu = pyautogui.locateOnScreen("file_menu.png")
# print(file_menu)
# pyautogui.click(file_menu)

# trash_icon = pyautogui.locateOnScreen("trash_icon.png")
# pyautogui.moveTo(trash_icon)

# screen = pyautogui.locateOnScreen("screenshot.png")
# print(screen)

# 참고사이트 https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_checkbox
# for i in pyautogui.locateAllOnScreen("checkbox.png"):
    # print(i)
    # pyautogui.click(i, duration = 0.25)

# checkbox = pyautogui.locateOnScreen("checkbox.png")
# pyautogui.click(checkbox)

# trash_icon = pyautogui.locateOnScreen("trash_icon.png")
# pyautogui.moveTo(trash_icon)

# 속도 개선
# 1. GrayScale
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", grayscale=True)
# pyautogui.moveT(trash_icon)

# 2. 범위 지정
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", region=(1488, 623, 1881-1488, 137)
# pyautogui.moveTo(trash_icon)

# pyautogui.mouseInfo()
# 1488, 623
# 1881, 760

# 3. 정확도 조정
run_btn = pyautogui.locateOnScreen('run_btn.png', confidence=0.7) # 90 % 이상 일치 시 실행
pyautogui.moveTo(run_btn) 


# 자동화 대상이 바로 보여지지 않는 경우
file_menu_notepad = pyautogui.locateOnScreen('file_menu_notepad.png')
if file_menu_notepad:
    pyautogui.click(file_menu_notepad)
else:
    print('발견 실패')

# 터미널에 나오는 안내가 이해되지 않아서 잠시 중단.. 
# 6번 파일 retry 필요