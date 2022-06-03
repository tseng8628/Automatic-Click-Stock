import time
import pyautogui

while True:
	a = pyautogui.position()
	print('滑鼠當前坐標位置', a)
	time.sleep(5)

