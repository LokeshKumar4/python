# -*- coding: utf-8 -*-
"""problem7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xd3Df2VQGYJuFmgSuB0kBY7USUj2L65q
"""



'''
in the string find out how many vowels are present with it unique count
futurense
u=2 , e =2

'''
n=input("Enter a string :")
dic={}
for char in n :
  if char in 'aeiou':
    dic[char]= n.count(char)
print(dic)