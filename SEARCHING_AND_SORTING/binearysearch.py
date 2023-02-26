
#BINARY SEARCH

def binarySearch(l,x):
    start= 0
    end=len(l)- 1
    while start <= end:
        mid = (start + end)//2
        if l[mid]==x:
            return mid
        elif l[mid]<x:
            start=mid+1
        else:
            end=mid-1
    return -1            
list= []
size = int(input("Enter size of list: "))
for i in range(size):
    n = int(input("Enter the elements of list: "))
    list.append(n)
list.sort()
print('The list will be sorted, the sorted list is: ',list)
key= int(input("Enter the number to search: "))
print('The key ',key,'is found at position: ',binarySearch(list,key))