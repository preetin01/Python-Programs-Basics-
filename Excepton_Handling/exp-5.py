#exceptoin handling for array out of index
array=[1,2,3,4,5]
for i in range(8):
    try:
        print("i=",array[i])
    except:
        print("error")    