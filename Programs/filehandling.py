#EXCEPTION HANDLING

#the try block will generate an exception, because x is not defined:
try:
    print(x)
except:
    print("Anexceptionoccurred")
    
#Print one  message if the try block raises a NameError and another for other errors: 
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")
    
#In this example, the try block does not generate any error:
try:
    print("Hello")
except:
    print("Somethingwentwrong")
else:
    print("Nothingwentwrong")
    
#The finally block, if specified, will be executed regardless if the try block raises an error or not.
try:
    print(x)
except:
    print("Somethingwentwrong")
finally:
    print("The'tryexcept'isfinished")
 
 
#RAISE AN EXCEPTION
#raise an error and stop the program if x is lower than 0:
x=-1
if x<0:
    raise Exception("Sorry,nonumbersbelowzero")

#Raise a TypeError if x is not an integer:
x="hello"
if not type(x)is int:
    raise TypeError("Onlyintegersareallowed")
  