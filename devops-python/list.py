age = [12,13,161,17]
print(len(age))
print(age[12:16])
age[0] = 16
print(age)
print(age[0:2]) #list sliyacing

age.append(19) # append funcation help to add one eliment in list
print(age) 

age.sort()  #help to sort small to big


age.sort(reverse=True) # help to sort big to small

age.reverse() #help to print reverse element

age.insert(3,15) #insert value (index,element)

print(age)