n = int(input())
for i in range(n):
    x,y =map(int,input().split())

    if x<y:
        print('FIRST')
    elif x==y:
        print('ANY')
    elif x>y:
        print('SECOND')
    