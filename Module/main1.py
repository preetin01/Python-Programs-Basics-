import mod1 as md

addition =md.add(10,20)
print(addition)

print('*****************')
#import module with anotherr name
from mod1 import divide

result=divide(20,10)
print(result)


print('*****************')
# to import all function from module use '*' 

from mod1 import *

res_add=add(4,5)
res_sub=sub(10,5)
res_mul=mul(9,8)
res_div=divide(90,9)

print(res_add)
print(res_sub)
print(res_mul)
print(res_div)