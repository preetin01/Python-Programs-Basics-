N=int(input("enter the number"))
for i in range(N-1):
    for j in range(i+1):
        print(i+1,end="")
    print()

#OR

for i in range(1,int(input())):
    print (i * int(bin(2**i - 1)[2:]))
        