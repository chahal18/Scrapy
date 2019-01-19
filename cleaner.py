# -*- coding: utf-8 -*-
import pandas as pd
import warnings
warnings.filterwarnings("ignore")


data = pd.read_csv('final.csv')

print(data.head())

for i in range(len(data)):
  temp = data.weight[i]
  temp = ''.join(temp.split(' ')[0])
  data.weight[i] = temp

  data.height[i] = data.height[i].replace("½",".5")
  data.height[i] = data.height[i].replace("¾",".75")
  data.height[i] = data.height[i].replace("¼",".25")
  data.height[i] = data.height[i].replace("\xa0"," ")
  
  splits = data.height[i].split(' ')
  par = len(splits)
  
  if (par >= 4):
    feet = float(data.height[i][0])

    if (splits[2] != 'in' and splits[2] != 'or' ):
      inches = float(splits[2])
      print('splits2 runs')
    else:
      inches = 0
    data.height[i] = (feet*12 + inches)*2.54
  elif (par == 2):
    feet = float(data.height[i][0])
    data.height[i] = (feet*12)*2.54

  print('feet = %.2f \t in = %.2f \n ' % (feet,inches))  

print(data.head())

data.to_csv('Fin.csv', index = False)      