def make_zeros(a, b):
    matrix = []
    for i in range(a):
        matrix.append([0] * b)
    return matrix

def matmul(a,b):
    result=make_zeros(len(a),len(b))
    #print(result)
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
    print(result)

print("Matrix 1")
r = int(input("Enter the number of rows:"))
c = int(input("Enter the number of columns:"))
  

matrix1 = []
print("Enter the entries rowwise for matrix 1:")
  

for i in range(r):         
    a =[]
    for j in range(c):     
         a.append(int(input()))
    matrix1.append(a)
  

for i in range(r):
    for j in range(c):
        print(matrix1[i][j], end = " ")
    print()
    
print("Matrix 2")
  

matrix2 = []
print("Enter the entries rowwise for matrix2:")
  

for i in range(r):         
    b =[]
    for j in range(c):     
         b.append(int(input()))
    matrix2.append(b)
  

for i in range(r):
    for j in range(c):
        print(matrix2[i][j], end = " ")
    print()
  
matmul(matrix1,matrix2)