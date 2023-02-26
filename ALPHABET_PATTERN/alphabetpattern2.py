n=int(input("enter the rows:"))
count=0
for i in range(n):
    for j in range(n-i):
        print(chr(65+count),end=" ")
        count=count+1
    print()    
#ouput
'''
A B C D E 
F G H I 
J K L 
M N 
O 
'''

n=int(input("enter the rows:"))
count=0
for i in range(n):
    for j in range(i+1):
        print(chr(65+count),end=" ")
        count=count+1
    print()  
#output
'''
A 
B C 
D E F 
G H I J 
K L M N O 
'''     
n=int(input("enter the rows:"))
for i in range(n):
    for j in range(i+1):
        print(chr(65+j),end=" ")
    print()    
#output
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
        print(chr(65+j),end=" ")
    print()
#output
'''
A B C D E 
A B C D 
A B C 
A B 
A 
'''  