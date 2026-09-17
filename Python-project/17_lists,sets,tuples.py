#四个通用集合
fruits = ["apple","banana","mango","pineapple"]
# print(fruits[::3])
# print(fruits[0:3])
for fruit in fruits:
    print(fruit,end=" ")
print("apple" in fruits)

# fruits[3]="coconut"
# fruits.append("coconut")
# fruits.remove("apple")
# fruits.insert(0,"orange")#具体索引替换
# fruits.sort()#按首字母排序
# fruits.reverse()#倒转

print(fruits)

#Set{}中的元素是无序的且无法重复，可以增加删除但无法索引

#Tuple()可被查找，不可更改但可以重复，速度更快



