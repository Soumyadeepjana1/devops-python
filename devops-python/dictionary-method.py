info = {
    "name" : "soumyadeep",
    "age" : 22,
    "state" : "wb",
    "class" : "MCA"
}

print(info.keys()) # help to print all keys

print(info.values()) # help to print all values



print(info.items())  # help to print key and value pair 


db = list(info.items()) 
print(db[1])


print(info.get("class")) #help to print value of key

print(info.update({"ind" : "wc"}))   #help to add new ki value pair 

print(info)

