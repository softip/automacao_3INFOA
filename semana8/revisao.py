import pyautogui, time

#clica no campo de login
pyautogui.click(360, 500, duration=1)
pyautogui.write("ivan.pereira@ifsuldeminas.edu.br", interval=0.1)
#clica no botão avançar
pyautogui.click(640, 750, duration=1)
time.sleep(10)
pyautogui.write("não não não", interval=0.1)
pyautogui.click(262, 607, duration=1)
pyautogui.click(635, 749, duration=10)