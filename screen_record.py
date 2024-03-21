import cv2
import numpy as np
import pyautogui
import keyboard

# Frames 
fps = 60
#resolution = pyautogui.size()
resolution = (1920, 1080)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('grabacion.mp4', fourcc, fps, resolution)

print('Iniciando Grabacion...')

while True:
    frame = np.array(pyautogui.screenshot())
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)
    
    if keyboard.is_pressed('q'):
        break
    
print('Grabacion finalizada')
out.release()
cv2.destroyAllWindows()

