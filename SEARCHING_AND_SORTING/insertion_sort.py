
#INSERTION SORTING

def insertion_sort(arr,n):

    for j in range(1,n):
        key=arr[j]
        i=j-1
        while (i>=0 and arr[i]>key):
            arr[i+1]=arr[i]
            i=i-1
        arr[i+1]=key
     
       
n=int(input("Enter the size of array:")) 
arr=[]
for element in range(n):
    element=int(input("Enter the array element:")) 
    arr.append(element)
print("Given array:",arr)    
insertion_sort(arr,n)          
print('sorted array:',arr) 