from time import sleep
from machine import Pin, PWM

class controleur_moteur:
    def __init__(self):
        self.pwm_moteur1 = PWM(Pin(16))
        self.pwm_moteur2 = PWM(Pin(18))
        self.pwm_moteur3 = PWM(Pin(20))
        self.pwm_moteur4 = PWM(Pin(22))

        #Initialiser des PWM aux bonnes fréquences
        self.pwm_moteur1.freq(50)
        self.pwm_moteur2.freq(50)
        self.pwm_moteur3.freq(50)
        self.pwm_moteur4.freq(50)

        self.reset_moteur()

    #Ce bout de code permet de régler les sortie PWM plus simplement et de ne pas a avoir à gérer la galère qu'est d'utiliser une valeur entre
    def set_duty(self, moteur: int, duty: float) -> None:
        try:
            if duty > 100 or duty < 0 or moteur > 4 or moteur < 1:
                raise ValueError("duty should be between 0 and 100 and moteur should be an integer betwen 1 and 4")
            if not isinstance(moteur, int) or not isinstance(duty, float):
                raise TypeError("duty should be float and moteur should be int")
            if moteur == 1:
                self.pwm_moteur1.duty_u16(round(65535 / 100 * duty))
            elif moteur == 2:
                self.pwm_moteur2.duty_u16(round(65535 / 100 * duty))
            elif moteur == 3:
                self.pwm_moteur3.duty_u16(round(65535 / 100 * duty))
            elif moteur == 4:
                self.pwm_moteur4.duty_u16(round(65535 / 100 * duty))
        except TypeError as e:
            print(f"TypeErro: {e}")
        except ValueError as e:
            print(f"ValueError: {e}")

    def reset_moteur(self) -> None:
        for i in range(1, 5):
            self.set_duty(i, 50)

