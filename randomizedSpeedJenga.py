import tkinter as tk
import RPi.GPIO as GPIO
import sys
import os
import time
import random
from tkinter import simpledialog
from time import sleep
from speedJenga import SpeedJenga
from consts import *
import pygame

class RandomizedSpeedJenga(SpeedJenga):
    def __init__(self):
        playersInput = simpledialog.askstring("Players", "Please type the names of all players separated by commas (like Tim,Bobby,Ge)")
        self.players = playersInput.split(",")
        self.index = 0
        self.roundNumber = 1
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(GREEN_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(GREEN_BUTTON, GPIO.RISING, callback=self.greenButtonCallback, bouncetime=500)

        GPIO.setup(WHITE_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(WHITE_BUTTON, GPIO.RISING, callback=self.whiteButtonCallback, bouncetime=500)

        GPIO.setup(RED_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        pygame.init()

        self.root = tk.Tk()
        self.root.title("Jiant Genga")
        self.label = tk.Label(self.root, text="Press the green button to start", font=("Helvetica", 32))
        self.label.place(x=60,y=30)
        self.label.configure(fg="lime green")
        self.label.configure(bg="black")
        self.label.pack()

        self.root.mainloop()


    def countdown(self):
        self.label.configure(font=("Courier", 120))
        self.label.configure(text="Ready...")
        self.playSound("/home/pi/jiant-genga/ready.mp3")
        time.sleep(4)
        self.label.configure(text = "GO!")
        time.sleep(1)
        self.playSound("/home/pi/jiant-genga/Jeopardy-theme-song.mp3")
        allottedTime = 30.00
        self.startTime = time.time()
        self.currTime = time.time()
        prev_input = 1
        while self.currTime - self.startTime < allottedTime:
            self.currTime = time.time()

            # Player made a successful move
            curr_input = GPIO.input(RED_BUTTON)
            time.sleep(0.025)
            if (not prev_input) and curr_input and self.index < len(self.players):
                self.player = self.players[self.index]
                self.index += 1
                self.playSound("/home/pi/jiant-genga/Jeopardy-theme-song.mp3")
                self.startTime = time.time()
                self.currTime = time.time()
            # All players this round have went. Reshuffle the list and start again
            elif ((not prev_input) and curr_input) or self.index >= len(self.players):
                self.index = 0
                random.shuffle(self.players)
                self.player = self.players[self.index]
                self.index += 1
                self.roundNumber += 1
                self.startTime = time.time()
                self.currTime = time.time()
            else:
                self.player = self.players[self.index]
            
            if self.currTime >= self.startTime + allottedTime:
                self.label.configure(font=("Courier", 80))
                self.label.configure(text = "Time's up")
                self.pauseSound()
                self.playSound("/home/pi/jiant-genga/buzz.mp3")
                self.b = tk.Button(self.root, text="Press the white button to return to main menu", command=lambda: self.whiteButtonCallback(WHITE_BUTTON))
                self.b.pack()
                GPIO.cleanup()
            else:
                self.label.configure(font=("Courier", 64))
                timeLeft = round(allottedTime - (self.currTime - self.startTime), 2)
                formattedTime = "{:04.2f}".format(timeLeft)
                self.label.configure(text = "Player: " + self.player + "\n\n" + str(formattedTime)+ "\nRound " + str(self.roundNumber))
            prev_input = curr_input

    def whiteButtonCallback(self, channel):
        self.root.destroy()
        os.system("python3 /home/pi/jiant-genga/start.py")

    def greenButtonCallback(self, channel):
        self.root.title("Randomized Jenga")
        self.countdown()

