x = 3.14
y = -4
z = 5


# result1 = round(x)
# print(result1)
#
# result2 = abs(y)
# print(result2)
#
# result3 = pow(3,4)
# print(result3)
#
# reslut4 = max(x,y,z)
# print(reslut4)
#
# reslut5 = min(x,y,z)
# print(reslut5)

# import math
# print(math.pi)
#
# print(math.sqrt(x))  #根号
#
# print(math.ceil(9.1))  #向上取整
#
# print(math.floor(9.1))  #向下取整

import math

radius = float(input("Enter the radius of a circle: "))

area = math.pi * pow(radius, 2)  # 

print(f"The area of the circle is: {round(area, 2)}cm²") # round(data,x)取x整数