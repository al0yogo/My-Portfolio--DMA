
##getting the dataset
# Load the Drive helper and mount
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from matplotlib.cbook import get_sample_data
import pytesseract
from pytesseract import pytesseract
import PIL
from PIL import Image
import cv2
import csv
import pandas as pd

img = input('file name: ')
#img = r'C:\\Users\\ennie\\Downloads\\everything\\images\\fivele.png'
imge = Image.open(img)
imge = imge.resize((1000,1000))
data = pytesseract.image_to_string(imge)
print(data)

#split the numbers into a list
datasplit = data.split()  


img2 = input('file name: ')
#img = r'C:\\Users\\ennie\\Downloads\\everything\\images\\fivele.png'
imge2 = Image.open(img2)
imge2 = imge2.resize((1000,1000))
data2 = pytesseract.image_to_string(imge2)
print(data2)

#split the numbers into a list
datasplit2 = data2.split()  

for i in datasplit:
    if i in datasplit2:
        print(i + ' is in both datasets')
        print('it\'s index is: ', datasplit.index(i))
