import numpy as np
def displaySortedArray(a):
    print("After Sorting Elements Are:")
    for i in range(len(a)):
        print(a[i]," ",end="")
    
def bubbleSort(a):
    for i in range(len(a)):
        for j in range((len(a)-i-1)):
            if(a[j]>a[j+1]):
                a[j]=a[j]+a[j+1]
                a[j+1]=a[j]-a[j+1]
                a[j]=a[j]-a[j+1]
    print("Applying Bubble Sort!!")
    displaySortedArray(a)
    

    
def insertionSort(a):
    temp=0
    j=0
    for i in range(1,len(a)):
        temp=a[i]
        j=i-1
        while((temp<a[j]) and (j>=0)):
            a[j+1]=a[j]
            j=j-1
        a[j+1]=temp
    print("Applying Insertion Sort!!")
    displaySortedArray(a)
    
def smallest(a,k):
    pos=k
    small=a[k]
    for i in range((k+1),len(a)):
        if(a[i]<small):
            small=a[i]
            pos=i
    return pos

def selectionSort(a):
    temp=0
    pos=0
    for k in range(len(a)):
        pos=smallest(a,k)
        temp=a[k]
        a[k]=a[pos]
        a[pos]=temp
    print("Applying Selection Sort!!")
    displaySortedArray(a)

print("Press a for Bubble Sort")
print("Press b for Insertion Sort")
print("Press c for Selection Sort")
print("Press d for Exit")
c=input("Enter your choise:")

if(c=='a'):
    n=int(input("enter size:"))
    a=np.empty(n, dtype=int)

    for i in range(n):
        a[i]=int(input())
    bubbleSort(a)
elif(c=='b'):
    n=int(input("enter size:"))
    a=np.empty(n, dtype=int)

    for i in range(n):
        a[i]=int(input())
    
    insertionSort(a)
elif(c=='c'):
    n=int(input("enter size:"))
    a=np.empty(n, dtype=int)

    for i in range(n):
        a[i]=int(input())
    
    selectionSort(a)
    
elif(c=='d'):
    print("you are exit!!")
    pass
else:
    print("Wrong choise!!")