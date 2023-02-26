# sum of n natural number

#using for loops

n=int(input("enter the number:-"))
sum=0
for i in range(n):
    sum=sum+n
    n=n-1
print(sum)


#using while loops

n=int(input("enter the number:-"))
sum=0
while n>=0:
    sum=sum+n
    n=n-1
print(sum)
