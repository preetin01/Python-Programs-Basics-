'''
Given an array of strings words, return the words that can be typed using letters of the alphabet 
on only one row of American keyboard like the image below.

In the American keyboard:
the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".

Example 1:
            Input: words = ["Hello","Alaska","Dad","Peace"]
            Output: ["Alaska","Dad"]
'''

string_array=eval(input("enter the array"))
s=[]
for i in string_array:
    s.append(i.lower())
row1="qwertyuiop"
row2="asdfghjkl"
row3="zxcvbnm"
flag=True
s1=[]
for j in s:
    if j[0] in row1:
        for k in j:
            if k not in row1:
                flag=False
    elif j[0] in row2:
        for k in j:
            if k not in row2:
                flag=False
    elif j[0] in row3:
        for k in j:
            if k not in row3:
                flag=False
    if flag==True:
        s1.append(j)      
print(s1)