# num1 = int(input("enter your all age number: "))
# num2 = int(input("enter a number: "))
# num3 = int(input("enter a number: "))
# age = [num1,num2,num3]
# print(age)
# print(type(age))


num = [1,2,1]
num1 = num.copy()
num1.reverse()
if num1 == num:
    print("its palindrome")
else:
    print("not palindrome")