
#Palindrome check using recursion

def ispalindrome(arr,start,end):
    
    if start>=end:
        return 1 
    if(arr[start]==arr[end]):
        return ispalindrome(arr,start+1,end-1)
    else: 
        return 0
    
if __name__ == "__main__":
    arr=[1]
    n=len(arr)
    if (ispalindrome(arr,0,n-1)==1):
        print('Palindrome')
    else:
        print('Not Palindrome')          
