import pyautogui, os, time

pyautogui.FAILSAFE = True

print(pyautogui.position())

while True:
	flag = 1
	if pyautogui.position().x == 0 and pyautogui.position().y == 0:
		print('Nosviii')
		break
	x = pyautogui.position().x
	y = pyautogui.position().y
	if pyautogui.position().x != x or pyautogui.position().y != y:
		os.system('clear')
		print(pyautogui.position())
	if x == 50 and y == 50 and flag == 1:
		flag = 0
		print('Encontraste un secreto ameeeo')
		time.sleep(2)
