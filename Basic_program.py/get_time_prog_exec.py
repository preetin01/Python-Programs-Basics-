
#HOW TO GET THE TIME OF A PROGRAM'S EXECUTION
import time 
def myfunc():
    start_time=time.time()
    s=0
    for i in range (1,n+1):
        s+=i
    end_time=time.time()
    return s,end_time-start_time

n=int(input())
print(myfunc())    