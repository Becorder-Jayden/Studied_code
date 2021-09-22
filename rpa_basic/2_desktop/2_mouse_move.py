import pyautogui

# 마우스 이동
# pyautogui.moveTo(200, 100) # 지정한 위치(가로 x, 세로 y)로 마우스를 이동
# pyautogui.moveTo(100, 200, duration=5) # 5초 동안 100, 200 위치로 이동

# pyautogui.moveTo(100, 200, duration = 5)
# pyautogui.moveTo(200, 200, duration = 5)
# pyautogui.moveTo(300, 300, duration = 5)/

# 상대 좌표로 마우스 이동 (현재 커서가 있는 위치로부터)
pyautogui.moveTo(100, 100, duration = 1)
print(pyautogui.position()) # Point(x, y)
pyautogui.move(100, 100, duration = 1) # 100, 100 기준으로 +100, +100 -> 200, 200
print(pyautogui.position()) # Point(x, y)
pyautogui.move(100, 100, duration = 1) # 200, 200 기준으로 -> 300, 300
print(pyautogui.position()) # Point(x, y)