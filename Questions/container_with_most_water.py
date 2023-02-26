'''
You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

>>Input1: height = [1,8,6,2,5,4,8,3,7]
Output: 49

>>Input2:[1,3,2,1,5,2]
Output:9
'''
height=eval(input('enter the list:->'))
s=0
e=len(height)-1
area=0
list=[]
while s<=e:
    if height[s]>height[e]:
        area=(e-s)*height[e]
        e-=1
    else:
        area=(e-s)*height[s]
        s+=1
    list.append(area)
print(max(list))           
           