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
import getopt
import sys
from PIL import Image
#drive.mount('/content/drive')

#img = input('image file:')
#img = r'/content/drive/My Drive/the4.png'
img = input('firstfile: ')
#img = r'C:\\Users\\ennie\\Downloads\\everything\\code\\the4.png'


# r'C:\\Users\\ennie\\Downloads\\everything\\code\\the4.png'
#r'/content/drive/My Drive/the4.png'
imge = Image.open(img)
imge = imge.resize((400, 400))
data = pytesseract.image_to_boxes(imge)

#print(data)

datasplit = data.split()  
print(datasplit)

# import pandas library as pd
import pandas as pd
  
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# create an Empty DataFrame object
df = pd.DataFrame()
  
print(df.head(3))
i = 0
# append columns to an empty DataFrame
while i > len(datasplit):
  if datasplit[i] in alphabet:
    df[datasplit[i]] = [datasplit[i+1], datasplit[i+2], datasplit[i+3], datasplit[i+4], datasplit[i+5]]
  i = i + 1

print(df.head(3))

list1 = []
list3 = []
list2 = []
list4 = []
list5 = []
list6 = []


for i in range(6):
  list1.append(datasplit[i])
for i in range(6, 12):
  list2.append(datasplit[i])
for i in range(12, 18):
  list3.append(datasplit[i])

"""
for i in range(18, 24):
  list4.append(datasplit[i])
for i in range(24, 30):
  list5.append(datasplit[i])
for i in range(30, 36):
  list6.append(datasplit[i])
"""
#create new df 
df = pd.DataFrame({list1[0]:list1[1:5]}, index=[1,2,3,4])
print (df.head(3))

df[list2[0]] = list2[1:5]
df[list3[0]] = list3[1:5]

"""
df[list4[0]] = list4[1:5]
df[list5[0]] = list5[1:5]
df[list6[0]] = list6[1:5]
"""
print(df.head(3))

#img2 = r'/content/drive/My Drive/the1.jpeg'
img2 = input('second file: ')
#r'C:\\Users\\ennie\\Downloads\\everything\\code\\the1.jpeg'
#img2 = r'C:\\Users\\ennie\\Downloads\\everything\\code\\the1.jpeg'
imge2 = Image.open(img2)
imge2 = imge2.resize((400, 400))
data2 = pytesseract.image_to_boxes(imge2)

#print(data)

datasplit2 = data2.split() 


df2 = pd.DataFrame()
  
i = 0
# append columns to an empty DataFrame
while i > len(datasplit2):
  if datasplit2[i] in alphabet:
    df2[datasplit2[i]] = [datasplit2[i+1], datasplit2[i+2], datasplit2[i+3], datasplit2[i+4], datasplit2[i+5]]
  i = i + 1


list10 = []
list30 = []
list20 = []
list40 = []
list50 = []
list60 = []


for i in range(6):
  list10.append(datasplit2[i])
for i in range(6, 12):
  list20.append(datasplit2[i])
for i in range(12, 18):
  list30.append(datasplit2[i])

"""
for i in range(18, 24):
  list40.append(datasplit[i])
for i in range(24, 30):
  list50.append(datasplit[i])
for i in range(30, 36):
  list60.append(datasplit[i])
"""

#create new df 
df2 = pd.DataFrame({list10[0]:list10[1:5]}, index=[1,2,3,4])

df2[list20[0]] = list20[1:5]
df2[list30[0]] = list30[1:5]

"""
df2[list40[0]] = list40[1:5]
df2[list50[0]] = list50[1:5]
df2[list60[0]] = list60[1:5]
"""
print(df2)

import matplotlib.pyplot as plt


#checks to see if the data sets are the same for x points
def check_lists(firstlist, secondlist):
  buffer = 40
  a = firstlist
  b = secondlist
  for i in range(len(firstlist)):
    if int(a[i]) >= int(b[i]) - buffer and int(a[i]) <= int(b[i]) + buffer or int(b[i]) >= int(a[i]) - buffer and int(b[i]) <= int(a[i]) + buffer:
      print('true')
      Results.append('True')
    else:
      print('false')
      Results.append('False')
  print(Results)


  #test final again
def Finaltestafterlistchecks(resultlist):
  Final = 0

  for i in range(len(resultlist)):
    if resultlist[i] == 'True':
      Final += 1
    else:
      print('false')
      print('The false index is', i+1)
  if Final >= len(resultlist)/5:
    print('it is the same person.')

  print('the length of the result list is:', len(resultlist))


  #variables
TListX = list(df[list10[0]][0:4])

TListX2 = list(df2[list1[0]][0:4])

HListX = list(df[list2[0]][0:4])

HListX2 = list(df2[list20[0]][0:4])

EListX = list(df[list3[0]][0:4])

EListX2 = list(df2[list30[0]][0:4])


Results = []


check_lists(TListX,TListX2)

check_lists(HListX, HListX2)

check_lists(EListX, EListX2)

Finaltestafterlistchecks(Results)

input("Press enter to exit ;)")