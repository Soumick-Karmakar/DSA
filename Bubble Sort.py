# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 11:02:43 2020

@author: Admin
"""

lst=list(map(int,input().split()))
for i in range((len(lst))-1):
    for j in range((len(lst))-1):
        if lst[j]>lst[j+1]:
            n=lst[j]
            lst[j]=lst[j+1]
            lst[j+1]=n
for i in range(len(lst)):
    print(lst[i])