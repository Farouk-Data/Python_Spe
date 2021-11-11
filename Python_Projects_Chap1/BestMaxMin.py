#!/usr/bin/python

def findMax(arr):
    Max = None
    for i in arr:
        #if Max == None
        if Max is None or Max < i : 
            Max = i
    return Max

def findMin(arr):
    Min = None
    for i in arr:
        #if Min == None
        if Min is None or Min > i:
            Min = i
    return Min

arr = [1,5,3,6,-3]
print 'Max of arr is ',findMax(arr)
print 'Min of arr is ',findMin(arr)

