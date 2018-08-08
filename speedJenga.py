import RPi.GPIO as GPIO
import sys
import tkinter as tk
import time

class SpeedJenga:
    def __init__(self):
        #self.numPlayers = numPlayers
        #self.currentPlayer = 0

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)

        # Pin 10 will be the red button
        GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        GPIO.add_event_detect(10, GPIO.RISING, callback = self.greenButtonCallback, bouncetime=500)

        GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        GPIO.add_event_detect(18, GPIO.RISING, callback = self.whiteButtonCallback)

        GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        GPIO.add_event_detect(26, GPIO.RISING, callback = self.redButtonCallback)

        # Timer setup
        self.root = tk.Tk()
        self.root.title("Jiant Genga")
        self.label = tk.Label(self.root, text="press the green button to start", font=("Helvetica", 32))
        self.label.place(x=60, y=30)
        self.label.pack()

        self.root.mainloop()

    def countdown(self):
        self.p = 10.00
        self.t = time.time()
        self.n = time.time()
        while self.n - self.t < self.p:
            self.n = time.time()

            if GPIO.input(26):
                self.p = 10.00
                self.t = time.time()
                self.n = time.time()
                self.label.configure(font=("Courier", 150))
            if self.n >= self.t + self.p:
                self.label.config(font=("Courier", 80))
                self.label.configure(text = "Time's up")
                GPIO.cleanup()
            else:
                self.label.configure(text = round(10 - (self.n - self.t)))
        
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

