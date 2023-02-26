n=int(input("enter the rows:"))
for i in range(n):
    for j in range(1,n-i):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ") 
    for j in range(i-1,-1,-1):
        print("*",end=" ")
    print()  
    
# OUTPUT 
'''
            * * 
          * * * * 
        * * * * * * 
      * * * * * * * * 
    * * * * * * * * * * 
  * * * * * * * * * * * * 
'''  
n=int(input("enter the rows:"))
for i in range(n):
    for j in range(1,n-i):
        print(" ",end=" ")
    for j in range(i+1):
        print(j+1,end=" ") 
    for j in range(i-1,-1,-1):
        print(j+1,end=" ")
    print()  
# OUTPUT
'''
            1 1 
          2 2 2 2 
        3 3 3 3 3 3 
      4 4 4 4 4 4 4 4 
    5 5 5 5 5 5 5 5 5 5 
  6 6 6 6 6 6 6 6 6 6 6 6 
'''                             