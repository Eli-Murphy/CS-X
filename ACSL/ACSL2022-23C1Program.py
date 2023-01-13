#!/bin/python3

import math
from math import log
import os
import random
import re
import sys
from collections import Counter


#
# Complete the 'findModeCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER num
#  2. INTEGER base
#  3. STRING start
#


def val(c): 
    if c >= '0' and c <= '9': 
        return ord(c) - ord('0') 
    else: 
        return ord(c) - ord('A') + 10; 

def toDeci(str,base): 
    llen = len(str) 
    power = 1 
    num = 0     

    for i in range(llen - 1, -1, -1): 
          
        if val(str[i]) >= base: 
            print('Invalid Number') 
            return -1
        num += val(str[i]) * power 
        power = power * base 
    return num 
      



def my_range(start,end,base,step=1):

    def Convert(n,base):
       string = "0123456789ABCDEF"
       if n < base:
          return string[n]
       else:
          return Convert(n//base,base) + string[n%base]
    return (Convert(i,base) for i in range(start,end,step))


def findModeCount(num, base, start):

    if base > 10:
        start10 = toDeci(start, base)
    else:
        start10 = int(start, base)

    print(start)
    print(start10)
    
    mainlist = list(my_range(start10, start10+num, base))
    out = list(''.join(mainlist))
    counter = Counter(out)
    most_common_2 = counter.most_common()
    print(most_common_2[0][1])
    return most_common_2[0][1]  


if __name__ == '__main__':


    num = 20
    base = 12
    start = "9AB"

    #num = int(input().strip())

    #base = int(input().strip())

    #start = input()

    result = findModeCount(num, base, start)

