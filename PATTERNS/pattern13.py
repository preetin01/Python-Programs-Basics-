n=int(input("enter the row:"))
for i in range(n):
    for j in range(n-i):
        print(n-i,end=" ")
    print()  
#output
'''
6 6 6 6 6 6 
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1 
'''

n=int(input("enter the row:"))
for i in range(n):
    for j in range(n-i):
        print(j+1,end=" ")
    print()              
#output
'''
1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 
'''    