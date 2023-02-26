n=int(input('enter the rows:'))
for i in range(n):
    for j in range(n-i-1):
        print('_',end="")
    for j in range(i+1):
        print("#",end="")
    print()    
                
    