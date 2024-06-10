import RPi.GPIO as GPIO
from time import sleep

class logique:
    
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)

        GPIO.setup(3, GPIO.OUT)
        GPIO.setup(5, GPIO.OUT)
        GPIO.setup(7, GPIO.OUT)

    def pb_plastique(self) -> None:
        GPIO.output(3, GPIO.LOW)
        GPIO.output(5, GPIO.LOW)
        GPIO.output(7, GPIO.HIGH)
        sleep(3)
        GPIO.cleanup()

    def pb_papier(self) -> None:
        GPIO.output(3, GPIO.HIGH)
        GPIO.output(5, GPIO.LOW)
        GPIO.output(7, GPIO.HIGH)
        sleep(3)
        GPIO.cleanup()

    def pb_metal(self) -> None:
        GPIO.output(3, GPIO.LOW)
        GPIO.output(5, GPIO.HIGH)
        GPIO.output(7, GPIO.HIGH)
        sleep(3)
        GPIO.cleanup()

    def pb_verre(self) -> None:
        GPIO.output(3, GPIO.HIGH)
        GPIO.output(5, GPIO.HIGH)
        GPIO.output(7, GPIO.HIGH)
        sleep(3)
        GPIO.cleanup()

    def jeter_dechet(self, code = 5) -> None:
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
