# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 16:50:13 2022

@author: Elkin Gutierrez
"""

def solution(n):
    #here we divide by 2 until there are not 0s at the right oif the binary representation of n
    while n%2==0:
        n=n//2
    result=0
    #for each strike we will count how many 0s we have
    count=0
    while n>1:
        if n%2==1:
            n=n//2
            count=0
        else:
            n=n//2
            count+=1
        #we want te max count strike of 0s 
        result=max(result,count)
    
    return(result)
    pass
