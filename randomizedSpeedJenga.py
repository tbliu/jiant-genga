import tkinter as tk
import RPi.GPIO as GPIO
import sys
import time
import random
from tkinter import simpledialog
from picamera import PiCamera
from time import sleep
from speedJenga import SpeedJenga
from consts import *

class RandomizedSpeedJenga(SpeedJenga):
    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(GREEN_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(GREEN_BUTTON, GPIO.RISING, callback=lambda: 3, bouncetime=500)

        GPIO.setup(WHITE_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(WHITE_BUTTON, GPIO.RISING, callback=lambda: 3, bouncetime=500)

        GPIO.setup(RED_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(RED_BUTTON, GPIO.RISING, callback=lambda: 3, bouncetime=500)

        self.camera = PiCamera()

        playersInput = simpledialog.askstring("Players", "Please type the names of all players separated by commas (like Tim,Bobby,Ge)")
        self.players = playersInput.split(",")
        self.numPlayers = len(self.players)
        self.movesThisTurn = 0

        self.root = tk.Tk()
        self.root.title("Jiant Genga")
        self.label = tk.Label(self.root, text="press the green button to start", font=("Helvetica", 32))
        self.label.place(x=60,y=30)
        self.label.pack()

        self.root.mainloop()

    def countdown(self):
        return

    def redButtonCallback(self, channel):
        return

    def greenButtonCallback(self, channel):
        return

    def whiteButtonCallback(self, channel):
        return

