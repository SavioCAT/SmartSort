#import RPi.GPIE as GPIO
from time import sleep

class logique:
    def __init__(self):
        self.GPIO.setmode(GPIO.BOARD)
        self.GPIO.setwarnings(False)

        self.GPIO.setup(3, GPIO.OUT)
        self.GPIO.setup(5, GPIO.OUT)
        self.GPIO.setup(7, GPIO.OUT)

    def pb_plastique(self):
        self.GPIO.output(3, GPIO.LOW)
        self.GPIO.output(5, GPIO.LOW)
        self.GPIO.output(7, GPIO.HIGH)
        sleep(3)
        self.GPIO.cleanup()

    def pb_papier(self):
        self.GPIO.output(3, GPIO.HIGH)
        self.GPIO.output(5, GPIO.LOW)
        self.GPIO.output(7, GPIO.HIGH)
        sleep(3)
        self.GPIO.cleanup()

    def pb_metal(self):
        self.GPIO.output(3, GPIO.LOW)
        self.GPIO.output(5, GPIO.HIGH)
        self.GPIO.output(7, GPIO.HIGH)
        sleep(3)
        self.GPIO.cleanup()

    def pb_verre(self):
        self.GPIO.output(3, GPIO.HIGH)
        self.GPIO.output(5, GPIO.HIGH)
        self.GPIO.output(7, GPIO.HIGH)
        sleep(3)
        self.GPIO.cleanup()

    def jeter_dechet(self, code = 5):
        if code == 1:
            self.pb_plastique()
        elif code == 2:
            self.pb_papier()
        elif code == 3:
            self.pb_metal()
        elif code == 4:
            self.pb_verre()
        else:
            print("Code non reconnu")