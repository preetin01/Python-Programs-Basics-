# SUARE PATTERN
n=int(input("enter the number:"))
for i in range(n):
    for j in range(n):
        print("*",end=' ')   # print the "*" in the same line 
    print()                  # print the "*" in the new line      
#output
'''
* * * *
* * * *
* * * *
* * * *
''' 
m=int(input("enter the row:"))
for i in range(n):
    for j in range(n):
        print(n-i,end=" ")
    print()    
# OUTPUT
'''
5 5 5 5 5 
4 4 4 4 4 
3 3 3 3 3 
2 2 2 2 2 
1 1 1 1 1 
''' 
m=int(input("enter the row:"))
for i in range(n):
    for j in range(n):
        print(i+1,end=" ")
    print() 
    
# OUTPUT  
'''
1 1 1 1 
2 2 2 2 
3 3 3 3 
4 4 4 4 
'''      