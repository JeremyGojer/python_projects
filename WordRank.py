# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 23:35:50 2022

@author: jerem
"""

from collections import Counter

ip = input()

strg = list(ip)
strg.sort()
ip = list(ip)
          
#print(strg,ip)
# this turns the string into list of all combinations possible except duplicates    
n = len(strg)
def pluck(x):
    a = []
    l = len(x)
    for i in range(l):
        a.append([x[i],x[:i]+x[i+1:l]])
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    return b  
#print(pluck(strg))

#finds duplicates in format [len(x),repetition 1,...]
def dupl(x):
    a = [len(x)]
    b = Counter(x)
    for i in b:
        if b[i] > 1:
            a.append(b[i])
    return a

#factorial function of x
def fact(x):
    prod = 1
    for i in range(1,x+1):
        prod *= i
    return prod

#product of all elements in list x
def prodl(x):
    prod = 1
    if len(x) < 1:
        return 1
    else:
        for i in x:
            prod *= i
        return prod

# x : original string, y : pluck method of sorted string
def comb(x,y,sum=1):
    y = pluck(y)
    i = 0
    for i in y:
        if i[0] != x[0]:
            a = list(map(fact, dupl(i[1])))
            sum += a[0]//prodl(a[1:])
        else:
            y = i[1]
            x = x[1:]
            return comb(x,y,sum)
    return sum
        
print(comb(ip,strg,sum=1))