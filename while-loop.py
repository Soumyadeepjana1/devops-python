# i = 100
# while i >=1:
#     print(i)
#     i-=1


# i = 1
# while i <= 10:
#     print(f"{10} * {i} = ",10*i)
#     i += 1





num = [1,4,9,16,25,36,49,64,81,100]
number = [1,4,9,16,25,36,49,64,81,100]
# i = 0
# while i < len(num):
#     print(num[i])
#     i += 1

# for i in num:

#     print(i)

# for i in number:
#     index = number.index(i)
#     print(index)    


i = 0 
while i < len(number):
    if number[i] == 36:
        print("found",i)
        break
    else:
        print("not found")
            
    i += 1