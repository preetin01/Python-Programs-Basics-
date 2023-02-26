mydict={"name":"Preeti",
        "age":19,
        "roll no":[1,6,3],
        "sister":{"PN":"sushmo"}
}

print(mydict.keys())         #print the keys of the dictionary
print(type(mydict.keys()))   #give the type of the given contents
print(mydict.values())      #print the values of the  of the dictionary
print(mydict.items())       #print the (keys ,values) for all the contents of the dictionary  
print(mydict)
updatedict={
    "friend":"pg"
}
mydict.update(updatedict)      #update the dictionary by adding key-value pairs from updatedict
print(mydict)


#both give the same values associated with the key 'name'
print(mydict.get("name"))  
print(mydict['name'])


#the difference between the .get and [] synatax in dictionary
#but in this case
print(mydict.get('name1'))      #return none  as name1 is not present in the dictionary.
print(mydict['name1'])          #throw an error as  name1 is not present in the dictionary.
