import pyautogui
import pyperclip
import time

pyautogui.PAUSE = 1

# Abrindo o navegador
pyautogui.hotkey('alt', 'tab')
pyautogui.press('win')
time.sleep(10)
pyautogui.write('chrome')
pyautogui.press('enter')

# Baixando base de dados
pyautogui.hotkey('ctrl', 't')
pyperclip.copy(
    'https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga')
pyautogui.hotkey('ctrlleft', 'v')
pyautogui.press('enter')
time.sleep(3)

pyautogui.doubleClick(x=424, y=328)
time.sleep(3)

pyautogui.click(x=381, y=405)
pyautogui.click(x=1160, y=217)
pyautogui.click(x=934, y=617)
time.sleep(5)

