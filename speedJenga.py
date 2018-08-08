import RPi.GPIO as GPIO

# Red button will be used to end games
def redButtonCallback(channel):
    print("Red button was pushed")

# Green button will be used to start games
def greenButtonCallback(channel):
    print("Green button was pushed")

# White button will be used to signal end of a player's turn and the start of another's turn. 
def whiteButtonCallback(channel):
    print("White button was pushed")

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# Pin 10 will be the red button
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(10, GPIO.RISING, callback = redButtonCallback)

message = input("Playing Jenga")

GPIO.cleanup()
