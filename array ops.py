""" Print an Array 
def printarray(arr):
    for element in arr:
        print(element,end="")
    print()

arr = [1, 2, 3, 4, 5]
printarray(arr)"""

"""Find Maximum and Minimum"""
def findmaxmin(arr):
    maxval = max(arr)
    minval = min(arr)
    return maxval,minval

arr = [1,2,3,5]
maxval,minval = findmaxmin(arr)
print(maxval,minval)

