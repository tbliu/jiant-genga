import RPi.GPIO as GPIO
import sys
import tkinter as tk

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
        self.label = tk.Label(self.root, text="null")
        self.label.place(x=35, y=15)
        self.label.pack()

        self.countdown(5)

        self.root.mainloop()

    def countdown(self, count):
        #self.label['test'] = count
        self.label.configure(text=str(count))

        if count > 0:
            self.root.after(1000, self.countdown, count-1)

    # Red button will be used to end games
    def redButtonCallback(self, channel):
        print("Red button was pushed")
        GPIO.cleanup()
        sys.exit(0)

    # Green button will be used to start games
    def greenButtonCallback(self, channel):
        print("Player successfully made a move")
        print("Next player please make a move...")
        # TODO: RESET TIMER LOGIC


    # White button will be used to signal end of a player's turn and the start of another's turn. 
    def whiteButtonCallback(self, channel):
        print("White button was pushed")

