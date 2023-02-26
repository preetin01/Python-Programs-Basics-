from itertools import groupby
s=input("enter the sting:-")
for i,j in groupby(s):
    print((len(list(j)),int(i)),end=" ")
  