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
            1 
          1 2 1 
        1 2 3 2 1 
      1 2 3 4 3 2 1 
    1 2 3 4 5 4 3 2 1 
  1 2 3 4 5 6 5 4 3 2 1 
1 2 3 4 5 6 7 6 5 4 3 2 1 
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
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(n-i-1):
        print(j+1,end=" ")
    for j in range(n-i-3,-1,-1):   
        print(j+1,end=" ")
    print() 
   
# OUTPUT
'''
            1 
          1 2 1 
        1 2 3 2 1 
      1 2 3 4 3 2 1 
    1 2 3 4 5 4 3 2 1 
  1 2 3 4 5 6 5 4 3 2 1 
1 2 3 4 5 6 7 6 5 4 3 2 1 
  1 2 3 4 5 6 5 4 3 2 1 
    1 2 3 4 5 4 3 2 1 
      1 2 3 4 3 2 1 
        1 2 3 2 1 
          1 2 1
            1 
'''   
n=int(input("enter the rows:"))
for i in range(n):
    for j in range(1,n-i):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    for j in range(i-1,-1,-1):
        print("*",end=" ")    
    print()    
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(n-i-1):
        print("*",end=" ")
    for j in range(n-i-3,-1,-1):
        print("*",end=" ")
    print() 
    
# OUTPUT
'''
                  * 
                * * *
              * * * * *
            * * * * * * *
          * * * * * * * * *
        * * * * * * * * * * *
      * * * * * * * * * * * * * 
    * * * * * * * * * * * * * * *
  * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * *
  * * * * * * * * * * * * * * * * *
    * * * * * * * * * * * * * * *
      * * * * * * * * * * * * *
        * * * * * * * * * * * 
          * * * * * * * * *
            * * * * * * *
              * * * * *
                * * *
                  *

'''                                