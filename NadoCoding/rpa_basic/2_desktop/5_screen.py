import pyautogui
# 스크린 샷 찍기
# img = pyautogui.screenshot()
# img.save("screenshot.png") # 파일로 저장

# pyautogui.mouseInfo()
# 29,21 52,165,241 #34A5F1

pixel = pyautogui.pixel(29,21)
print(pixel)

# print(pyautogui.pixelMatchesColor(29,21, (52,165,241)))
# print(pyautogui.pixelMatchesColor(29,21, pixel))
