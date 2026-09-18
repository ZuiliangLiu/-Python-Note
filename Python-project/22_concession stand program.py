# dictionary("key":"value")

menus = {"pizza":3.00,
        "hamburger":2.99,
        "chips":1.25}
total_price = 0
cart = []
menu = menus.items()

print("----------MENU----------")
for key,value in menu:
    print(f"{key:10}: ${value:.2f}")
while True:

    food = input("Select your food?(q to quit):")
    if food == "q":
        break
    elif food not in menus:
        print("Please enter a valid option")
    else:
        price = menus.get(food)
        total_price = total_price + price
    cart.append(food)

for food in cart:
    print(food,end="")
print()

print(f"You need pay ${total_price:.2f}")
print("------------------------")