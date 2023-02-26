n =int(input())
for i in range(n):
    x,y=map(int,input().split())

    if x<2*y:
        print('NO')
    elif 2*x>y:
        print('YES')
