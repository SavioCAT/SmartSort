import subprocess
from PIL import Image
import cv2
from time import sleep

class photo:

    #choqué de fou, cette fonction sert à prendre une photo. :O
    def prendre_photo(self):
        try:
	        result = subprocess.run(['libcamera-still','--immediate','-o','./picture/pic.jpg'], capture_output=True, text=True, check=True)
	        print(result.stdout)
        except subprocess.CalledProcessError as e:
	        print(f"{e}")
	        print(f"{e.stderr}")
	
        image = Image.open('./picture/pic.jpg')
	
        max_size = (1944,1944)
        resized = image.resize(max_size)
        resized.save('./picture/pic.jpg')

	img = cv2.imread('./picture/pic.jpg')
	    
        size_crop = (224, 224)
        resized_img = cv2.resize(img, size_crop, interpolation=cv2.INTER_AREA)
        cv2.imwrite('./picture/pic.jpg', resized_img)

