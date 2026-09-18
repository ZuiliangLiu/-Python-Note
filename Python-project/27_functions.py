# def happy_birthday(name,age):
#     print(f"Happy {age}th birthday, {name}!")
#
#
# happy_birthday("Suise"  ,23)
#
#
# def add(x,y):
#     z = x+y
#     return z
# def subtract(x,y):
#     z = x-y
#     return z
# print(add(2,3))
# print(subtract(2,3))
# def add(a, b):
#     return a + b       # 可以保存、继续计算
#
# def show_add(a, b):
#     print(a + b)       # 只负责显示
#
# total = add(2, 3)
# print(total * 10)       # 50
# show_add(2, 3)          # 5

# def area(width: float, height: float) -> float:
#     """返回矩形面积。"""
#     return width * height
#
# print(area(3.5, 2))

def add_item(items, item):
    items.append(item)       # 会修改原列表

numbers = [1, 2]
add_item(numbers, 3)
print(numbers)               # [1, 2, 3]

