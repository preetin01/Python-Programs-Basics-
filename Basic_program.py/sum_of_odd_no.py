n=int(input('enter the number: '))
sum=0
for num in range(1,n+1):
    if num%2!=0:
        print(num)
        sum+=num
print('the sum of odd number is: ',sum)        