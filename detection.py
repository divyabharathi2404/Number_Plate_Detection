import json
import urllib.request
import cv2
from google.colab.patches import cv2_imshow
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

file = []
for line in open('Indian_Number_plates.json', 'r'):
    file.append(json.loads(line))


for dat in file:
    data=dat[0]
    image_url=data['content']
    full_file_name = 'car' + '.jpg'
    urllib.request.urlretrieve(image_url,full_file_name)
    width=data['annotation'][0]['imageWidth']
    height=data['annotation'][0]['imageHeight']
    image = cv2.imread('car.jpg')
    cv2_imshow(image)
    img = Image.open('car.jpg').convert('LA')
    img.save('greyscale.png')
    img = mpimg.imread('car.jpg')     
    plt.imshow( gray,cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
    plt.show()
    
