
# Finding the largest number
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
c=int(input("enter the third number:"))
if a>=b and a>=c:
    print("The largest number a is ",a)
elif b>=a and b>=c:
    print("The largest number b is ",b)  
else:
    print("the largest number c is ",c)      
    