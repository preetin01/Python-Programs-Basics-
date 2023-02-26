'''
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
    

n=int(input("enter the rows:"))
for i in range(n):
    for j in range(n-i):
        print("---",end="")
    for j in range(i+1):
        print(".|.",end="")
    for j in range(i):
        print(".|.",end="")
    for j in range(n-i):
        print("---",end="")        
    print() 
for i in range(n-n+1):
    for j in range(n-i-1):
        print("---",end="")
    print("-WELCOME-",end="")
    for j in range(n-i-1):
        print("---",end="")
    print()    
for i in range(n):
    for j in range(i+1):
        print("---",end="")
    for j in range(n-i):
        print(".|.",end="")
    for j in range(n-i-1):
        print(".|.",end="")
    for j in range(i+1):
        print("---",end="")    
    print()            
#OUTPUT  '''          
 
n,m=map(int, input().split())
x='.|.'
y='WELCOME'
for i in range(n//2):
    print(x*((i*2)+1)).center(m,'-')
    
print(y.center(m,'-'))

for i in range(n//2-1,-1,-1):
    print(x*((i*2)+1)).center(m,'-')    