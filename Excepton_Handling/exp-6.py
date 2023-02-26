Filename=input("Enter the file name: ")
try:
    fp=open(Filename)
    fp.close
except:
    print("file '%s' not found"%(Filename))   
     
print("Done")    