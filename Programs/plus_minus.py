def plusMinus(arr):
    # Write your code here
    pos_value=0
    neg_value=0
    zero_value=0
    for i in range(n):
        if arr[i]>0:
            pos_value+=1
        elif arr[i]<0:
            neg_value+=1
        else:
            zero_value+=1
    print(pos_value/n) 
    print(neg_value/n) 
    print(zero_value/n)                
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
       