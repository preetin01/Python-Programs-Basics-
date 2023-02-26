t=int(input("enter the no of test case: "))
count=0
for i in range(t):
    n,a,b=map(int,input().split())
    while(n):
        n=n/2
        count+=1
    print((count*a)+(count-1)*b)    
        