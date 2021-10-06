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
# trash_icon = pyautogui.locateOnScreen("trash_icon.png", region=x, y, width, height)
# pyautogui.moveT(trash_icon)

pyautogui.mouseInfo()
