import RPi.GPIO as GPIO
import sys
import tkinter as tk
import time
import os
from consts import *

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

        # Timer setup
        self.root = tk.Tk()
        self.root.title("Jiant Genga")
        self.label = tk.Label(self.root, text="Press the green button to start", font=("Helvetica", 32))
        self.label.place(x=0, y=0)
        self.label.configure(bg="black")
        self.label.configure(fg="lime green")
        self.label.pack()

        self.root.mainloop()

    def countdown(self):
        #self.root.configure(height=576)
        #self.label.configure(width=10)
        allottedTime = 30.00
        self.label.configure(font=("Courier", 200))
        startTime = time.time()
        currTime = time.time()
        while currTime - startTime < allottedTime:
            currTime = time.time()

            # Player successfully made a move so restart the timer for the next player
            if GPIO.input(RED_BUTTON):
                startTime = time.time()
                currTime = time.time()

            if currTime >= startTime + allottedTime:
                self.label.configure(font=("Courier", 80))
                self.label.configure(text = "Time's up")
                self.b = tk.Button(self.root, text="OK", command=self.testcallback)
                self.b.pack()
                GPIO.cleanup()
            else:
                timeLeft = round(allottedTime - (currTime - startTime), 2)
                formattedTime = '{0:.2f}'.format(timeLeft)
                self.label.configure(text = formattedTime)
        

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
        self.root.title("Next player, please make a move")
        self.label.config(font=("Courier", 150))
        print("Next player please make a move...")
        self.countdown()


    # White button will be used to signal end of a player's turn and the start of another's turn. 
    def whiteButtonCallback(self, channel):
        print("White button was pushed")

