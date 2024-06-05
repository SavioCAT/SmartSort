import cv2
import keras
import numpy as np
from moteur import pilote_moteur
from time import sleep
from picture import photo 

class modele_IA:
    def __init__(self):
        self.model_path = "./model4juin.h5"
        self.image_path = "./picture/pic.jpg"
        self.class_name = ['assiette_carton', 'boite_carton', 'bouteille_plastique', 'bouteille_verre', 'brique_carton', 'canette_metal', 'conserve_metal', 'gobelet_carton']
        self.pic = photo()
        self.test_model = keras.models.load_model(self.model_path)

    def lecture_img(self):
        self.pic.prendre_photo()
        self.image = cv2.imread(self.image_path)
        self.image_normalized = self.image / 255.0
        self.image_batch = np.expand_dims(self.image_normalized, axis = 0)

        self.prediction = self.test_model.predict(self.image_batch)[0]
        self.prediction_argmax = np.argmax(self.prediction)
        self.predicted_label = self.class_name[self.prediction_argmax]

        print(self.class_name)
        print(self.prediction, "proba = ", self.prediction[self.prediction_argmax])
        print(self.predicted_label)
        
        if self.predicted_label.split("_")[1] == 'carton':
        	print("carton")
        	return 1
        elif self.predicted_label.split("_")[1] == 'plastique':
        	print("plastique")
        	return 2
        elif self.predicted_label.split("_")[1] == 'metal':
        	print("metal")
        	return 3
        else:
        	print("verre")
        	return 4
        



