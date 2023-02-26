import math
t=int(input("enter the no of test case: "))
for i in range(t):
    n,a,b=map(int,input().split())
    count=math.floor(math.log2(n))
    print((count*a)+(count-1)*b)    
        