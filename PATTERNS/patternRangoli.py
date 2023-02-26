'''
----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----
'''
n=int(input("enter the rows"))
for i in range(n):
    for j in range(n-i-1):
        print("--",end="")
    for j in range(i+1):
         print(chr(99+j),end=' ')    
    for j in range(i):
        print(ch,end=' ')         
    for j in range(n-i-1):
        print('--',end='')
    print()
for i in range(n):
    for j in range(i):
        print('--',end='')
    for j in range(n-i-1):
        print('#',end=' ')
    for j in range(n-i-1):
        print('#',end=' ')
    #for j in range():            
    print()    