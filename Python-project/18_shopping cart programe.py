foods = []
prices = []
total_price = 0


while True:
    food = input("Please enter your food:(food/N) ")
    if food == "N":
        break

    else:
        price = float(input(f"Please enter your {food} price:$ "))
        foods.append(food)
        prices.append(price)


total_price = sum(prices)

print("------Your Cart------")
for food in foods:
    print(food,end=" ")
print()

print(f"Total price: {total_price}")






