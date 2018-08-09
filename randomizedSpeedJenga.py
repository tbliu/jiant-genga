import tkinter as tk
import RPi.GPIO as GPIO
import sys
import time
import random
from tkinter import simpledialog
#from picamera import PiCamera
from time import sleep
from speedJenga import SpeedJenga
from consts import *

class RandomizedSpeedJenga(SpeedJenga):
    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(GREEN_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(GREEN_BUTTON, GPIO.RISING, callback=self.greenButtonCallback, bouncetime=500)

        GPIO.setup(WHITE_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(WHITE_BUTTON, GPIO.RISING, callback=self.whiteButtonCallback, bouncetime=500)

        GPIO.setup(RED_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        #GPIO.add_event_detect(RED_BUTTON, GPIO.RISING, callback=self.redButtonCallback, bouncetime=1000)

        #self.camera = PiCamera()

        playersInput = simpledialog.askstring("Players", "Please type the names of all players separated by commas (like Tim,Bobby,Ge)")
        self.players = playersInput.split(",")
        self.index = 0

        self.root = tk.Tk()
        self.root.title("Jiant Genga")
        self.label = tk.Label(self.root, text="Press the green button to start", font=("Helvetica", 32))
        self.label.place(x=60,y=30)
        self.label.pack()

        self.root.mainloop()

    def onClose(self, widget):
        if (tk.messagebox.askokcancel("Quit", "Do you want to quit?")):
            widget.grid_remove()
            GPIO.cleanup()

    def countdown(self):
        allottedTime = 30.00
        self.startTime = time.time()
        self.currTime = time.time()
        prev_input = 1
        while self.currTime - self.startTime < allottedTime:
            self.currTime = time.time()

            # Player made a successful move
            curr_input = GPIO.input(RED_BUTTON)
            if (not prev_input) and curr_input and self.index < len(self.players):
                self.player = self.players[self.index]
                self.index += 1
                self.startTime = time.time()
                self.currTime = time.time()
            elif (not prev_input) and curr_input and self.index >= len(self.players):
                self.index = 0
                random.shuffle(self.players)
                self.player = self.players[self.index]
                self.index += 1
                self.startTime = time.time()
                self.currTime = time.time()
            
            if self.currTime >= self.startTime + allottedTime:
                self.label.configure(font=("Courier", 80))
                self.label.configure(text = "Time's up")
                GPIO.cleanup()
            else:
                self.label.configure(font=("Courier", 64))
                timeLeft = round(allottedTime - (self.currTime - self.startTime))
                self.label.configure(text = "Player:\n " + self.player + "\n" + str(timeLeft))
            prev_input = curr_input

    def redButtonCallback(self, channel):
        return

    def greenButtonCallback(self, channel):
        self.player = self.players[self.index]
        self.index += 1
        self.countdown()

    def whiteButtonCallback(self, channel):
        return

