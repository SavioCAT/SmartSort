from intelligence import modele_IA
from time import sleep
from moteur import pilote_moteur


if __name__ == "__main__" :
    
    ia_mod = modele_IA
    
    resultat = ia_mod.lecture_img()
    
    if resultat is not None :
        if resultat[0] == 1 :
        	print("Carton")
        elif resultat[0] == 2 :
        	print("plastique")
        elif resultat[0] == 3 :
        	print("metal")
        elif resultat[0] == 4 :
        	print("Verre")
        else :
        print("Prédiction inconnue")
    else :
        print("Impossible de faire une prédiction")