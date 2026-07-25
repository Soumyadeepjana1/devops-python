# restaurant billing system

# Pizza = ₹200
# Burger = ₹120
# Cold Drink = ₹50

print(" welcome to ABC restaurant ")

print("pizza = 200")
print("burger = 120")
print("cold drink = 50")

food = input("enter your food (ex - burger, pizza, cold drink): ").strip().lower()

if food == "pizza":
    print("your bill is 200")
elif food == "burger":
    print("your bill is 120")
elif food in ("cold drink", "cold drinks"):
    print("your bill is: 50")
elif "pizza" in food and "burger" in food:
    print("your bill is: 320")
elif "burger" in food and "cold drink" in food:
    print("your bill is: 170")
elif "cold drink" in food and "pizza" in food:
    print("your bill is: 250")
else:
    print("item not recognized or total bill calculated")