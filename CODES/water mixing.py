for i in range(int(input())):
    a,b,x,y=map(int,input().split())
    diff=a-b
    if diff==0:
        print('YES')
    elif diff<0:
        if abs(diff)<=x:
            print('YES')
        else:
            print('NO')
    else:
        if abs(diff)<=y:
            print('YES')
        else:
            print('NO')