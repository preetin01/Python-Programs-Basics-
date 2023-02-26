#Factorial Using Recursion

def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)


num=int(input('enter the number: '))
print('The factorial of',num,'is ',fact(num))