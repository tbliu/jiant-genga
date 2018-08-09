import RPi.GPIO as GPIO
import sys
import tkinter as tk
import time
import os
from consts import *
import pygame

class SpeedJenga:
    def __init__(self):
        #self.numPlayers = numPlayers
        #self.currentPlayer = 0

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
        self.label = tk.Label(self.root, text="press the green button to start", font=("Helvetica", 32))
        self.label.place(x=60, y=30)
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
        self.label.configure(text = "Ready...")
        self.playSound("ready.mp3")
        time.sleep(4)
        self.playSound("Jeopardy-theme-song.mp3")
        allottedTime = 30.00
        startTime = time.time()
        currTime = time.time()
        while currTime - startTime < allottedTime:
            currTime = time.time()

            # Player successfully made a move so restart the timer for the next player
            if GPIO.input(RED_BUTTON):
                startTime = time.time()
                currTime = time.time()
                self.playSound("Jeopardy-theme-song.mp3")

            if currTime >= startTime + allottedTime:
                self.label.configure(font=("Courier", 80))
                self.label.configure(text = "Time's up")
                self.pauseSound()
                self.playSound("lose.mp3")
                self.b = tk.Button(self.root, text="OK", command=self.testcallback)
                self.b.pack()
                GPIO.cleanup()
            else:
                timeLeft = round(allottedTime - (currTime - startTime))
                self.label.configure(text = timeLeft)
        

    def testcallback(self):
        self.root.destroy()
        os.system("python3 start.py")

        
    # Red button will be used to end games
    def redButtonCallback(self, channel):
        print("Red button pushed down")
        #GPIO.cleanup()
        #sys.exit(0)

    # Green button will be used to start games
    def greenButtonCallback(self, channel):
        print("green button pressed")
        self.root.title("Next player, please make a move")
        self.label.config(font=("Courier", 150))
        self.countdown()


    # White button will be used to signal end of a player's turn and the start of another's turn. 
    def whiteButtonCallback(self, channel):
        print("White button was pushed")

