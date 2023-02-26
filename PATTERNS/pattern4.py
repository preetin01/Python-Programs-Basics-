# RIGHT SIDED TRIANGLE PATTERN

n=int(input("enter the rows:"))
for i in range(n):
    for j in range(n-i):
        print(" ",end=" ")
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
'''
n=int(input("enter the row:"))
for i in range(n):
    for j in range(n-i):
      print(" ",end=" ")
    for j in range(i+1):
      print(i+1,end=" ")
    print()   
# OUTPUT
'''
          1 
        2 2 
      3 3 3 
    4 4 4 4 
  5 5 5 5 5 
'''  
n=int(input("enter the row:"))
for i in range(n):
    for j in range(n-i):
      print(" ",end=" ")
    for j in range(i+1):
      print(n-i,end=" ")
    print() 
# OUTPUT
'''
          5 
        4 4 
      3 3 3 
    2 2 2 2 
  1 1 1 1 1 
'''       