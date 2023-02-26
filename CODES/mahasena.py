n=int(input())
a=list(map(int,input().split()))
for i in range(len(a)):
    x=a[i]%2
    print(x)
    if x==0:
        print('READY FOR BATTLE')
    else:
        print('NOT READY')