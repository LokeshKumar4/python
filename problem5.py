# -*- coding: utf-8 -*-
"""problem5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19DlOq_ygJvgx7bhM9l78PSC4v-8JGMQ7
"""



'''
Q. check the input string provided by the user , in case string provided is starting with the vowel we add on "ing" in the last otherwise we add on "esy" in the end of the string 

'''

n=input("enter a string :")
if n[0] in ('a','e','i','o','u','A','E','I','O','U'):
  n=n+"ing"
else:
  n=n+"esy"

print(n)