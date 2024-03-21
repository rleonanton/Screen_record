import cv2
import numpy as np 
import pyautogui
import keyboard
import pyaudio
import wave

# Configuración de grabación de vídeo
fps = 10
resolution = pyautogui.size()
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('grabacion_con_audio.mp4', fourcc, fps, resolution)

# Configuración de grabación de audio
audio_format = pyaudio.paInt16  # Formato de audio
channels =  1 # Número de canales (estéreo)
sample_rate = 44100  # Tasa de muestreo (muestras por segundo)
chunk_size = 1024  # Tamaño del búfer de audio
audio_duration = 10  # Duración del audio en segundos

p = pyaudio.PyAudio()
stream = p.open(format=audio_format,
                channels=channels,
                rate=sample_rate,
                input=True,
                frames_per_buffer=chunk_size)

frames = []

# Inicio de la grabación
print("Iniciando grabación...")

while True:
    frame = np.array(pyautogui.screenshot())
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)
    
    # Capturar audio
    data = stream.read(chunk_size)
    frames.append(data)
    
    if keyboard.is_pressed('q'):
        break

# Detener la grabación
print("Deteniendo grabación...")

# Guardar el archivo de audio
stream.stop_stream()
stream.close()
p.terminate()

audio_output_filename = 'grabacion_audio.wav'
wf = wave.open(audio_output_filename, 'wb')
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(audio_format))
wf.setframerate(sample_rate)
wf.writeframes(b''.join(frames))
wf.close()

out.release()
cv2.destroyAllWindows()

print("Grabación completa. Archivos de vídeo y audio guardados.")
