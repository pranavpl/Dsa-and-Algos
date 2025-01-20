""" Print an Array 
def printarray(arr):
    for element in arr:
        print(element,end="")
    print()

arr = [1, 2, 3, 4, 5]
printarray(arr)"""

"""Find Maximum and Minimum
def findmaxmin(arr):
    maxval = max(arr)
    minval = min(arr)
    return maxval,minval

arr = [1,2,3,5]
maxval,minval = findmaxmin(arr)
print(maxval,minval)"""

""" Reverse an Array

def reversearr(arr):
    return arr[::-1]
arr = [1, 2, 3, 4, 5]
reversearr = reversearr(arr)
print("Reversed Array:",reversearr)"""


"""Check if Sorted
def sorted(arr):
    for i in range(len(arr)-1):
        if arr[i]>arr[i +1]:
         return False
    return True

arr = [8, 2, 3, 4, 5]
print("Is Sorted:", sorted(arr))"""


"""Sum of Array Elements

def sum(arr):
     for i in arr:
          arr = i+1
    
arr = [1, 2, 3, 4, 5]
total = sum(arr)
print("Sum of Elements:", total)"""

"""Find Duplicates (Brute Force)"""

def dinddep(arra):
     duplicate = []
     for i in range(len(arra)):
          for j in range(i+1,len(arra)):
             if arra[i] == arra[j] and arra[i] not in duplicate:
               duplicate.append(arra[i])
     return duplicate

arr = [4, 2, 4, 3, 2, 5, 6, 3]
duplicate = dinddep(arr)
print("Duplicates:", duplicate)