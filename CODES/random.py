#generating random real number
'''import random as r

print("the random number is: ",r.uniform(1,100))
print("two decimal place: ",round(r.uniform(1,100),2))
'''
#generating random string

'''import string as s
import random as r
print("string: ", s.ascii_letters) 
letter=r.sample(s.ascii_letters,5)
print(letter)'''

#generating random digit (otp)

import string as s
import random as r
print("digit: ",s.digits)
digit=r.sample(s.digits)
print("the otp is: ",digit)

#generating random password 
#splchar=@!#$%^&*
#password=r.sample(splchar+s.ascii_letters+s.digits ,12)