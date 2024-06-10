from time import sleep
import RPi.GPIO as GPIO

class communication:
    def __init__(self):
        self.GPIO.setmode(GPIO.BOARD)
        self.GPIO.setwarnings(False)
        
        self.GPIO.setup(11, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        self.GPIO.setup(13, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        self.GPIO.setup(15, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        self.GPIO.setup(19, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        
        self.GPIO.setup(8, GPIO.OUT)
        self.GPIO.setup(10, GPIO.OUT)
        self.GPIO.setup(12, GPIO.OUT)
        
    def attente_objet(self) -> None:
        self.GPIO.output(8, GPIO.LOW)
        self.GPIO.output(10, GPIO.LOW)
        self.GPIO.output(12, GPIO.LOW)

    def attente_user(self) -> None:
        self.GPIO.output(8, GPIO.HIGH)
        self.GPIO.output(10, GPIO.LOW)
        self.GPIO.output(12, GPIO.LOW)
        
    def traitement_objet_en_cours(self) -> None:
        self.GPIO.output(8, GPIO.LOW)
        self.GPIO.output(10, GPIO.HIGH)
        self.GPIO.output(12, GPIO.LOW)
        
    def ajout_poubelle_1(self) -> None:
        self.GPIO.output(8, GPIO.HIGH)
        self.GPIO.output(10, GPIO.HIGH)
        self.GPIO.output(12, GPIO.LOW)
        
    def ajout_poubelle_2(self) -> None:
        self.GPIO.output(8, GPIO.LOW)
        self.GPIO.output(10, GPIO.LOW)
        self.GPIO.output(12, GPIO.HIGH)
        
    def ajout_poubelle_3(self) -> None:
        self.GPIO.output(8, GPIO.HIGH)
        self.GPIO.output(10, GPIO.LOW)
        self.GPIO.output(12, GPIO.HIGH)
        
    def ajout_poubelle_4(self) -> None:
        self.GPIO.output(8, GPIO.HIGH)
        self.GPIO.output(10, GPIO.HIGH)
        self.GPIO.output(12, GPIO.HIGH)
        
    def look_for_input(self):
        if GPIO.input(11) == 0 and GPIO.input(13) == 0 and GPIO.input(15) == 0 and GPIO.input(19) == 0:
            return 'langue_1'
        elif GPIO.input(11) == 0 and GPIO.input(13) == 0 and GPIO.input(15) == 0 and GPIO.input(19) == 1:
            return 'langue_2'
        elif GPIO.input(11) == 0 and GPIO.input(13) == 0 and GPIO.input(15) == 1 and GPIO.input(19) == 0:
            return 'langue_3'
        elif GPIO.input(11) == 0 and GPIO.input(13) == 1 and GPIO.input(15) == 0 and GPIO.input(19) == 1:
            return 'arret'
        elif GPIO.input(11) == 0 and GPIO.input(13) == 1 and GPIO.input(15) == 1 and GPIO.input(19) == 0:
            return 'choix_user_poubelle_1'
        elif GPIO.input(11) == 0 and GPIO.input(13) == 1 and GPIO.input(15) == 1 and GPIO.input(19) == 1:
            return 'choix_user_poubelle_2'
        elif GPIO.input(11) == 1 and GPIO.input(13) == 0 and GPIO.input(15) == 0 and GPIO.input(19) == 0:
            return 'choix_user_poubelle_3'
        elif GPIO.input(11) == 1 and GPIO.input(13) == 0 and GPIO.input(15) == 0 and GPIO.input(19) == 1:
            return 'choix_user_poubelle_4'
        elif GPIO.input(11) == 1 and GPIO.input(13) == 0 and GPIO.input(15) == 1 and GPIO.input(19) == 0:
            return 'lancement_manuel'
        elif GPIO.input(11) == 1 and GPIO.input(13) == 1 and GPIO.input(15) == 1 and GPIO.input(19) == 1:
            return 'reset'
        else:
            return 'erreur'
