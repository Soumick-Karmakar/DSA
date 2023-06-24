# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 20:30:12 2020

@author: Admin
"""

lst=list(map(int,input().split()))
for i in range(1,len(lst)):
    a=i
    for j in range((i-1),-1,-1):
         if lst[a]<=lst[j]:
            m=lst[a]
            lst[a]=lst[j]
            lst[j]=m
            a=a-1
         else:
            j=-1
            
for i in range(len(lst)):
    print(lst[i],end=' ')