from intelligence import modele_IA
from time import sleep
from logique_moteur import logique
from ultrason import ultrason_logique
from communication_interface import communication

def incertain():
    print("resultat incertain, attente action opérateur.")
    while True:
        sleep(0.01)
        decision = com_interface.look_for_input()
        match decision:
            case 'choix_user_poubelle_1':
                moteur.jeter_dechet(1)
                break
            case 'choix_user_poubelle_2':
                moteur.jeter_dechet(2)

                break
            case 'choix_user_poubelle_3':
                moteur.jeter_dechet(3)

                break
            case 'choix_user_poubelle_4':
                moteur.jeter_dechet(4)

                break
            case _:
                print('choix invalide')

if __name__ == "__main__" :

    # ['waiting', 'stop', 'running'] Juste pour garder en tete les etats existants
    state_statut = 0

    ia_mod = modele_IA()
    moteur = logique()
    ultrason_plateau = ultrason_logique()
    com_interface = communication()
    distance_plateau = 100

    while True:
        sleep(0.01)
        match state_statut:
            case 0:

                break
            case 1:
                break
            case 2:
                resultat = ia_mod.lecture_img()

                if resultat is not None:
                    if resultat[0] == 1:
                        if resultat[1] < 0.70:
                            incertain()
                        print("Carton")
                        state_statut = 0
                    elif resultat[0] == 2:
                        if resultat[1] < 0.70:
                            incertain()
                        print("plastique")
                        state_statut = 0
                    elif resultat[0] == 3:
                        if resultat[1] < 0.70:
                            incertain()
                        print("metal")
                        state_statut = 0
                    elif resultat[0] == 4:
                        if resultat[1] < 0.70:
                            incertain()
                        print("Verre")
                        state_statut = 0
                    else:
                        print("Prédiction inconnue")
                else:
                    print("Impossible de faire une prédiction")
                break
            case _:
                break