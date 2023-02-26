#Print 1 To N Without Loop
def fun(n):
    if n<=0:
        return
    fun(n-1)
    print(n,end=' ')
    
m=int(input('enter the number')) 
fun(m)   