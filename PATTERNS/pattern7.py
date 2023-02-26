n=int(input("enter the rows:"))
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(n-i):
        print("*",end=" ") 
    for j in range(n-i):
        print("*",end=" ")  
    print() 

#  OUTPUT
'''
  * * * * * * * * * * 
    * * * * * * * * 
      * * * * * * 
        * * * * 
          * * 
''' 
n=int(input("enter the rows:"))
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(n-i):
        print(n-i,end=" ") 
    for j in range(n-i):
        print(n-i,end=" ")  
    print() 
# OUTPUT
'''
  6 6 6 6 6 6 6 6 6 6 6 6 
    5 5 5 5 5 5 5 5 5 5 
      4 4 4 4 4 4 4 4 
        3 3 3 3 3 3 
          2 2 2 2 
            1 1 
'''      