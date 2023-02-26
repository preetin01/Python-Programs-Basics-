

n=int(input("enter the row:"))
k=n-1
for i in range(n):
    for j in range(k):
        print(end=" ")
    k=k-1
    for j in range(i+1):
        print("*",end=" ") 
    print("\r")   
# OUTPUT
'''
     * 
    * * 
   * * * 
  * * * * 
 * * * * * 
* * * * * * 
'''  
n=int(input("enter the row:"))
k=n-1
for i in range(n):
    for j in range(k):
        print(end=" ")
    k=k-1
    for j in range(i+1):
        print(i+1,end=" ") 
    print("\r")  
# OUTPUT
'''
     1 
    2 2 
   3 3 3 
  4 4 4 4 
 5 5 5 5 5 
6 6 6 6 6 6 
'''     