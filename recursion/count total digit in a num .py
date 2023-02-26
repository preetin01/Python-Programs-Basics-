# count total digit in a number

def countdigit(n):
    count=0
    while n!=0:
        n=n//10
        count=count+1
    return count


num=int(input('enter the number: '))
print('The total digit in a number',num,'is ',countdigit(num))     