#Mod Division
a=int(input("enter the divisor:"))
b=int(input("enter the divident:"))
q=int(a/b)
r=a%b
print("The value of quotent is:",q)
print("The value of remainder is:",r)
print(divmod(a,b))

#Power - Mod Power
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
m=int(input("enter the third number:"))
print("Power of a and b:",pow(a,b))
print("Power of a,b and c:",pow(a,b,m))