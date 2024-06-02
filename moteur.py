from time import sleep
from machine import Pin, PWM

###############################################
#                                             #
# Code à destination d'une raspberry pi pico  #
#                                             #
###############################################

#initialisation des pins
pwm_moteur1 = PWM(Pin(16))
pwm_moteur2 = PWM(Pin(18))
pwm_moteur3 = PWM(Pin(20))
pwm_moteur4 = PWM(Pin(22))

pin_comm_pi5_bit0 = Pin(13, Pin.IN, Pin.PULL_DOWN)
pin_comm_pi5_bit1 = Pin(14, Pin.IN, Pin.PULL_DOWN)
pin_comm_pi5_declancheur = Pin(15, Pin.IN, Pin.PULL_DOWN)

#Initialiser des PWM aux bonnes fréquences
pwm_moteur1.freq(50)
pwm_moteur2.freq(50)
pwm_moteur3.freq(50)
pwm_moteur4.freq(50)


def set_duty(moteur: int, duty: float) -> None:
    try:
        if duty > 100 or duty < 0 or moteur > 4 or moteur < 1:
            raise ValueError("duty should be between 0 and 100 and moteur should be an integer betwen 1 and 4")
        if not isinstance(moteur, int) or not isinstance(duty, float):
            raise TypeError("duty should be float and moteur should be int")
        if moteur == 1:
            pwm_moteur1.duty_u16(round(9830 / 100 * duty))
        elif moteur == 2:
            pwm_moteur2.duty_u16(round(9830 / 100 * duty))
        elif moteur == 3:
            pwm_moteur3.duty_u16(round(9830 / 100 * duty))
        elif moteur == 4:
            pwm_moteur4.duty_u16(round(9830 / 100 * duty))
    except TypeError as e:
        print(f"TypeErro: {e}")
    except ValueError as e:
        print(f"ValueError: {e}")


def reset_moteur() -> None:
    for i in range(1, 5):
        set_duty(i, 50)


reset_moteur()
