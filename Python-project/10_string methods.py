
# name = input("Enter your full name: ")

# result = name
# print(f"The full name is {result}")

# result1 = name.find("l")#查找字符位置
# result2 = name.rfind("l")查找第二个字符位置
# print(result1)
# print(result2)

# result = name.capitalize() #将首字母大写
# result = name.upper() #将所有字母大写
# result = name.lower() #将所有字母小写
# result = name.isdigit()#只有都是数字时 返回True
# result = name.isalpha()#全为字母时返回True
# result = name.count("")
# result = name.replace("old", "new")


# print(help(str))
user_name = input("Enter your name: ")

if len(user_name) > 12:
    print("Your name is too long")
elif not user_name.find(" ") == -1:#没找到空格 返回-1
    print("Your name can't contain spaces")
elif not user_name.isalpha():#若全为字母返回Ture
    print("Your name can't contain numbers")
else:
    print(f"Welcome {user_name}!")



