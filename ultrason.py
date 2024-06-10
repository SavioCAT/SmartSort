import RPi.GPIO as GPIO
from time import sleep, time


class ultrason_logique:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)

        GPIO.setup(38, GPIO.OUT)
        GPIO.setup(40, GPIO.IN)

        GPIO.output(38, GPIO.LOW)

    def distance(self) -> float:
        GPIO.output(38, GPIO.HIGH)
        leep(0.00001)
        GPIO.output(38, GPIO.LOW)

        while GPIO.input(40) == 0:
            start = time.time()

        while GPIO.input(40) == 1:
            stop = time.time()

        elapsed = stop - start
        distance = (elapsed * 34300) / 2

        return distance