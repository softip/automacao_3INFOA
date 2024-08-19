#https://mouseaccuracy.com/
import pyautogui, sys

while True:
    try:
        ponto = pyautogui.locateCenterOnScreen('bolinha.png',
                                    grayscale=True,
                                    region=[0,89,846,591],
                                    confidence=0.9)
        pyautogui.click(ponto, duration=0.1)
    except KeyboardInterrupt:
        sys.exit()        
    except:
        print("Não encontrada bolinha")
