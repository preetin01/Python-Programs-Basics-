'''def func(a):
    yield a
a=[1,2,3] 
b=func(a)
#print(b)
next(b)   


def new(dict):
    for x,y in dict.items:
        yield x,y
a={1:'hi',2:'hello',3:'bello'}
b=new(a)
print(b)
#next(b)'''       


def myfunc(i):
    while i<3:
        yield i
        i+=1
j=myfunc(2)
next(j)        