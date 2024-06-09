from intelligence import modele_IA
from time import sleep
from logique_moteur import logique

if __name__ == "__main__" :

    state = ['waiting', 'stop', 'running', 'traitement_dechet']
    state_statut = 0

    ia_mod = modele_IA()
    moteur = logique()

    while True:
        sleep(0.01)
        match state_statut:
            case 0:
                break
            case 1:
                break
            case 2:
                break
            case 3:
                break




        resultat = ia_mod.lecture_img()

        if resultat is not None:
            if resultat[0] == 1:
                print("Carton")
            elif resultat[0] == 2:
                print("plastique")
            elif resultat[0] == 3:
                print("metal")
            elif resultat[0] == 4:
                print("Verre")
            else:
                print("Prédiction inconnue")
        else:
            print("Impossible de faire une prédiction")