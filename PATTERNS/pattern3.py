# DECREASING TRIANGLE PATTERN

n=int(input("enter the rows:"))
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()    

# OUTPUT
'''
* * * * 
* * * 
* * 
*
'''
n=int(input("enter the row:"))
for i in range(n):
    for j in range(n-i):
        print(n-i,end=" ")
    print()    
#OUTPUT
'''
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1 
'''    
n=int(input("enter the row:"))
for i in range(n):
    for j in range(n-i):
        print(i+1,end=" ")
    print()    
#OUTPUT 
'''
1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5 
'''   