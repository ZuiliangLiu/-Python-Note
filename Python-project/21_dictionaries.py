# dictionary = {"keys":"values"}

capitals = {"USA":"Washington D.C.",
            "UK":"london",
            "France":"Paris",
            "China":"Beijing"}

# capital = capitals.get(input("Enter your country:"))
# print(capital)

# if capitals.get(input("Enter your country:")):
#     print("Capital is exist")
# else:
#     print("Capital is not exist")

# capitals.update({"Germany":"Berlin"})
# print(capitals)
# capitals.update({"France":"ABC"})
# capitals.pop("USA")
# print(capitals)
# capitals.popitem()#只能删除最新的一个
# print(capitals)
# capitals.clear()
# print(capitals)
# keys = capitals.keys()
# print(keys)

items = capitals.items()
for key, value in items:
    print(f"{key}, {value}")