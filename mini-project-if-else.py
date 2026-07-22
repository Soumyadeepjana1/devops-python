# resturdent billing system

# Pizza = ₹200
# Burger = ₹120
# Cold Drink = ₹50

print(" welcome to ABC resturdent ")

print("pizza = 200")
print("burger = 120")
print("cold drink = 50 ")

food = str(input("enter your food (ex - burger,pizza,cold drink): "))

if (food == "pizza"):
    print("your bill is 200")
elif(food == "burger"):
    print("your bill is 120")
elif(food == "cold drinks"):
    print("your bill is: 50")
elif(food == "pizza","burger"):
    print("your bill is: 320")
elif(food == "burger","cold drink"):
    print("your bill is:250")
elif(food == "cold drink","pizza"):
    print("your bill is: 250")
else:
    print("your bill is: 370")