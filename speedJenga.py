import RPi.GPIO as GPIO
import sys

class SpeedJenga:
    def __init__(self, numPlayers):
        self.numPlayers = numPlayers
        self.currentPlayer = 0

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)

        # Pin 10 will be the red button
        GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        GPIO.add_event_detect(10, GPIO.RISING, callback = self.greenButtonCallback, bouncetime=500)

        GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        GPIO.add_event_detect(18, GPIO.RISING, callback = self.whiteButtonCallback)

        GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        GPIO.add_event_detect(26, GPIO.RISING, callback = self.redButtonCallback)

    # Red button will be used to end games
    def redButtonCallback(self, channel):
        print("Red button was pushed")
        GPIO.cleanup()
        sys.exit(0)

    # Green button will be used to start games
    def greenButtonCallback(self, channel):
        print("Player " + str(self.currentPlayer) + " successfully made a move")
        self.currentPlayer = (self.currentPlayer + 1) % self.numPlayers
        print("New current player is now " + str(self.currentPlayer))
        # TODO: RESET TIMER LOGIC


    # White button will be used to signal end of a player's turn and the start of another's turn. 
    def whiteButtonCallback(self, channel):
        print("White button was pushed")

