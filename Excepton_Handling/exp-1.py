for i in range(-5,6):
   print("100/",i,"=",100/i)
    
#how to handle the above exception
for i in range(-5,6):
    try:
        print("100/",i,"=",100/i)
    except:
        print('error')    
        