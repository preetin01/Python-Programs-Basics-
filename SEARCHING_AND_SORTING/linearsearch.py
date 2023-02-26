
#LINEAR SEARCHING

list=[]
num=int(input("Enter size of the list: "))
for n in range(num):
    numbers=int(input("Enter any number: "))
    list.append(numbers)
found=False
x=int(input("Enter a number to searched: "))
for i in range(len(list)):
   if x==list[i]:
        found=True
        print("\n%d found at position %d"%(x,i))
        break
if not found:
    print("\n%d is not in list "%x)