n=int(input("enter the number: "))
sum=0
for num in range(2,n+1):
    for i in range(2,num):
        if num%i==0:
            break     
    else:
        print(num)
        sum+=num
print("the sum of all prime number is ",sum)        
           
        
        
        
        
