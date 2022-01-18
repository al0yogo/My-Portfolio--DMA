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
data = pytesseract.image_to_boxes(imge)
print(data)

#split the numbers into a list
datasplit = data.split()  
print(datasplit)


#ceate list for each letter
list1 = []
list3 = []
list2 = []
list4 = []
list5 = []


#append numbers + letter to each list
for i in range(6):
  list1.append(datasplit[i])
for i in range(6, 12):
  list2.append(datasplit[i])
for i in range(12, 18):
  list3.append(datasplit[i])
for i in range(18, 24):
  list4.append(datasplit[i])
for i in range(24, 30):
  list5.append(datasplit[i])
#add first column and rows to dataframe
df = pd.DataFrame({list1[0]:list1[1:5]}, index=[1,2,3,4])

listoflists = [list1, list2, list3, list4, list5]
print(listoflists)
check = []
x = 1
for i in listoflists:
  name = i[0]
  if i[0] in check:
    name = name + ' ' * x
    df[name] = i[1:5]
    x = x+1
  else:
    df[i[0]] = i[1:5]
  check.append(i[0])
print(datasplit)
print(df)

img2 = input('second file name: ')
imge2 = Image.open(img2)
imge2 = imge2.resize((1000,1000))
data2 = pytesseract.image_to_boxes(imge2)

#split the numbers into a list
datasplit2 = data2.split()  
print(datasplit2)


#ceate list for each letter
list12 = []
list32 = []
list22 = []
list42 = []
list52 = []


#append numbers + letter to each list
for i in range(6):
  list12.append(datasplit2[i])
for i in range(6, 12):
  list22.append(datasplit2[i])
for i in range(12, 18):
  list32.append(datasplit2[i])
for i in range(18, 24):
  list42.append(datasplit2[i])
for i in range(24, 30):
  list52.append(datasplit2[i])
#add first column and rows to dataframe
df2 = pd.DataFrame({list12[0]:list12[1:5]}, index=[1,2,3,4])

listoflists2 = [list12, list22, list32, list42, list52]
print(listoflists2)
check2 = []
x2 = 1
for i in listoflists2:
  name2 = i[0]
  if i[0] in check2:
    name2 = name2 + ' ' * x
    df2[name2] = i[1:5]
    x2 = x2 + 1
  else:
    df2[i[0]] = i[1:5]
  check2.append(i[0])
print(datasplit2)
print(df2)

#checks to see if the data sets are the same for x points
def check_lists(firstlist, secondlist):
  buffer = 60
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
      print('The first false index is', i+1)
      break
  if Final >= len(resultlist)/2:
    print('it is the same person.')

  print('the length of the result list is:', len(resultlist))

  #variables

checklist1 = list(df[list1[0]][0:4])
print(checklist1)
#list1[0] = 'letter index/column name'

checklist12 = list(df2[list12[0]][0:4])
print(checklist12)

checklist2 = list(df[list2[0]][0:4])

checklist22 = list(df2[list22[0]][0:4])

checklist3 = list(df[list3[0]][0:4])

checklist32 = list(df2[list32[0]][0:4])

checklist4 = list(df[list4[0]][0:4])

checklist42 = list(df2[list42[0]][0:4])

checklist5 = list(df[list5[0]][0:4])

checklist52 = list(df2[list52[0]][0:4])


Results = []

check_lists(checklist1,checklist12)
check_lists(checklist2,checklist22)
check_lists(checklist3,checklist32)
check_lists(checklist4,checklist42)
check_lists(checklist5, checklist52)
Finaltestafterlistchecks(Results)

input('enter to exit: ')