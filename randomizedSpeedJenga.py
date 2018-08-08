import tkinter as tk
import RPi.GPIO as GPIO
import sys
import time
from picamera import PiCamera
from time import sleep
from speedJenga import SpeedJenga
from consts import *
from PIL import Image, ImageTK

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
        self.takePictures()

    def takePictures(self):
        self.camera.start_preview()
        sleep(10)
        self.camera.stop_preview()

