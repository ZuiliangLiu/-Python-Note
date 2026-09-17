#str() ,int() ,float() ,bool()
# type()输出类型
name = "Bro code"
age = 25
gpa = 3.2
is_student = True

print(type(name))
print(type(age))
print(type(is_student))

age += 1
print(age)
age =str(age)
age += "1"
print(age)

name = bool(name)
print(name)

name1 = ""
name1 = bool(name1)
print(name1)