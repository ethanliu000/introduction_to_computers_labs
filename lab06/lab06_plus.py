# -*- coding: utf-8 -*-
"""lab06_plus.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15KC1meiYrm_E3X2ep2pZYonVJ4_cwCme
"""

import random as r
Times = {"One":0, "Two":0, "Three":0, "Four":0, "Five":0, "Six":0}
list1 = list(Times.keys())
list2 = list(Times.values())
list_prob = []

for i in range(1000000):
  a = r.randint(1, 6)
  for j in range(1,7):
    if a == j:
      list2[j-1]=list2[j-1]+1

for i in range(6):
  b = (list2[i]/1000000)*100
  list_prob.append(round(b, 2))
for i in range(6):  
  print("The Probability of",list1[i],"is",list_prob[i],"%")