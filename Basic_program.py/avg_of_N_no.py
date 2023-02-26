from re import I




#AVERAGE OF N NUMBER

N=int(input("enter the number: "))
sum=0
for num in range(1,N+1):
    print(num)
    sum+=num
    avg=sum/N
print("the average of N number is ",avg)    
    
