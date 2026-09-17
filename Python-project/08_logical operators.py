

temp = float(input("The temperature is: "))
is_raining = input("raining or NOT?(False/True):")#非空字符串任然默认为True

if temp > 35 or temp< 0  or is_raining == "True":
    print("Outdoor event will be canceled")
else:
    print("Outdoor event is still scheduled🤪")

