mydict={"Name":"Preeti",
        "age":19,
        "roll no":[1,6,3],
        "sister":{"PN":"sushmo"}
        }
print(mydict['Name'])
print(mydict['roll no'])
print(mydict['sister']['PN'])
mydict['age']=18     #update the valu of the key "age" of the dictionary
print(mydict['age'])