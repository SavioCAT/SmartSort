import RPi.GPIO as GPIO
from time import sleep, time


class ultrason_logique:
    def __init__(self):
        self.GPIO.setmode(GPIO.BOARD)
        self.GPIO.setwarnings(False)

        self.GPIO.setup(38, GPIO.OUT)
        self.GPIO.setup(40, GPIO.IN)

        self.GPIO.output(38, GPIO.LOW)

    def distance(self) -> float:
        self.GPIO.output(38, GPIO.HIGH)
        sleep(0.00001)
        self.GPIO.output(38, GPIO.LOW)

        while self.GPIO.input(40) == 0:
            start = time.time()

        while self.GPIO.input(40) == 1:
            stop = time.time()

        elapsed = stop - start
        distance = (elapsed * 34300) / 2

        return distance