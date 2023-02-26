#The finally block gets executed no matter if try block raise any error or not
try:
    print("x= ",x)
except:
    print("something went wrong")
finally:
    print("The 'try except' is finished")        