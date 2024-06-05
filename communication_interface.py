from time import sleep
import RPi.GPIE as GPIO

class communication:
	def __init__(self):
		self.GPIO.setmode(GPIO.BOARD)
        self.GPIO.setwarnings(False)
        
        self.GPIO.setup(11, GPIO.IN)
        self.GPIO.setup(13, GPIO.IN)
        self.GPIO.setup(15, GPIO.IN)
        self.GPIO.setup(19, GPIO.IN)
        
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
