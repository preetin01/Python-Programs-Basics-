class car():
    def __init__(self,modelname,yearm,price):
        self.modelname=modelname
        self.yearm=yearm
        self.price=price

    def price_inc(self):
        self.price=int(self.price*1.15)
    
honda=car("city",2017,100000)
tata=car("bolt",2016,600000)        

honda.cc=1500  #add new value

print(honda.price)
honda.price_inc()
print(honda.price)
