def rotateList(l, n):
    if(n>0):
        return l[-n:] + l[:-n]
    else:
        return 1;


lst = []
n = int(input("Enter number of elements : "))
 
for i in range(0, n):
    ele = int(input())
    lst.append(ele)

x=int(input("How many times you want to rotate List? "))    
print("Before rotation: ",lst)
print("After rotation ",x," time: ",rotateList(lst,x))