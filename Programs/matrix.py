print("----------------------")
print("MATRIX MULTIPLICATION")
print("----------------------")
A=[]
print("MATRIX-1")
n=int(input("enter N for N*N matrix::"))
print("enter the element:")
for i in range(n):
    row=[]
    for j in range(n):
        b=int(input())
        row.append(b)
    A.append(row)
print(A)
print(("MATRIX FORM"))
for i in range(n):
    for j in range(n):
        print(A[i][j],end=" ") 
    print()
print("--------------------") 
B=[]
print("MATRIX-2")
n=int(input("enter N for N*N matrix::"))
print("enter the element:")
for i in range(n):
    row=[]
    for j in range(n):
        b=int(input())
        row.append(b)
    B.append(row)
print(B)
print(("MATRIX FORM"))
for i in range(n):
    for j in range(n):
        print(B[i][j],end=" ") 
    print()
print("----------------------")
mul=[]
for i in range(n):
    row=[]
    for i in range(n):
        b=0
        row.append(b)
    mul.append(row)
for i in range(n):
    for j in range(n):
        for k in range(n):
            mul[i][j]+=A[i][k]*B[k][j]
print("THE RESULTANT MATRIX IS::>")
print(mul)
for i in range(n):
    for j in range(n):
        print(mul[i][j],end=" ")
    print()                        
    
               