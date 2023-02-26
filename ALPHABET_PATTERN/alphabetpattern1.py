# loop through alphabets and print them

# 65 in char is A
# 90 in char is Z
for i in range(65, 91):
    print(chr(i), end=" ")
print()    

#OUTPUT
'''
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
'''  
# Square pattern   
n=int(input("enter the row:"))
count=0
for i in range(n):
    for j in range(n):
        print(chr(65+count),end=" ")
        count=count+1                # changing charater
    print()  
#OUTPUT
'''
A B C D E 
F G H I J 
K L M N O 
P Q R S T 
U V W X Y 
'''    

n=int(input("enter the row:"))
count=0
for i in range(n):
    for j in range(n):
        print(chr(65+j),end=" ")
        count=count+1                # changing charater
    print()  
#OUTPUT
'''
A B C D E 
A B C D E 
A B C D E 
A B C D E 
A B C D E 

'''   
n=int(input("enter the row:"))
count=0
for i in range(n):
    for j in range(n):
        print(chr(65+i),end=" ")
        count=count+1                # changing charater
    print()  
#OUTPUT
'''
A A A A A 
B B B B B 
C C C C C 
D D D D D 
E E E E E 
''' 