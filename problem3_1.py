# -*- coding: utf-8 -*-
"""problem3_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DUVVduZ87lBWW4PS9brop0iKx_dHFA0W
"""

'''
Q. to take a list value and create its cube if it is a integer number and make the changes for the original index 
'''

def cubeCalc(listData):
  for i in range(len(listData)):
    if type(listData[i]) is int:
      listData[i]=listData[i]**3

mylist=[1,2,3,4,5,6]
print("actual list: ",mylist)
cubeCalc(mylist)
print("cube of list: ",mylist)