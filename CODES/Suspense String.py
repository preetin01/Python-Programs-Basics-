# cook your dish here
for i in range(int(input('enter the test cases: '))):
    n=int(input('enter the lenght of string: '))
    s=input('enter the string: ')
    t=''
    for j in range(len(s)):
        t=(s[j])+1
        t=(s[len(s)-j-1])+1
    print(str(t))