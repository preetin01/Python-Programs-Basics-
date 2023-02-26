for _ in range(int(input('enter the no. of test cases: '))):
    n=int(input('enter the size of string: '))
    s=input('enter the string: ')
    d={}
    for i in s:
        if i in d:
            d[c]+=1 
    flag=False
    for j in d:
        if d[j]%2==1:
            print('NO')
            flag=False
            break
        else:
            continue
    if (not flag):
        print('YES')