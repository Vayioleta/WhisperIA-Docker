Tarea = "Transcript to Language" #@param ["Transcript to Language", "Translate to English"]
import os
import numpy as np
import whisper
from scipy.io.wavfile import write
from IPython.display import clear_output

task = "translate" if Tarea == "Translate to English" else "transcribe" 

audio, sr = get_audio()
write('record.wav', sr, audio)

!whisper "record.wav" --task {task} --model medium --verbose False

clear_output()
if task == "translate":
  print("-- TRADUCCIÓN A INGLÉS --\n")
else:
  print("-- TRANSCRIPCIÓN A ESPAÑOL --\n")
  
print(open('record.wav.txt').read())