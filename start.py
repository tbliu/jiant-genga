import tkinter as tk
from tkinter import simpledialog
from speedJenga import SpeedJenga
from randomizedSpeedJenga import RandomizedSpeedJenga
import RPi.GPIO as GPIO
from consts import *

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(GREEN_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(GREEN_BUTTON, GPIO.RISING, callback = lambda: RandomizedSpeedJenga(), bouncetime=500)

GPIO.setup(RED_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(RED_BUTTON, GPIO.RISING, callback = lambda; SpeedJenga(), bouncetime=500)

root = tk.Tk()
label = tk.Label(root, width=768, height=576, text="Press the green button for Randomized Speed Jenga. Press the right button for Normal Speed Jenga", font=("Helvetica", 32))
#frame = tk.Frame(root, width=768, height=576)
#frame.pack()
#speedJengaButton = tk.Button(frame, text= "Speed Jenga", font=("Helvetica", 18), height="30", width="30", command=lambda: SpeedJenga())
#speedJengaButton.pack(side = tk.LEFT)

#randomizedJengaButton = tk.Button(frame, text = "Randomized Speed Jenga", font=("Helvetica", 18), height="30", width="30", command=lambda: RandomizedSpeedJenga())
#randomizedJengaButton.pack(side = tk.RIGHT)

tk.mainloop()
