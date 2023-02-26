#constructor

class car():
    def __init__(self,modelname,yearm,price):
        self.modelname=modelname
        self.yearm=yearm
        self.price=price

honda=car("city",2017,100000)
tat=car("bolt",2016,600000)        

honda.cc=1500  #add new value

print(honda.price)

print(honda.__dict__)#if we want to see the complete values that is associated with the objects
