n=int(input("enter the rows:"))
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()
# OUTPUT
'''
*
* *
* * *
* * * *
* * * * *
* * * * * *
* * * * * * *
'''    
n=int(input("enter the rows:"))
for i in range(n):
    for j in range(i+1):
        print(j+1,end=" ")
    print()
# OUTPUT
'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6
1 2 3 4 5 6 7
'''  
n=int(input("enter the row:"))
for i in range(n):
    for j in range(i,-1,-1):
        print(j+1,end=" ")
    print()    
# OUTPUT
'''
1 
2 1 
3 2 1 
4 3 2 1 
5 4 3 2 1 
6 5 4 3 2 1 
'''    