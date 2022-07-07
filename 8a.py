

lst = []
n = int(input("Enter how many numbers you want to enter in list : "))
for i in range(0, n):
    ele = int(input())
    lst.append(ele)
     
print("Original list: ",lst)
dic={}
for i in lst:
    dic[i]=lst.count(i)
print("Printing count of each item: ",dic)

