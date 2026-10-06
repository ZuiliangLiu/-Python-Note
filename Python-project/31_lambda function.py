outline = lambda :print("-----------")#匿名函数定义，只能用在简单函数上
add = lambda x,y:x + y
outline()
print(add(10,20))


data_list = ["C++","Python","Jack","PHP","Java","Go","JavaScript","Rust"]#按首字符字符顺序进行排序
data_list.sort()
print(data_list)

data_list.sort(key = lambda list:len(list))#作为参数传递
print(data_list)