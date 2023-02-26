

#SUM OF THE FIRST N POSITIVE NUMBER
n=int(input("How many number? "))
sum=0
for num in range(1,n+1):
    print(num)
    sum+=num
print("Sum of N positive number is",sum)    
 



#***************************************# 
n=int(input("Enter the number: "))
sum=(n*(n+1))/2
print("Sum is",sum)    