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
        com_interface.attente_user()
        match decision:
            case 'choix_user_poubelle_1':
                moteur.jeter_dechet(1)
                com_interface.ajout_poubelle_1()
                break
            case 'choix_user_poubelle_2':
                moteur.jeter_dechet(2)
                com_interface.ajout_poubelle_2()
                break
            case 'choix_user_poubelle_3':
                moteur.jeter_dechet(3)
                com_interface.ajout_poubelle_3()
                break
            case 'choix_user_poubelle_4':
                moteur.jeter_dechet(4)
                com_interface.ajout_poubelle_4()
                break
            case _:
                print('choix invalide')

if __name__ == "__main__" :

    # ['waiting', 'stop', 'running'] Juste pour garder en tete les etats existants
    state_statut = 2

    ia_mod = modele_IA()
    moteur = logique()
    ultrason_plateau = ultrason_logique()
    com_interface = communication()
    distance_plateau = 100

    while True:
        sleep(0.01)
        while True:
            match state_statut:
                case 0:
                    com_interface.attente_objet()
                    sleep(100)
                    break
                case 1:
                    break
                case 2:
                    resultat = ia_mod.lecture_img()
                    com_interface.traitement_objet_en_cours()
                    if resultat is not None:
                        if resultat[0] == 1:
                            if resultat[1] < 0.99: # PENSER A MODIFIER
                                incertain()
                            else:
                                com_interface.ajout_poubelle_1()
                                sleep(0.3)
                            print("Carton")
                            state_statut = 0
                        elif resultat[0] == 2:
                            if resultat[1] < 0.99:
                                incertain()
                            else:
                                com_interface.ajout_poubelle_2()
                                sleep(0.3)
                            print("plastique")
                            state_statut = 0
                        elif resultat[0] == 3:
                            if resultat[1] < 0.99:
                                incertain()
                            else:
                                com_interface.ajout_poubelle_3()
                                sleep(0.3)
                            print("metal")
                            state_statut = 0
                        elif resultat[0] == 4:
                            if resultat[1] < 0.99:
                                incertain()
                            else:
                                com_interface.ajout_poubelle_4()
                                sleep(0.3)
                            print("Verre")
                            state_statut = 0
                        else:
                            print("Prédiction inconnue")
                    else:
                        print("Impossible de faire une prédiction")
                    break
                case _:
                    break
