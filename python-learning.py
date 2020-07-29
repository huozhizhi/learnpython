#!/usr/bin/env python3
def cal(*number):
    sum =0
    for n in number:
        sum =sum + n*n
    return sum
print (cal())

def fact(n):
    if n==1:
        return n
    return n*fact(n-1)
