import subprocess
from PIL import Image
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

        size_crop = (224,224)
        img = Image.open('./picture/pic.jpg')
        img.thumbnail(size_crop)
        img.save('./picture/pic.jpg')

