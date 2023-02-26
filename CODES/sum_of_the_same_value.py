# count the element which is greater than 10 in list
l=list(map(int,input().split()))
count=0
for i in range(len(l)):
    if l[i]>=10:
        count+=1
print(count)



t=int(input())
for i in range(t):
    n=int(input())
    count=0
    l=list(map(int,input().split()))
    for j in range(len(l)):
        if l[j]>=1000:
            count+=1
    print(count)        




t=int(input('enter test cases: '))
for i in range(t):
    n , m=list(map(int,input('enter n an m : ').split()))
    arr=[]
    res=abs(n[i]-m[i])
    arr.append(res)
print('array is: ',arr)