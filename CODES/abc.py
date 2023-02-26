'''def fizzBuzz(n):
    res=[]
    for i in range(1,n+1):
        if i%3==0 and i%5==0:
            res.append('FizzBuzz')
        if i%3==0 and i%5!=0:
            res.append('Fizz') 
        if i%3!=0 and i%5==0:
            res.append('Buzz')
        else:
            ans=str(i)
            
        res.append(ans)    
    print(res) 
n=int(input('enter the number: '))
fizzBuzz(n)  '''             

def fizzBuzz(n):
    res = []
    num= ""
    for i in range(1, n + 1): 
        num = str(i)
        if i % 3 == 0 and i % 5 == 0:
            num = "FizzBuzz"
        if i % 3 == 0:
            num = "Fizz"
        if i % 5 == 0:
            num= "Buzz"
        else:
            res.append(num)
    print(res)
n=int(input("enter the nuumber: "))  
fizzBuzz(n)  