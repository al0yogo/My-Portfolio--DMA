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

    print('the length of the result list is:', len(Results))

def sevenletters(img, img2):
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
    list6 = []
    list7 = []


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
    for i in range(30, 36):
      list6.append(datasplit[i])
    for i in range(36, 42):
      list7.append(datasplit[i])
    #add first column and rows to dataframe
    df = pd.DataFrame({list1[0]:list1[1:5]}, index=[1,2,3,4])

    listoflists = [list1, list2, list3, list4, list5, list6, list7]
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
    list62 = []
    list72 = []


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
    for i in range(30, 36):
      list62.append(datasplit2[i])
    for i in range(36, 42):
      list72.append(datasplit2[i])
    #add first column and rows to dataframe
    df2 = pd.DataFrame({list12[0]:list12[1:5]}, index=[1,2,3,4])

    listoflists2 = [list12, list22, list32, list42, list52, list62, list72]
    print(listoflists2)
    check2 = []
    x2 = 1
    for i in listoflists2:
      name2 = i[0]
      if i[0] in check2:
        name2 = name2 + ' ' * x2
        df2[name2] = i[1:5]
        x2 = x2 + 1
      else:
        df2[i[0]] = i[1:5]
      check2.append(i[0])
    print(datasplit2)
    print(df2)


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

    checklist6 = list(df[list6[0]][0:4])

    checklist62 = list(df2[list62[0]][0:4])

    checklist7 = list(df[list6[0]][0:4])

    checklist72 = list(df2[list62[0]][0:4])

    check_lists(checklist1,checklist12)
    check_lists(checklist2,checklist22)
    check_lists(checklist3,checklist32)
    check_lists(checklist4,checklist42)
    check_lists(checklist5, checklist52)
    check_lists(checklist6, checklist62)
    check_lists(checklist7, checklist72)
    Finaltestafterlistchecks(Results)

def Sixletters(img, img2):
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
    list6 = []


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
    for i in range(30, 36):
      list6.append(datasplit[i])
    #add first column and rows to dataframe
    df = pd.DataFrame({list1[0]:list1[1:5]}, index=[1,2,3,4])

    listoflists = [list1, list2, list3, list4, list5, list6]
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
    list62 = []


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
    for i in range(30, 36):
      list62.append(datasplit2[i])
    #add first column and rows to dataframe
    df2 = pd.DataFrame({list12[0]:list12[1:5]}, index=[1,2,3,4])

    listoflists2 = [list12, list22, list32, list42, list52, list62]
    print(listoflists2)
    check2 = []
    x2 = 1
    for i in listoflists2:
      name2 = i[0]
      if i[0] in check2:
        name2 = name2 + ' ' * x2
        df2[name2] = i[1:5]
        x2 = x2 + 1
      else:
        df2[i[0]] = i[1:5]
      check2.append(i[0])
    print(datasplit2)
    print(df2)


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

    checklist6 = list(df[list6[0]][0:4])

    checklist62 = list(df2[list62[0]][0:4])


    check_lists(checklist1,checklist12)
    check_lists(checklist2,checklist22)
    check_lists(checklist3,checklist32)
    check_lists(checklist4,checklist42)
    check_lists(checklist5, checklist52)
    check_lists(checklist6, checklist62)
    Finaltestafterlistchecks(Results)

def fiveletters(img, img2):

  data = pytesseract.image_to_boxes(img)
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

  data2 = pytesseract.image_to_boxes(img2)

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
      name2 = name2 + ' ' * x2
      df2[name2] = i[1:5]
      x2 = x2 + 1
    else:
      df2[i[0]] = i[1:5]
    check2.append(i[0])
  print(datasplit2)
  print(df2)

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


  # assigning an image from the source path

def fourletters(img, img2):
  imge = Image.open(img)
  imge = imge.resize((1000,1000))
  data = pytesseract.image_to_boxes(imge)

  #split the numbers into a list
  datasplit = data.split()  
  print(datasplit)


  #ceate list for each letter
  list1 = []
  list3 = []
  list2 = []
  list4 = []


  #append numbers + letter to each list
  for i in range(6):
    list1.append(datasplit[i])
  for i in range(6, 12):
    list2.append(datasplit[i])
  for i in range(12, 18):
    list3.append(datasplit[i])
  for i in range(18, 24):
    list4.append(datasplit[i])

  #add first column and rows to dataframe
  df = pd.DataFrame({list1[0]:list1[1:5]}, index=[1,2,3,4])

  listoflists = [list1, list2, list3, list4]
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

  #load image and convert to number points
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


  #append numbers + letter to each list
  for i in range(6):
    list12.append(datasplit2[i])
  for i in range(6, 12):
    list22.append(datasplit2[i])
  for i in range(12, 18):
    list32.append(datasplit2[i])
  for i in range(18, 24):
    list42.append(datasplit2[i])

  #add first column and rows to dataframe
  df2 = pd.DataFrame({list12[0]:list12[1:5]}, index=[1,2,3,4])

  listoflists2 = [list12, list22, list32, list42]
  print(listoflists2)
  check2 = []
  x2 = 1
  for i in listoflists2:
    name2 = i[0]
    if i[0] in check2:
      name2 = name2 + ' ' * x2
      df2[name2] = i[1:5]
      x2 = x2 + 1
    else:
      df2[i[0]] = i[1:5]
    check2.append(i[0])
  print(datasplit2)
  print(df2)

    
  checklist1 = list(df[list1[0]][0:4])

  #list1[0] = 'letter index/column name'

  checklist12 = list(df2[list12[0]][0:4])


  checklist2 = list(df[list2[0]][0:4])

  checklist22 = list(df2[list22[0]][0:4])

  checklist3 = list(df[list3[0]][0:4])

  checklist32 = list(df2[list32[0]][0:4])

  checklist4 = list(df[list4[0]][0:4])

  checklist42 = list(df2[list42[0]][0:4])



  Results = []

  check_lists(checklist1,checklist12)
  check_lists(checklist2,checklist22)
  check_lists(checklist3,checklist32)
  check_lists(checklist4,checklist42)

  Finaltestafterlistchecks(Results)

def threeletters(img, img2):
  imge = Image.open(img)
  imge = imge.resize((1000,1000))
  data = pytesseract.image_to_boxes(imge)

  #split the numbers into a list
  datasplit = data.split()  
  print(datasplit)


  #ceate list for each letter
  list1 = []
  list3 = []
  list2 = []


  #append numbers + letter to each list
  for i in range(6):
    list1.append(datasplit[i])
  for i in range(6, 12):
    list2.append(datasplit[i])
  for i in range(12, 18):
    list3.append(datasplit[i])

  #add first column and rows to dataframe
  df = pd.DataFrame({list1[0]:list1[1:5]}, index=[1,2,3,4])

  listoflists = [list1, list2, list3]
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

  #load image and convert to number points
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


  #append numbers + letter to each list
  for i in range(6):
    list12.append(datasplit2[i])
  for i in range(6, 12):
    list22.append(datasplit2[i])
  for i in range(12, 18):
    list32.append(datasplit2[i])

  #add first column and rows to dataframe
  df2 = pd.DataFrame({list12[0]:list12[1:5]}, index=[1,2,3,4])

  listoflists2 = [list12, list22, list32]
  print(listoflists2)
  check2 = []
  x2 = 1
  for i in listoflists2:
    name2 = i[0]
    if i[0] in check2:
      name2 = name2 + ' ' * x2
      df2[name2] = i[1:5]
      x2 = x2 + 1
    else:
      df2[i[0]] = i[1:5]
    check2.append(i[0])
  print(datasplit2)
  print(df2)

    
  checklist1 = list(df[list1[0]][0:4])

  #list1[0] = 'letter index/column name'

  checklist12 = list(df2[list12[0]][0:4])


  checklist2 = list(df[list2[0]][0:4])

  checklist22 = list(df2[list22[0]][0:4])

  checklist3 = list(df[list3[0]][0:4])

  checklist32 = list(df2[list32[0]][0:4])




  Results = []

  check_lists(checklist1,checklist12)
  check_lists(checklist2,checklist22)
  check_lists(checklist3,checklist32)

  Finaltestafterlistchecks(Results)

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

def findcommonwords():    
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
    input('enter to proceed: ')




    
Results = []
def main():
  findcommonwords()

  img = input('image of singular common word: ')
  img2 = input('image of singular common word on the second piece of writing: ')
  # converts the image to result and saves it into result variable
  string = pytesseract.image_to_string(img)
  string2 = pytesseract.image_to_string(img2)
  print(string)

  Results = []
  #maybe i could do a for loop and run through it, similar words ill call the following
  #functions on... or stick their image to boxes in a seperate dataset, but the point is you don't need to divide the image only the data
  WL = len(string) - 1
  print(WL)
  WLT = len(string2) - 1
  if WL == 5 and WL == WLT:
    fiveletters(img, img2)
  if WL == 6 and WL == WLT:
    Sixletters(img, img2)
  if WL == 4 and WL == WLT:
    fourletters(img, img2)
  if WL == 3 and WL == WLT:
    threeletters(img, img2)
  if WL == 7 and WL == WLT:
    sevenletters(img, img2)



main()