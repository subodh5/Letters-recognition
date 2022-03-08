from skimage.transform import resize
from skimage import color, io
from os import remove
import numpy as np

def imageprocess():
    img = io.imread('temp.png')
    remove("temp.png")
    image = color.rgb2gray(img)
    image_resized = resize(image, (28,28), anti_aliasing=True)
    finalimg=np.resize(image_resized, (28,28,1))
    return finalimg
    

def recognize(model):
    numarr = imageprocess()
    result=model.predict(np.array([numarr]))
    return np.argmax(result)

