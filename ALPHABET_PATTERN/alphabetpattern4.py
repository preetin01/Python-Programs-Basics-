n=int(input("enter the rows:"))
for i in range(n):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(i+1):
        print(chr(65+i),end=" ")
    print()  
'''
          A 
        B B 
      C C C 
    D D D D 
  E E E E E 
'''   
n=int(input("enter the rows:"))
for i in range(n):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(i+1):
        print(chr(65+j),end=" ")
    print()  
'''
          A 
        A B 
      A B C 
    A B C D 
  A B C D E 
'''        
n=int(input("enter the rows:"))
for i in range(n):
  for j in range(n-i):
    print(" ",end=" ")
  for j in range(i+1):
      print(chr(65+j),end=" ")
  for j in range(i-1,-1,-1) :   
    print(chr(65+j),end=" ")
  print() 
for i in range(n):
  for j in range(i+2):
    print(" ",end=" ")
  for j in range(n-i-1):
    print(chr(65+j),end=" ")
  for j in range(n-i-3,-1,-1): 
    print(chr(65+j),end=" ")   
  print()  
        
#OUTPUT
'''
            A 
          A B A 
        A B C B A 
      A B C D C B A 
    A B C D E D C B A 
  A B C D E F E D C B A 
    A B C D E D C B A 
      A B C D C B A 
        A B C B A 
          A B A 
            A
'''               