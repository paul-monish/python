import numpy as np

def bubbleSort(a):
    for i in range(len(a)):
        for j in range((len(a)-i-1)):
            if(a[j]>a[j+1]):
                a[j]=a[j]+a[j+1]
                a[j+1]=a[j]-a[j+1]
                a[j]=a[j]-a[j+1]
    return a;

def linearSearch(a, x):
 
    for i in range(len(a)):
        if (a[i] == x):
            return i
    return -1
 
def binarySearch (arr, l, r, x):
 
    if(r >= l):
 
        mid = l+(r - l)// 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
        else:
            return binarySearch(arr, mid + 1, r, x)
 
    else:
       
        return -1
 
print("Press a for Linear Search")
print("Press b for Binary Search")
print("Press c for Exit")
c=input("Enter your choise:")
if(c=='a'):
    
    print("Linear Search!!")
    n=int(input("enter size:"))
    
    a=np.empty(n, dtype=int)
    
    for i in range(n):
        a[i]=int(input())
    
    x=int(input("Enter Which element you want to fine?"))
    
    result = linearSearch(a,x)
    if(result == -1):
        print("Element is not present in array")
    else:
        print("Element is present at index", result)
elif(c=='b'):
    
    print("Binary Search!!")
    n=int(input("enter size:"))
    
    a=np.empty(n, dtype=int)
    
    for i in range(n):
        a[i]=int(input())
    
    x=int(input("Enter Which element you want to fine?"))
    
    arr=bubbleSort(a)
    result = binarySearch(arr, 0, len(arr)-1, x)
    if(result == -1):
        print("Element is not present in array")
    else:
        print("Element is present at index", result)
elif(c=='c'):
    print("you are exit!!")
    pass
else:
    print("Wrong choise!!")

