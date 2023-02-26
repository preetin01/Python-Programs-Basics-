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
'''  
n=int(input("enter the rows:"))
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ") 
    for j in range(n-i):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")              
    print()
# OUTPUT
'''
  * * * * * * * 
    * * * * * * * 
      * * * * * * * 
        * * * * * * * 
          * * * * * * * 
            * * * * * * * 
'''    