import pyautogui
import time

#Atleta
cAtleta = pyautogui.locateCenterOnScreen('atleta.png', grayscale=True, confidence=0.9)
pyautogui.click(cAtleta, duration=0.8)
pyautogui.write('Novo Atleta')

#Modalidade
cModalidade = pyautogui.locateCenterOnScreen('modalidade.png', grayscale=True, confidence=0.9)
pyautogui.click(cModalidade, duration=0.8)
pyautogui.write('Nova Modalidade')

#Medalha
cMedalha = pyautogui.locateCenterOnScreen('medalha.png', grayscale=True, confidence=0.9)
pyautogui.click(cMedalha, duration=0.8)
pyautogui.write('Nova Medalha')

#rolagem
pyautogui.scroll(-250)
time.sleep(3)

#Comite
cComite = pyautogui.locateCenterOnScreen('comite.png', grayscale=True, confidence=0.9)
pyautogui.click(cComite, duration=0.8)
pyautogui.write('Nova Comite')

#Enviar
cEnviar = pyautogui.locateCenterOnScreen('enviar.png', grayscale=True, confidence=0.9)
pyautogui.click(cEnviar, duration=0.8)
