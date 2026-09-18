import random


low = 1
high = 100
number = random.randint(low, high)
print(number)

options = ("rock", "paper", "scissors")
print(random.choice(options))

print(random.random())

card = ["1","2","3","4","5","6","7","J","K","O"]
random.shuffle(card)#列表
print(card)
