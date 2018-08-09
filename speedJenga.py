import RPi.GPIO as GPIO
import sys
import tkinter as tk
import time
import os
from consts import *
import pygame

class SpeedJenga:
    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(GREEN_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(GREEN_BUTTON, GPIO.RISING, callback = self.greenButtonCallback, bouncetime=500)

        GPIO.setup(WHITE_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(WHITE_BUTTON, GPIO.RISING, callback = self.whiteButtonCallback)

        GPIO.setup(RED_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(RED_BUTTON, GPIO.RISING, callback = self.redButtonCallback)

        # sound player set up
        pygame.init()
        
        # Timer setup
        self.root = tk.Tk()
        self.root.title("Jiant Genga")
        self.label = tk.Label(self.root, text="Press the green button to start", font=("Courier", 24))
        self.label.place(x=25,y=25, anchor="center")
        self.label.configure(fg="lime green")
        self.label.configure(bg="black")
        self.label.pack()
        self.root.mainloop()

    def playSound(self, song):
        pygame.mixer.music.load(song)
        print("start playing sound")
        pygame.mixer.music.play(0)

    def pauseSound(self):
        pygame.mixer.pause()
        print("paused sound")

    def countdown(self):
        self.label.configure(font=("Courier", 120))
        self.label.configure(text = "Ready...")
        self.playSound("/home/pi/jiant-genga/ready.mp3")
        time.sleep(4)
        self.label.configure(text = "GO!")
        time.sleep(1)
        self.playSound("/home/pi/jiant-genga/Jeopardy-theme-song.mp3")
        allottedTime = 30.00
        startTime = time.time()
        currTime = time.time()
        while currTime - startTime < allottedTime:
            currTime = time.time()

            # Player successfully made a move so restart the timer for the next player
            if GPIO.input(RED_BUTTON):
                startTime = time.time()
                currTime = time.time()
                self.playSound("/home/pi/jiant-genga/Jeopardy-theme-song.mp3")

            if currTime >= startTime + allottedTime:
                self.label.configure(font=("Courier", 80))
                self.label.configure(text = "Time's up")
                self.pauseSound()
                self.playSound("/home/pi/jiant-genga/buzz.mp3")
                self.b = tk.Button(self.root, text="Press the white button to return to main menu", command=lambda: self.whiteButtonCallback(WHITE_BUTTON))
                self.b.pack()
                GPIO.cleanup()
            else:
                timeLeft = round(allottedTime - (currTime - startTime), 2)
                formattedTime = "{:04.2f}".format(timeLeft)
                self.label.configure(text = formattedTime)
        

    def whiteButtonCallback(self, channel):
        self.root.destroy()
        os.system("python3 start.py")

    # Red button will be used to end games
    def redButtonCallback(self, channel):
        print("Red button pushed down")

    # Green button will be used to start games
    def greenButtonCallback(self, channel):
        self.root.title("Next player, please make a move")
        self.label.config(font=("Courier", 150))
        self.countdown()

