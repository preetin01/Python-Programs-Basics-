
print("select the operation to perform")
print("-------------------------------")
print("1.sum")
print("2.subtract")
print("3.multiply")
print("4.divide")
print("5.Exit")
print("---------")
while(True):    
    i=int(input("Enter your choice:"))
    a=int(input("Enter the first number"))
    b=int(input("Enter the second number"))
    if i==1:
        sum=a+b
        print(sum)
    elif i==2:
        sub=a-b
        print(sub)
    elif i==3:
        mul=a*b
        print(mul)
    elif i==4:
        c=(a/b)
        div="{:.2f}".format(c)
        print(div)   
    elif i==5:
        print("Exit")
        break               
    else:
        print("Wrong Choice")        