import pyautogui

pyautogui.FAILSAFE = True

width, height = pyautogui.size()

try:

	for i in range(10):
		pyautogui.moveTo( 850, 440, duration = 0.5)
		pyautogui.moveTo(1050, 440, duration = 0.5)
		pyautogui.moveTo(1050, 650, duration = 0.5)
		pyautogui.moveTo( 850, 650, duration = 0.5)

except:
	print('Salimooo')
