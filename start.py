import tkinter as tk
from tkinter import simpledialog
from speedJenga import SpeedJenga
from randomizedSpeedJenga import RandomizedSpeedJenga
import RPi.GPIO as GPIO
from consts import *

def speedJengaCallback(channel):
    GPIO.remove_event_detect(RED_BUTTON)
    GPIO.remove_event_detect(WHITE_BUTTON)
    GPIO.remove_event_detect(GREEN_BUTTON)
    GPIO.cleanup()
    return SpeedJenga()

def randomizedJengaCallback(channel):
    GPIO.remove_event_detect(RED_BUTTON)
    GPIO.remove_event_detect(WHITE_BUTTON)
    GPIO.remove_event_detect(GREEN_BUTTON)
    GPIO.cleanup()
    return RandomizedSpeedJenga()

def getHelpCallback(channel):
    tk.messagebox.showinfo("Help", "For both games: \nPress the green button when prompted to start the game.\nPress the red button if you made a successful move.\nPress the white button when the game ends to return to main menu.")

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(GREEN_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(GREEN_BUTTON, GPIO.RISING, callback = randomizedJengaCallback, bouncetime=500)

GPIO.setup(RED_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(RED_BUTTON, GPIO.RISING, callback = speedJengaCallback, bouncetime=500)

GPIO.setup(WHITE_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(WHITE_BUTTON, GPIO.RISING, callback = getHelpCallback, bouncetime=500)

root = tk.Tk()
label = tk.Label(root, width=768, height=576, text="Press the green button for Randomized Speed Jenga. \nPress the red button for Normal Speed Jenga. \nPress the white button for instructions", font=("Helvetica", 24))
label.pack()

tk.mainloop()
