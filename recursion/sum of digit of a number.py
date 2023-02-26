# sum of digit of a number

def sumdigit(n):
    sum=0
    if n<10:
        return n
    return sumdigit(n//10)+n%10

num=int(input('enter the number: '))
print('The sum of digit of number',num,'is ',sumdigit(num))    
    