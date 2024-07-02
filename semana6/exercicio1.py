'''fazer uma pesquisa no google
clique no campo de pesquisa, após digite o
texto 'como automatizar o whatsapp
após pressione a tecla enter
'''

import pyautogui
pyautogui.click(444, 468)
pyautogui.write('como automatizar o whatsapp')
pyautogui.press('enter')

pyautogui.moveTo(32,404, duration=0.2)
pyautogui.dragTo(505,573, duration=0.2)
pyautogui.hotkey('ctrl', 'c')

pyautogui.click(1059,521, duration=0.2)
pyautogui.hotkey('ctrl', 'v')
